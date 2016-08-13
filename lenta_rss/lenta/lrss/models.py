from django.db import models

class News(models.Model):
    def __unicode__(self):
        return self.name

    date = models.DateField()
    name = models.TextField()
    brief = models.TextField()
    rubric = models.TextField()
    link = models.TextField()
