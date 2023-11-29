from sqlalchemy import create_engine
import pandas as pd
import os

db_name = os.getenv('DB_NAME_SEMINAR2')
db_user = os.getenv('DB_USER')
db_host = os.getenv('DB_HOST')
db_pw = os.getenv('DB_PW')
db_port = os.getenv('DB_PORT')

engine = create_engine(f'postgresql://{db_user}:{db_pw}@{db_host}:{db_port}/{db_name}')

def read_sql(sql: str) -> pd.DataFrame:
    return pd.read_sql(sql, engine)
