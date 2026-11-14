import os
import pandas as pd
import psycopg2
from google.cloud import bigquery

host = os.environ["PG_HOST"]
database = os.environ["PG_DATABASE"]
user = os.environ["PG_USER"]
password = os.environ["PG_PASSWORD"]

conn = psycopg2.connect(
    host=host,
    database=database,
    user=user,
    password=password
)

query = "SELECT * FROM products"

df = pd.read_sql(query, conn)

client = bigquery.Client()

table_id = "ida2projekt.morele_dw.products"

job = client.load_table_from_dataframe(
    df,
    table_id
)

job.result()

print(f"Załadowano {len(df)} rekordów do BigQuery")
