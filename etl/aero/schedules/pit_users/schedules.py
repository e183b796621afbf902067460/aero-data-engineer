from dagster import ScheduleDefinition

from aero.jobs.pit_users.jobs import dag


every_12th_hour = ScheduleDefinition(
    name='pit_users',
    job=dag,
    cron_schedule="0 */12 * * *"
)
