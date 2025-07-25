from dagster import Definitions, load_assets_from_modules
from postgres_source import assets  # noqa: TID252
from dagster_embedded_elt.dlt import DagsterDltResource
from .jobs import run_postgres_asset
from .schedules import postgres_job_schedule

dlt_resource = DagsterDltResource()
all_assets = load_assets_from_modules([assets])

defs = Definitions(
    assets=all_assets,
    resources={
        "dlt": dlt_resource,
    },

    jobs=[run_postgres_asset],
    schedules=[postgres_job_schedule]
)
