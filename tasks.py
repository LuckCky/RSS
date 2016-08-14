from celery import Celery
import datetime
import feedparser
import django
import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "lenta_rss.lenta.lenta.settings")
django.setup()
from lenta_rss.lenta.lrss.models import News
from celery.decorators import periodic_task

app = Celery('rss', broker='amqp://guest@localhost//')
app.conf.CELERY_RESULT_BACKEND = 'db+sqlite:///results.sqlite3'

@app.task
def feeds(x):
    feed = feedparser.parse(x)
    return feed

@periodic_task(run_every=datetime.timedelta(minutes=15))
def start():
    c = feeds('https://lenta.ru/rss')
    for x in range(0, len(c['entries'])):
        try:
            rubric = c['entries'][x]['tags'][0]['term']
        except KeyError:
            rubric = ' '
        try:
            News.objects.get(title=c['entries'][x]['title'])
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
                     title=c['entries'][x]['title'],
                     date=date,
                     rubric=rubric,
                     brief=c['entries'][x]['summary'])
            n.save()

if __name__ == "__main__":
    start()
