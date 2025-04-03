from django.contrib import admin
from .models import Recipe

# Register your models here.

@admin.register(Recipe)
class RecipesAdmin(admin.ModelAdmin):
    list_display = ('title', 'category', 'rating', 'date_created')
    
    
    