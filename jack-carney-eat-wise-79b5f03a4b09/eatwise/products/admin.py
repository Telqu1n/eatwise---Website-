from django.contrib import admin
from .models import Products
# Register your models here.

class AdminProduct(admin.ModelAdmin):
    list_display = ['name', 'price', 'category']
    search_fields = ['name', 'category']
    list_filter = ['category']
    list_per_page = 10
    
admin.site.register(Products, AdminProduct)
