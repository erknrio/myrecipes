from django.contrib import admin
from django.db.models.signals import pre_save
from django.dispatch import receiver
from django.utils.text import slugify

from .models import DishType, FoodType, Difficult, Thematic, PublicTarget,\
    IngredientAlternative, Ingredient, Recipe


@receiver(pre_save, sender=Recipe)
def genera_slug(sender, instance, using, **kwargs):
    if not instance.slug:
        instance.slug = slugify(instance.title)


class RecipeAdmin(admin.ModelAdmin):
    exclude = ('slug',)


admin.site.register(DishType)
admin.site.register(FoodType)
admin.site.register(Difficult)
admin.site.register(Thematic)
admin.site.register(PublicTarget)
admin.site.register(IngredientAlternative)
admin.site.register(Ingredient)
admin.site.register(Recipe, RecipeAdmin)
