--количество новостей от каждого источника
select source, count(*) as news_count
from news group by source
order by news_count desc;

--5 свежих новостей
select source, published, left(title,40) as short_title
from news
order by published desc
limit 5;

-- новости по часам
select date_trunc('hour', published) as hour, count(*) as news_count
from news
group by hour
order by hour asc;