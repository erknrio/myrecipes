# -*- coding: utf-8 -*-

from django.db import models
from django.contrib.auth.models import User


class Difficult(models.Model):
    description = models.CharField(max_length=50)

    def __str__(self):
        return self.description


class Thematic(models.Model):
    # spanish, mexican, chinese, tc.
    description = models.CharField(max_length=50)

    def __str__(self):
        return self.description


class Ingredient(models.Model):
    description = models.CharField(max_length=50)

    def __str__(self):
        return self.description


class IngredientAlternative(models.Model):
    ingredient = models.ForeignKey(Ingredient, on_delete=models.CASCADE)
    description = models.CharField(max_length=50)

    def __str__(self):
        return self.description


class Recipe(models.Model):
    fieldsets = (
        (None, {
            'fields': ('title', 'foo')
        }),
        ('Avanzadas', {
            'classes': ('collapse',),
            'fields': ('reuse',)
        })
    )
    title = models.CharField(max_length=50, unique=True)
    slug = models.SlugField()
    short_description = models.CharField(max_length=140, verbose_name='Descripción breve')
    difficult = models.OneToOneField(Difficult, on_delete=models.CASCADE)
    directions_time = models.PositiveSmallIntegerField(verbose_name='Tiempo de preparación')
    price = models.PositiveSmallIntegerField(verbose_name='Precio (€)')
    person_number = models.PositiveSmallIntegerField(verbose_name='Comensales', default=1)
    calories = models.PositiveSmallIntegerField(blank=True, null=True)
    thematic = models.OneToOneField(Thematic, on_delete=models.CASCADE)
    ingredients = models.ManyToManyField(Ingredient)
    directions = models.TextField()
    nutritional_value = models.PositiveSmallIntegerField(blank=True, null=True)
    conservation = models.CharField(max_length=140, blank=True, null=True)
    # FIXME Este campo podria ser un textfield
    # o mejor un enlace a otra receta existente
    reuse = models.ForeignKey('self', blank=True, null=True, on_delete=models.CASCADE)
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


class DishType(models.Model):
    recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE)
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
    recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE)
    # vegetarian, gluten free, etc.
    description = models.CharField(max_length=50)

    def __str__(self):
        return self.description


class PublicTarget(models.Model):
    recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE)
    # children, birthday, professional events, etc.
    description = models.CharField(max_length=50)

    def __str__(self):
        return self.description
