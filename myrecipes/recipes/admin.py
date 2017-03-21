from django.contrib import admin
from django.db.models.signals import pre_save
from django.dispatch import receiver
from django.utils.text import slugify

from .models import Recipe, Difficult, Thematic, Ingredient, DishType, FoodType, PublicTarget


@receiver(pre_save, sender=Recipe)
def genera_slug(sender, instance, using, **kwargs):
    if not instance.slug:
        instance.slug = slugify(instance.title)


class RecipeAdmin(admin.ModelAdmin):
    exclude = ('slug', 'author')


# class DishTypeAdmin(admin.ModelAdmin):
#     verbose_name = 'Tipo de plato'
#     verbose_name_plural = 'Tipos de platos'


admin.site.register(Recipe, RecipeAdmin)
admin.site.register(Difficult)
admin.site.register(Thematic)
admin.site.register(Ingredient)
admin.site.register(DishType)
admin.site.register(FoodType)
admin.site.register(PublicTarget)
