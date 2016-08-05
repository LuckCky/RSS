import tasks
from lenta_rss.lenta.lrss.models import News
import datetime

result = tasks.feeds.delay('https://lenta.ru/rss')
c = result.get(timeout=5)
for x in range(0, len(c['entries'])):
    try:
        rubric = c['entries'][x]['tags'][0]['term']
    except KeyError:
        rubric = ' '
    try:
        News.objects.get(name=c['entries'][x]['title'])
        pass
    except News.DoesNotExist:
        date = c['entries'][x]['published'].split(',')
        date = date[1].split(' ')
        day = int(date[1])
        months = {'Jan': 1,
                  'Feb': 2,
                  'Mar': 3,
                  'Apr': 4,
                  'May': 5,
                  'Jun': 6,
                  'Jul': 7,
                  'Aug': 8,
                  'Sep': 9,
                  'Oct': 10,
                  'Nov': 11,
                  'Dec': 12}
        month = int(months[date[2]])
        year = int(date[3])
        date = datetime.date(year, month, day)
        n = News(link=c['entries'][x]['link'],
                 name=c['entries'][x]['title'],
                 date=date,
                 rubric=rubric,
                 brief=c['entries'][x]['summary'])
        n.save()
