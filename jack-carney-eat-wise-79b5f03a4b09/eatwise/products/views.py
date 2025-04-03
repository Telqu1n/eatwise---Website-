from django.shortcuts import render
from django.views.generic import TemplateView
from .models import Products
from django.shortcuts import get_object_or_404
# Create your views here.

class ProductPageView(TemplateView):
    template_name = 'products/products.html'
     
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        
        # Fetch the 10 latest products
        context['products'] = Products.objects.order_by('-date_created')[:10]

        # Fetch products with a rating greater than 4.7
        context['best_sellers'] = Products.objects.filter(rating__gte=4.7).order_by('-rating')[:10]

        return context
    
    
class ProductDetailView(TemplateView):
    template_name = 'products/product_detail.html'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        slug = self.kwargs.get('slug')  # Get slug from URL
        product = get_object_or_404(Products, slug=slug)
        context['product'] = product
        
        return context