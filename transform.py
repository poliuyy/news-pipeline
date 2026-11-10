import pandas as pd

df = pd.read_csv("data/raw_news.csv")
df["published"] = pd.to_datetime(df["published"], utc = True)
source_names = {"Lenta.ru : Новости": "lenta", "ТАСС": "tass", "Интерфакс": "interfax"}
df["source"]=df["source"].map(source_names)
print(df.head())
df.info()
print(df["source"].value_counts())