import tasks
from lenta_rss.lenta.lrss.models import News

result = tasks.feeds.delay('https://lenta.ru/rss')
c = result.get(timeout=5)
for x in range(0, len(c['entries'])):
    #проверить есть ли c['entries'][x]['title'] в БД, если нет, то записать
    try:
        News.objects.get(name=c['entries'][x]['title'])
        pass
    except News.DoesNotExist:
        #add entry to DB
        print(x)

    # print('link:', c['entries'][x]['link'])
    # print('title:', c['entries'][x]['title'])
    # print('date:', c['entries'][x]['published'])
    # print('tags:', c['entries'][x]['tags'][0]['term'])
    # print('-'*20)
