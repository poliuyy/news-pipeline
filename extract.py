import feedparser

feed = feedparser.parse("https://lenta.ru/rss")

print("Источник:", feed.feed.title)
print("Новостей:", len(feed.entries))

for entry in feed.entries:
    print(entry.title)
    print(entry.link)
    print(entry.get("published", "нет даты"))
    print("---")