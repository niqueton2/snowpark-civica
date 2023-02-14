
from snowflake.snowpark import Session
import pandas as pd 
from snowflake_connection import SnowflakeConn

sc = SnowflakeConn()

snpk = sc.snow_session()

Personas = snpk.table("personas")
ElRey = snpk.sql("select NOMBRE from personas where id_persona=2 ")
print(ElRey.show())




