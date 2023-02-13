from typing import List
from datetime import datetime

import pandas as pd
from dagster import op, DynamicOut, DynamicOutput


@op(
    name='configs',
    required_resource_keys={'vault', 'logger'},
    tags={'data_mart': 'pit_users'},
    out=DynamicOut(dict)
)
def extract_from_vault(context) -> List[dict]:
    query = '''
        SELECT
            h_sources.h_source,
            h_endpoints.h_endpoint
        FROM 
            l_sources_endpoints
        LEFT JOIN
            h_sources USING(h_source_id)
        LEFT JOIN
            h_endpoints USING(h_endpoint_id)
    '''
    context.resources.logger.info(f"{query}")

    samples = context.resources.vault.read(query=query)
    for sample in samples:
        source, endpoint = sample[0], sample[1]
        yield DynamicOutput(
            {
                'source': source,
                'endpoint': endpoint
            },
            mapping_key=f'subtask_for_{source}_users_endpoint'
        )


@op(
    name='load_to_lake',
    required_resource_keys={'lake', 'logger', 'df_serializer'},
    tags={'data_mart': 'pit_users'}
)
def load_to_lake(context, df: List[list]) -> None:
    now, concat_df = datetime.utcnow(), pd.DataFrame()
    for mini_df in df:
        mini_df = context.resources.df_serializer.df_from_list(mini_df)
        concat_df = concat_df.append(mini_df, ignore_index=True)
        context.resources.logger.info(mini_df.head())
    concat_df['pit_ts'] = now
    context.resources.lake.get_client().insert_df(
        table='pit_users',
        df=concat_df
    )
