from dagster import job

from aero.assets.pit_users.assets import do
from aero.ops.pit_users.ops import extract_from_vault, load_to_lake
from aero.resources.vault.resource import vault
from aero.resources.logger.resource import logger
from aero.resources.lake.resource import lake
from aero.resources.serializer.resource import df_serializer


@job(
    name='pit_users',
    resource_defs={
        'vault': vault,
        'lake': lake,
        'logger': logger,
        'df_serializer': df_serializer
    }
)
def dag():
    configs = extract_from_vault()
    overviews = configs.map(do)
    load_to_lake(overviews.collect())
