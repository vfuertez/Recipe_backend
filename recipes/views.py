from django.shortcuts import render

# Create your views here.
from .models import Recipe
from rest_framework import viewsets
from rest_framework import permissions
from .serializers import RecipeSerializer

class RecipeViewset(viewsets.ModelViewSet):
    queryset = Recipe.objects.all()
    serializer_class = RecipeSerializer
    permission_classes = [permissions.AllowAny]