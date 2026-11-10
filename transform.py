import pandas as pd

df = pd.read_csv("data/raw_news.csv")

df["published"] = pd.to_datetime(df["published"], utc=True)

source_names = {"Lenta.ru : Новости": "lenta", "ТАСС": "tass", "Интерфакс": "interfax"}
df["source"]=df["source"].map(source_names)

print("До:", len(df))
df = df.drop_duplicates(subset="url")
df = df.reset_index(drop=True)
print("После:", len(df))

df["loaded_at"] = pd.Timestamp.now(tz="UTC")

df.to_csv("data/clean_news.csv", index=False)

print(df.head())
df.info()
print(df["source"].value_counts())