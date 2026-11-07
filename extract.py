import feedparser

addresses = ["https://lenta.ru/rss", "https://www.interfax.ru/rss.asp"]
for address in addresses:
    print(address)

    feed = feedparser.parse(address)

    # for entry in feed.entries:
    #     print(entry.title)
    #     print(entry.link)
    #     print(entry.get("published", "нет даты"))
    #     print("---")
    try:
        feed = feedparser.parse(address)
        if feed.bozo:
            print("Ошибка")
        else:
            print("Источник:", feed.feed.title)
            print("Новостей:", len(feed.entries))
    except Exception as e:
        print(e)
    
            