from snowflake.snowpark import Session

aver=SnowflakeConn()

a=spk.table('personas')

print(a.show())
 
