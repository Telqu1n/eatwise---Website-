from django.shortcuts import render
from django.views.generic import TemplateView
# Create your views here.

class RecipePageView(TemplateView):
    template_name = 'recipes/recipes.html'
    