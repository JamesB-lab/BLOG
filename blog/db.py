import pandas as pd
from sqlalchemy import create_engine

def get_engine(Server, Database, Driver):
        #SQL Connection Windows Authentication#

        Database_con = f'mssql://@{Server}/{Database}?driver={Driver}'

        engine = create_engine(Database_con)
        return engine


        #df.to_sql('StencilUsage', con, if_exists='append', index = False)
        