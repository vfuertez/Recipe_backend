from django.db import models

# Create your models here.
class Recipe(models.Model):
    name = models.CharField(max_length=250)
    image = models.CharField(max_length=250, blank=True, null=True)
    ingredients = models.TextField(max_length=1000, blank=True, null=True)
    recipe = models.TextField(max_length=1000, blank=True, null=True)
    