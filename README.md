# RSS 0.1
Python 3.5, Feedparser, Celery, Django, RabbitMQ
/rss celery -A tasks worker
/rss celery -A tasks beat
/rss/lenta_rss/lenta python manage.py runserver

