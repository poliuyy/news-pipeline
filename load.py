import os
import psycopg2
import pandas as pd
from dotenv import load_dotenv

load_dotenv()

df = pd.read_csv("data/clean_news.csv")

conn = psycopg2.connect(
    host=os.getenv("DB_HOST"),
    port=os.getenv("DB_PORT"),
    dbname=os.getenv("DB_NAME"),
    user=os.getenv("DB_USER"),
    password=os.getenv("DB_PASSWORD")
)

cur = conn.cursor()

cur.execute("select count(*) from news;")
before = cur.fetchone()[0]

for row in df.itertuples(index=False):
    cur.execute(
        """
        insert into news(title, url, published, source, loaded_at)
        values (%s, %s, %s, %s, %s)
        on conflict (url) do nothing;
        """, 
        (row.title, row.url, row.published, row.source, row.loaded_at))

conn.commit()

cur.execute("select count(*) from news;")
after = cur.fetchone()[0]
print ("Было:", before, "Стало:", after, "Добавлено:", after - before)

cur.close()
conn.close()
