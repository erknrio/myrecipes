from django.db import models
from django.utils import timezone


class Recipes(models.Model):
    title = models.CharField(max_length=50)
    short_description = models.CharField(max_length=140)
    # datetime_created = models.DateTimeField(default=timezone.now())
    datetime_created = models.DateTimeField(auto_now_add=True)
    datetime_modificated = models.DateTimeField(auto_now=True)
    publish = models.BooleanField(default=False)

    def __str__(self):
        return self.title
