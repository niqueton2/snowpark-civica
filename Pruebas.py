import snowflake_connection as Snk
from snowflake.snowpark import Session

session=Snk.snow_session()

a=session.table('personas')

print(a.show())

 
