import feedparser
import requests

addresses = ["https://lenta.ru/rss", "https://tass.ru/rss/v2.xml", "https://www.interfax.ru/rss.asp"]

def extract(addresses):
    news=[]
    for address in addresses:
        try:
            response = requests.get(address, timeout=10)
            response.raise_for_status()
            feed = feedparser.parse(response.content)
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

rows=extract(addresses)
print("Всего новостей:", len(rows))
print(rows)
            