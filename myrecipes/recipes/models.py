# -*- coding: utf-8 -*-

from django.db import models
from django.contrib.auth.models import User


class DishType(models.Model):
    # Starter, main, dessert, etc.
    description = models.CharField(max_length=50)

    def __str__(self):
        return self.description

    class Meta:
        """
        Modifica el nombre de la clase que se mostrara en el admin
        """
        verbose_name = 'Tipo de plato'
        verbose_name_plural = 'Tipos de platos'


class FoodType(models.Model):
    # vegetarian, gluten free, etc.
    description = models.CharField(max_length=50)

    def __str__(self):
        return self.description


class Difficult(models.Model):
    description = models.CharField(max_length=50)

    def __str__(self):
        return self.description


class Thematic(models.Model):
    # spanish, mexican, chinese, tc.
    description = models.CharField(max_length=50)

    def __str__(self):
        return self.description


class PublicTarget(models.Model):
    # children, birthday, professional events, etc.
    description = models.CharField(max_length=50)

    def __str__(self):
        return self.description


class IngredientAlternative(models.Model):
    description = models.CharField(max_length=50)

    def __str__(self):
        return self.description


class Ingredient(models.Model):
    description = models.CharField(max_length=50)
    ingredient_alternative = models.ManyToManyField(IngredientAlternative, blank=True)

    def __str__(self):
        return self.description


class Recipe(models.Model):
    # fieldsets = (
    #     (None, {
    #         'fields': ('title', 'foo')
    #     }),
    #     ('Avanzadas', {
    #         'classes': ('collapse',),
    #         'fields': ('reuse',)
    #     })
    # )
    title = models.CharField(max_length=50, unique=True)
    slug = models.SlugField()
    short_description = models.CharField(max_length=140, verbose_name='Descripción breve')
    dish_type = models.ForeignKey(DishType, on_delete=models.CASCADE, default=1)
    food_type = models.ManyToManyField(FoodType)
    difficult = models.ForeignKey(Difficult, default=1, on_delete=models.CASCADE)
    directions_time = models.PositiveSmallIntegerField(verbose_name='Tiempo de preparación')
    price = models.DecimalField(max_digits=6, decimal_places=2, verbose_name='Precio (€)')
    person_number = models.PositiveSmallIntegerField(verbose_name='Comensales', default=1)
    thematic = models.ForeignKey(Thematic, on_delete=models.CASCADE, default=1)
    public_target = models.ForeignKey(PublicTarget, on_delete=models.CASCADE, default=1)
    ingredients = models.ManyToManyField(Ingredient)
    directions = models.TextField()
    calories = models.PositiveSmallIntegerField(blank=True, null=True)
    nutritional_value = models.PositiveSmallIntegerField(blank=True, null=True)
    conservation = models.CharField(max_length=140, blank=True, null=True)
    # FIXME Este campo podria ser un textfield
    # o mejor un enlace a otra receta existente
    reuse = models.ForeignKey('self', blank=True, null=True, on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True, editable=False)
    last_updated = models.DateTimeField(auto_now=True, editable=False)
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
