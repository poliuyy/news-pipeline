import pandas as pd

df = pd.read_csv("data/raw_news.csv")
df["published"] = pd.to_datetime(df["published"], utc = True)
print(df.head())
df.info()