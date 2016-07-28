from django.db import models

class News(models.Model):
    date = models.DateField()
    name = models.TextField()
    brief = models.TextField()
    rubric = models.TextField()

    def __unicode__(self):
        return self.name
