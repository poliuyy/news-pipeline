import feedparser
import requests

addresses = ["https://lenta.ru/rss", "https://tass.ru/rss/v2.xml", "https://www.interfax.ru/rss.asp"]
for address in addresses:
    print(address)

    # for entry in feed.entries:
    #     print(entry.title)
    #     print(entry.link)
    #     print(entry.get("published", "нет даты"))
    #     print("---")
    try:
        response = requests.get(address, timeout=10)
        response.raise_for_status()
        feed = feedparser.parse(response.content)
        if feed.bozo:
            print("Ошибка:", feed.bozo_exception)
        else:
            print("Источник:", feed.feed.title)
            print("Новостей:", len(feed.entries))
    except Exception as e:
        print(e)
    
            