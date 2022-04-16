import pandas as pd
from sqlalchemy import create_engine, Column, Integer, String, ForeignKey, DateTime
from sqlalchemy.orm import declarative_base
import psycopg2

table_name = 'pixel_placement'

Base = declarative_base()

class Pixel_placement(Base):
    __tablename__ = table_name

    id = Column(Integer, primary_key=True)
    timestamp = Column(DateTime)
    user_id = Column(String)
    pixel_color = Column(String)
    x = Column(Integer)
    y = Column(Integer)

conn_string = 'postgresql+psycopg2://postgres:pass@127.0.0.1/reddit'
db = create_engine(conn_string)

conn = psycopg2.connect("dbname=reddit user=postgres password=admin")
conn.autocommit = True
cursor = conn.cursor()

Base.metadata.create_all(db)

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
    df.to_sql(table_name, db, if_exists='append', index=False)
    conn.commit()
    print(f'Done')

conn.close()









