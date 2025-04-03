from django.shortcuts import render
from django.views.generic import TemplateView
from .models import Recipe
from django.shortcuts import get_object_or_404
from .forms import RecipeForm
from django.views.generic.edit import CreateView
from django.urls import reverse

# Create your views here.

# views.py
class RecipePageView(TemplateView):
    template_name = 'recipes/recipes.html'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['recipes'] = Recipe.objects.all()
        context['best_sellers'] = Recipe.objects.filter(rating__gte=4.7).order_by('-rating')[:10]
        return context
    
class RecipeDetailView(TemplateView):
    template_name = 'recipes/recipe_detail.html'
    
from django.views.generic import TemplateView
from .models import Recipe
from django.shortcuts import get_object_or_404


class RecipeDetailView(TemplateView):
    template_name = 'recipes/recipe_detail.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        slug = self.kwargs.get('slug')  # Get slug from URL
        recipe = get_object_or_404(Recipe, slug=slug)
        context['recipe'] = recipe
        
        return context




class RecipeUploadView(CreateView):
    model = Recipe
    form_class = RecipeForm
    template_name = 'recipes/recipe_upload.html'
    
    def form_valid(self, form):
        # Assign the current user if needed
        if self.request.user.is_authenticated:
            form.instance.user = self.request.user
        return super().form_valid(form)
    
    def get_success_url(self):
        # Redirect to the newly created recipe's detail page
        return reverse('recipes:recipe-detail', kwargs={'slug': self.object.slug})
    