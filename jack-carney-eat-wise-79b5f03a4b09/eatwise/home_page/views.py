from django.shortcuts import render
from django.views.generic import TemplateView
from products.models import Products
from recipes.models import Recipe
# Create your views here.

class HomePageView(TemplateView):
    template_name = 'home_page/index.html'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['products'] = Products.objects.order_by('-date_created')[:10]
        context['best_sellers'] = Products.objects.filter(rating__gte=4.7).order_by('-rating')[:10]
        context['recipe'] = Recipe.objects.all()
        context['best_sellers_recipe'] = Recipe.objects.filter(rating__gte=4.7).order_by('-rating')[:10]

        return context

  
  