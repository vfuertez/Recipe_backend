from django.db import models

# Create your models here.
class Recipe(models.Model):
    name = models.CharField(max_length=250, blank=True)
    image = models.CharField(max_length=250, blank=True, null=True)
    ingredients = models.CharField(max_length=250, blank=True, null=True)
    recipe = models.CharField(max_length=250, blank=True, null=True)
    