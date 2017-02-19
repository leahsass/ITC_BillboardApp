from django.db import models
from django.utils import timezone


# Create your models here.
class Post(models.Model):
    published_date = models.DateTimeField(blank=True, null=True)
    title = models.CharField(max_length=500)
    text = models.TextField()
    author = models.CharField(max_length=500)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title