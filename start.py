import tasks
from lenta_rss.lenta.lrss.models import News

result = tasks.feeds.delay('https://lenta.ru/rss')
c = result.get(timeout=5)
# for x in range(0, len(c['entries'])):
#     try:
#         News.objects.get(name=c['entries'][x]['title'])
#         pass
#     except News.DoesNotExist:
#         n = News(link=c['entries'][x]['link'],
#                  name=c['entries'][x]['title'],
#                  date=c['entries'][x]['published'],
#                  rubric=c['entries'][x]['tags'][0]['term'],
#                  brief=c['entries'][x]['summary'])
#         n.save()


for x in range(0, len(c['entries'])):
#     print('link:', c['entries'][x]['link'])
#     print('title:', c['entries'][x]['title'])
    print('date:', c['entries'][x]['published'])
#     print('tags:', c['entries'][x]['tags'][0]['term'])
#     print('brief:', c['entries'][x]['summary'])
#     print('-'*20)
# print(c['entries'])