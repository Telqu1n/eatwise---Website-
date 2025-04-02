from django.shortcuts import render
from django.views.generic import TemplateView
# Create your views here.

class ProductPageView(TemplateView):
    template_name = 'products/products.html'
    