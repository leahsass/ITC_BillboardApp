from django.db import models
from django.utils import timezone


# Create your models here.
class Post(models.Model):
    published_date = models.DateTimeField()
    title = models.CharField(max_length=500)
    text = models.TextField()
    author = models.CharField(max_length=500)


    def __str__(self):
        return self.title+" by "+self.author