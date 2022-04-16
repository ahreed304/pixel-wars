import pandas as pd
from sqlalchemy import create_engine
import psycopg2

conn_string = 'postgresql+psycopg2://postgres:pass@127.0.0.1/reddit'
db = create_engine(conn_string)

conn = psycopg2.connect("dbname=reddit user=postgres password=foo")
conn.autocommit = True
cursor = conn.cursor()

prefix = 'https://placedata.reddit.com/data/canvas-history/2022_place_canvas_history-0000000000'
extension = '.csv.gzip'
for i in range(0, 79):
    url = f'{prefix}{str(i).zfill(2)}{extension}'
    print(f'Downloading file {url}...    ', end='', flush=True)
    df = pd.read_csv(url, compression='gzip')

    print(f'Processing...    ', end='', flush=True)
    df['x'] = df['coordinate'].str.split(',').str[0]
    df['y'] = df['coordinate'].str.split(',').str[1]
    df = df.drop('coordinate', axis=1)

    print(f'Loading into database...    ', end='', flush=True)
    df.to_sql('pixel_placement3', db, if_exists='append')
    conn.commit()
    print(f'Done')

conn.close()
