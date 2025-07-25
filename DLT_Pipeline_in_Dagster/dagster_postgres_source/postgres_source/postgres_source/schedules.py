import dagster as dg
from .jobs import run_postgres_asset

postgres_job_schedule = dg.ScheduleDefinition(

    job = run_postgres_asset,
    cron_schedule="*/5 * * * *",  # pipeline will run every 5 minutes

    # setting job on running state by default
    default_status=dg.DefaultScheduleStatus.RUNNING
)