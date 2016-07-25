from celery import Celery

app = Celery('rss', broker='amqp://guest@localhost//')
app.conf.CELERY_RESULT_BACKEND = 'db+sqlite:///results.sqlite'

@app.task
def feeds(x):
    import feedparser
    feed = feedparser.parse(x)
    return feed.feed.title

@app.task
def add(x, y):
    return x + y