from celery import Celery
import feedparser
import django
django.setup()

app = Celery('rss', broker='amqp://guest@localhost//')
app.conf.CELERY_RESULT_BACKEND = 'db+sqlite:///results.sqlite3'

@app.task
def feeds(x):
    feed = feedparser.parse(x)
    # feed = str(feed).encode('utf8')
    return feed
