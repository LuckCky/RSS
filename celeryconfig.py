import datetime

CELERYBEAT_SCHEDULE = {
    'check rss every 15 min': {
        'task': 'tasks',
        'schedule': datetime.timedelta(minutes=1)
    }
}
