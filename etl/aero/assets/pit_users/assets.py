from typing import List
import requests
from dagster import asset
import pandas as pd

from framework.bridge.bridge import Bridge
from framework.abstracts.abstracts import sourceAbstractFabric


@asset(name='df', required_resource_keys={'logger', 'df_serializer'})
def do(context, configs: dict) -> List[list]:

    r = requests.get(url=configs['endpoint'])
    if r.status_code != 200:
        raise ValueError('Bad request.')

    handler = Bridge(
        abstract=sourceAbstractFabric,
        fabric_name='users',
        handler_name=configs['source']
    ).produce_handler()
    handler.do(json_=r.json())

    df = pd.DataFrame([handler.pit_users])
    df['h_source'], df['h_endpoint'] = configs['source'], configs['endpoint']
    return context.resources.df_serializer.df_to_list(df)
