import feedparser

addresses = ["https://lenta.ru/rss", "https://tass.ru/rss/v2.xml", "https://www.interfax.ru/rss.asp"]
for address in addresses:
    print(address)

    feed = feedparser.parse(address)


    print("Источник:", feed.feed.title)
    print("Новостей:", len(feed.entries))

    for entry in feed.entries:
        print(entry.title)
        print(entry.link)
        print(entry.get("published", "нет даты"))
        print("---")