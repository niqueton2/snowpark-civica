
from snowflake.snowpark import Session

from snowflake_connection import SnowflakeConn

sc = SnowflakeConn()

snpk = sc.snow_session()

Personas = snpk.table("personas")

print(Personas.show())