import dagster as dg
from .assets import dagster_postgres_assets

run_postgres_asset = dg.define_asset_job("run_postgres_asset", selection='group:"postgres"')