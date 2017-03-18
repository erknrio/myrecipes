from django.db import models


class Recipes(models.Model):
    name = models.CharField(max_length=50)
    short_description = models.CharField(max_length=140)

    def __str__(self):
        return self.name
