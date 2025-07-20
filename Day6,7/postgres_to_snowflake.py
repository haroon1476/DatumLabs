
# <------------------------ EXTRACTING DATA FROM A SOURCE POSTGRES DATABASE TO A DESTINAKE SNOWFLAKE WAREHOUSE ---------------->

import dlt
from dlt.sources.sql_database import sql_database
from dlt.common.pendulum import pendulum

@dlt.source
def postgres_source():

    # connection string to connect to postgres database
    credentials = "postgresql+psycopg2://postgres:neEs2w6QNU0YplJMChzGuxA8Zo7DI93@104.248.248.69:54321/postgres"

    # Creating a source object to interact with sql database of postgres
    source = sql_database(credentials=credentials)
    
    return source

@dlt.resource(name="employeeTable" , primary_key="employee_id")
def employeeResouce(db):

    # Applying level one unnesting to employees table in postgres database
    employeeResource = db.employees
    employeeResource.max_table_nesting = 1
    yield from employeeResource


@dlt.resource(name="CustomerTable" , primary_key="customer_id")
def customerResource(db):

    # Applying level one unnesting to both customers table in postgres database
    customerResource = db.customers
    customerResource.max_table_nesting = 1
    yield from customerResource
    

def run_postgres_to_snowflake():

    source = postgres_source() # to interact with source db

    # creating a pipeline to connect source with destination
    pipeline = dlt.pipeline(

        pipeline_name="postgres_to_snowflake",
        destination="snowflake",
        dataset_name="postgres_employees_customers_unnested_data"
    )


     # applying incremetal loading to customers table in source on the basis of 'last_modified' column attribute
    source.customers.apply_hints(incremental=dlt.sources.incremental(
        "last_modified", initial_value = pendulum.datetime(2024, 4, 1, 0, 0, 0, tz="UTC")) , write_disposition="merge" , primary_key="customer_id")

    # applying hints on remaining table on the basis of primary keys
    source.items.apply_hints(incremental=dlt.sources.incremental("item_id" , initial_value=1) , write_disposition="merge" , primary_key="item_id")

    #Applying incremental loading on the basis of an 'int' type attribute and providing the initial value to it
    source.customers.apply_hints(incremental=dlt.sources.incremental("customer_id" , initial_value=10) , write_disposition="merge" , primary_key="customer_id")

    source.orders.apply_hints(incremental=dlt.sources.incremental("order_id" , initial_value=1) , write_disposition="merge" , primary_key="order_id")
    
    source.stores.apply_hints(incremental=dlt.sources.incremental("store_id" , initial_value=1) , write_disposition="merge" , primary_key="store_id")

    source.employees.apply_hints(incremental=dlt.sources.incremental("employee_id" , initial_value=1) , write_disposition="merge" , primary_key="employee_id")


    info = pipeline.run([employeeResouce(source), customerResource(source)] , write_disposition="merge")
    print("DLT load info:", info)

if __name__ == "__main__":
    run_postgres_to_snowflake()