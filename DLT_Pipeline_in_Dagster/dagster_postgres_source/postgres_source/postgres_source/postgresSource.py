
import dlt
from dlt.sources.sql_database import sql_database

@dlt.source
def postgres_source():
    
    # declaring a source that will interact with postgres database
    # Fetching all the tables from postgres source
    # source = sql_database()
    
    # Extracting only employees and customers table from the source
    source = sql_database().with_resources("employees" , "customers")

    # Applying incremental loading on employees table on the basis of it's primary key as we don't have any timestamp column yet
    source.employees.apply_hints(incremental=dlt.sources.incremental("employee_id" , initial_value=10) , write_disposition="merge" , primary_key="employee_id")

    return source
