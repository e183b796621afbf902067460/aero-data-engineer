from airflow.decorators import task, dag
from airflow.exceptions import AirflowSkipException
from airflow.utils.trigger_rule import TriggerRule

import pendulum
import datetime


@task()
def e_from_api_datasource() -> dict:
    from req



@dag(
    dag_id='to_datalake',
    start_date=pendulum.datetime(2023, 1, 1, tz="UTC"),
    schedule_interval='*/10 * * * *',
    catchup=False,
    max_active_runs=1,
    dagrun_timeout=datetime.timedelta(minutes=10)
)
def to_datalake():
    from resources.datalake.resource import s3_datalake
    from resources.datamart.resource import ch_datamart


to_datalake_dag = to_datalake()
