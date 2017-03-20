from django.db import models
from django.contrib.auth.models import User


class Recipe(models.Model):
    title = models.CharField(max_length=50, unique=True)
    slug = models.SlugField()
    short_description = models.CharField(max_length=140)
    difficult = models.OneToOneField(Difficult, on_delete=models.CASCADE)
    directions_time = models.PositiveSmallIntegerField()
    price = models.PositiveSmallIntegerField()
    person_number = models.PositiveSmallIntegerField()
    calories = models.PositiveSmallIntegerField()
    thematic = models.OneToOneField(Thematic, on_delete=models.CASCADE)
    ingredient = models.ManyToManyField(Ingredient)
    directions = models.TextField()
    nutricional_value = models.PositiveSmallIntegerField()
    conservation = models.CharField(max_length=140)
    # FIXME Este campo podria ser un textfield
    # o mejor un enlace a otra receta existente
    reuse = models.ForeignKey('self', on_delete=models.CASCADE)
    datetime_created = models.DateTimeField(auto_now_add=True)
    datetime_modificated = models.DateTimeField(auto_now=True)
    author = models.ForeignKey(User)
    publish = models.BooleanField(default=False)

    def __str__(self):
        return self.title

# FIXME Crear meta para que siempre ordene por
# datetime_modificated, tanto en admin como front
# class RecipeX(Recipe):
#
#     @staticmethod
#     def foo():
#         print("hi")


class Difficult(models.Model):
    description = models.CharField(max_length=50)


class DishType(models.Model):
    recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE)
    # Starter, main, dessert, etc.
    description = models.CharField(max_length=50)


class FoodType(models.Model):
    recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE)
    # vegetarian, gluten free, etc.
    description = models.CharField(max_length=50)


class Thematic(models.Model):
    # spanish, mexican, chinese, tc.
    description = models.CharField(max_length=50)


class PublicTarget(models.Model):
    recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE)
    # children, birthday, professional events, etc.
    description = models.CharField(max_length=50)


class Ingredient(models.Model):
    description = models.CharField(max_length=50)


class IngredientAlternative(models.Model):
    ingredient = models.ForeignKey(Ingredient, on_delete=models.CASCADE)
    description = models.CharField(max_length=50)


class Comments(models.Model):
    user = models.ForeignKey(User)
