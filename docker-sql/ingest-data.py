
import os
import argparse

import pandas as pd
from sqlalchemy import create_engine
from time import time



def main(params):
    user=params.user
    password=params.password
    host=params.host
    port=params.port
    db=params.db
    table_name=params.table_name
    url= params.url
    url2= 'https://d37ci6vzurychx.cloudfront.net/misc/taxi_zone_lookup.csv'
    csv_name='output.csv.gz'
    csv_name2= 'output2.csv'
    os.system(f"wget {url} -O {csv_name}")
    os.system(f"wget {url2} -O {csv_name2}")
    engine= create_engine(f"postgresql://{user}:{password}@{host}:{port}/{db}")
    
    d= pd.read_csv(csv_name2)
    d.to_sql(name="Taxi_Zone", con=engine, if_exists='replace')
    df_iter= pd.read_csv(csv_name, iterator=True, chunksize=100000, low_memory=False)
    #df=next(df_iter)
    next(df_iter).head(n=0).to_sql(name=table_name, con=engine, if_exists='replace')

    while True:
        t_start= time()
        df=next(df_iter)
        
        df.tpep_pickup_datetime=pd.to_datetime(df.tpep_pickup_datetime)
        df.tpep_dropoff_datetime=pd.to_datetime(df.tpep_dropoff_datetime)
        
        df.to_sql(name=table_name, con=engine, if_exists='append')

        t_end=time()
        print('inserted another chunck..., took %.3f second' %(t_end-t_start))


if __name__== '__main__':
    parser= argparse.ArgumentParser(description='ingest CSV data to postgres')

    #user 
    #password 
    #host 
    #port 
    #database name 
    #table name 
    #url

    parser.add_argument('--user', help='user name for postgres')
    parser.add_argument('--password', help='password for postgres')
    parser.add_argument('--host', help='host for postgres')
    parser.add_argument('--port', help='port for postgres')
    parser.add_argument('--db', help='database for postgres')
    parser.add_argument('--table_name', help='table name for postgres')
    parser.add_argument('--url', help='table name for url')
    
    args=parser.parse_args()
    main(args)















    


# In[ ]:




