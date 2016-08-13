from django.db import models

class News(models.Model):

    date = models.DateField('date published')
    title = models.CharField(max_length=200)
    brief = models.TextField()
    rubric = models.TextField()
    link = models.TextField()

    def __str__(self):
        return self.title
