import pandas as pd
from sqlalchemy import create_engine

def get_engine(self):
        #SQL Connection Windows Authentication#

        Server = 'UKC-VM-SQL01'
        Database = 'Stencil'
        Driver = 'ODBC Driver 17 for SQL Server'
        Database_con = f'mssql://@{Server}/{Database}?driver={Driver}'

        engine = create_engine(Database_con)
        con = engine.connect()


        #df.to_sql('StencilUsage', con, if_exists='append', index = False)
        