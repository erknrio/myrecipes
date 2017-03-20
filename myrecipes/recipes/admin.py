from django.contrib.admin import admin
from django.db.models.signals import pre_save
from django.dispatch import receiver
from django.utils.text import slugify

from .models import Recipe


@receiver(pre_save, sender=Recipe)
def genera_slug(sender, instance, using, **kwargs):
    if not instance.slug:
        instance.slug = slugify(instance.title)


admin.site.register(Recipe)
