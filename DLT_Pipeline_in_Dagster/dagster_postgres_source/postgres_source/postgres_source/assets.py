import dlt
from dagster import AssetExecutionContext
from dagster_embedded_elt.dlt import DagsterDltResource, dlt_assets
from .postgresSource import postgres_source  

@dlt_assets(

    # getting all the tables from the source
    dlt_source=postgres_source(),
    
    # setting up a pipeline
    dlt_pipeline=dlt.pipeline(

        pipeline_name="postgres_snowflake_via_dagster",
        dataset_name="dagster_postgres_data",
        destination="snowflake",
        progress="log",
    ),
    name="postgres_asset",  # this basically defines my asset name
    group_name="postgres",
)
def dagster_postgres_assets(context: AssetExecutionContext, dlt: DagsterDltResource):

    context.log.info("Starting postgres to Snowflake data ingestion")
    context.log.info("Source = Postgres , Destination = Snowflake")
    
    try:
        # Running the pipeline
        yield from dlt.run(context=context)
        context.log.info("Successfully completed postgres to Snowflake data ingestion")
        
    except Exception as e:
        context.log.error(f"Error {e} occured during data ingestion. Ingestion failed!")
        raise