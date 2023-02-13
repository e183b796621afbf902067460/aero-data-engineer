from dagster import Definitions, AssetsDefinition

from aero.assets.pit_users.assets import do
from aero.ops.pit_users.ops import extract_from_vault, load_to_lake
from aero.jobs.pit_users.jobs import dag
from aero.schedules.pit_users.schedules import every_12th_hour
from aero.resources.vault.resource import vault
from aero.resources.logger.resource import logger
from aero.resources.lake.resource import lake
from aero.resources.serializer.resource import df_serializer


extract_from_vault = AssetsDefinition.from_op(extract_from_vault)
load_to_lake = AssetsDefinition.from_op(load_to_lake)


pit_users = Definitions(
    assets=[extract_from_vault, do, load_to_lake],
    jobs=[dag],
    resources={
        'vault': vault,
        'lake': lake,
        'logger': logger,
        'df_serializer': df_serializer
    },
    schedules=[every_12th_hour]
)
