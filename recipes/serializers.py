from .models import Recipe
from rest_framework import serializers

class RecipeSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        
        model = Recipe
        
        fields = ['id','name', 'image', 'ingredients', 'recipe' ]