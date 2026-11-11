import feedparser
import requests
import pandas as pd
import time 
import os



addresses = ["https://lenta.ru/rss", "https://tass.ru/rss/v2.xml", "https://www.interfax.ru/rss.asp"]

def download(address, attempts=3):
    for attempt in range(attempts):
        try:
            response = requests.get(address, timeout=10)
            if response.status_code == 404:
                break
            elif response.status_code == 200:
                return response.content
            else: print ("Попытка", attempt, "плохой статус", response.status_code)
        except Exception as e:
            print("Попытка", attempt, "не удалась", e)
        time.sleep(2)
    raise Exception ("Не удалось скачать: "+ address)
        
def extract(addresses):
    news=[]
    for address in addresses:
        try:
            feed = feedparser.parse(download(address))
            if feed.bozo:
                print("Ошибка:", feed.bozo_exception)
            else:
                for entry in feed.entries:
                    news.append({
                        "title": entry.title,
                        "url": entry.link,
                        "published": entry.get("published", "нет даты"),
                        "source": feed.feed.title
                    })
                    
                print("Источник:", feed.feed.title)
                print("Новостей:", len(feed.entries))
        except Exception as e:
            print(e)
    return news

def run_extract():
    rows=extract(addresses)
    print("Всего новостей:", len(rows))

    df=pd.DataFrame(rows)
    os.makedirs("data", exist_ok=True)
    df.to_csv("data/raw_news.csv", index=False) 

if __name__ == "__main__":
    run_extract()