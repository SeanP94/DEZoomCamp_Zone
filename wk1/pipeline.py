import pandas as pd
import requests
from io import BytesIO
from sqlalchemy import create_engine
import argparse


def main(params):
    user = params.user
    password = params.password
    host = params.host
    port = params.port
    db = params.db
    table_name = params.table_name
    # url = params.url



    # Connect to docker postgres.
    engine = create_engine(f'postgresql://{user}:{password}@{host}:{port}/{db}')

    # Read Parquet 
    file =  requests.get('https://d37ci6vzurychx.cloudfront.net/trip-data/yellow_tripdata_2024-01.parquet')
    df = pd.read_parquet(BytesIO(file.content))


    # Create table
    df.head(0).to_sql(name=table_name, con=engine, if_exists='replace')
    chunk_size = 100000

    print("Beginning yellow_taxi_data insert")
    # Insert by chunk_size
    for it in [df[i:i+chunk_size] for i in range(0, df.shape[0], chunk_size)]:
        it.to_sql(name=table_name, con=engine, if_exists='append')
    print("Complete!")

if __name__ == '__main__':

    parser = argparse.ArgumentParser(description="Ingest Data for PGsql")
    parser.add_argument('--user', help='')
    parser.add_argument('--password', help='')
    parser.add_argument('--host', help='')
    parser.add_argument('--port', help='')
    parser.add_argument('--db', help='')
    parser.add_argument('--table_name', help='')
    # parser.add_argument('url', help='')
    args = parser.parse_args()

    main(args)

'''
python wk1/pipeline.py \
    --user=root \
    --password=root \
    --host=localhost \
    --port=5435 \
    --db=root \
    --table=yellow_taxi_data 
'''

'''
docker run -it \
    --network="host" \
    taxi_ingest:v001 \
        --user=root \
        --password=root \
        --host=localhost \
        --port=5435 \
        --db=root \
        --table=yellow_taxi_data 
'''

