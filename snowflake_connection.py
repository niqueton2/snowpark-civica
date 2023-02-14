from snowflake.snowpark import Session
from snowflake_connection import SnowflakeConn
# Necsitamos lo dea rriba para llamar a snowflake 

# SC=SnowflakeConn
# snk=SC.snow_session()
# snk.sql("select ...")

class SnowflakeConn:

    
    def __init__(self):
        
        self.connection_parameter = {"user": "NICOLAS.GARCIA@CIVICA-SOFT.COM", 

                     "authenticator":"externalbrowser", 

                     "account": "civicapartner.west-europe.azure", 

                     "warehouse": "WH_BASICO", 

                     "database": "NGARCIA_DB", 

                     "schema": "EDUCA"} 
        
    
    def close(self):
    
        Session.close() 


    def snow_session(self):
                
        spk = Session.builder.configs(self.connection_parameter).create()
        return spk