from airflow.decorators import task, dag
from airflow.utils.trigger_rule import TriggerRule

from resources.datalake.resource import S3DataLakeResource

import pendulum
import datetime


@task()
def e_from_api_datasource() -> dict:
    import pandas as pd
    import requests

    response = requests.get('https://random-data-api.com/api/cannabis/random_cannabis?size=10').json()
    df = pd.DataFrame(data=response)

    return df.to_dict(orient='list')


@task(trigger_rule=TriggerRule.ALL_SUCCESS)
def l_to_datalake(df: dict, s3: S3DataLakeResource, dt: datetime.datetime) -> None:
    import pandas as pd

    dt = dt.strftime("%Y-%m-%d %H:%M:%S")
    df = pd.DataFrame.from_dict(df)
    df['ts'] = dt

    df.rename(
        columns={
            "id": 'dm_cannabis_id',
            "uid": "dm_cannabis_uid",
            "strain": "dm_cannabis_strain",
            "cannabinoid_abbreviation": "dm_cannabis_cannabinoid_abbreviation",
            "cannabinoid": "dm_cannabis_cannabinoid",
            "terpene": "dm_cannabis_terpene",
            "medical_use": "dm_cannabis_medical_use",
            "health_benefit": "dm_cannabis_health_benefit",
            "category": "dm_cannabis_category",
            "type": "dm_cannabis_type",
            "buzzword": "dm_cannabis_buzzword",
            "brand": "dm_cannabis_brand",
            'ts': 'dm_cannabis_timestamp'
        },
        inplace=True
    )

    s3.to_csv(df=df, path=f"s3://datalake-bucket/cannabis/{dt}")


@dag(
    dag_id='to_datalake',
    start_date=pendulum.datetime(2023, 1, 1, tz="UTC"),
    schedule_interval='*/1 * * * *',
    catchup=False,
    max_active_runs=1,
    dagrun_timeout=datetime.timedelta(minutes=1)
)
def to_datalake():
    from resources.datalake.resource import s3_datalake

    s3, now = s3_datalake(), datetime.datetime.now()

    df = e_from_api_datasource()
    l_to_datalake(
        df=df,
        s3=s3,
        dt=now
    )


to_datalake_dag = to_datalake()
