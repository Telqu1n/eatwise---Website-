from django.db import models
from django.utils.text import slugify

class Recipe(models.Model):
    CATEGORY_CHOICES = [
        ('vegetarian', 'Vegetarian'),
        ('vegan', 'Vegan'),
        ('gluten-free', 'Gluten-Free'),
        ('keto', 'Keto'),
        ('dairy-free', 'Dairy-Free'),
    ]
    
    title = models.CharField(max_length=100)
    description = models.TextField()
    ingredients = models.TextField()
    directions = models.TextField()
    image = models.ImageField(upload_to='recipe_images')
    categories = models.JSONField(default=list)  # Works with SQLite
    rating = models.FloatField(default=0.0)
    date_created = models.DateTimeField(auto_now_add=True)
    slug = models.SlugField(unique=True, blank=True)
    
    def save(self, *args, **kwargs):
        if not self.slug:
            base_slug = slugify(self.title).lower()
            unique_slug = base_slug
            counter = 1
            
            while Recipe.objects.filter(slug=unique_slug).exists():
                unique_slug = f"{base_slug}-{counter}"
                counter += 1
                
            self.slug = unique_slug
        
        # Ensure categories are lowercase and unique
        self.categories = list(set(cat.lower() for cat in self.categories))
        super().save(*args, **kwargs)
    
    def __str__(self):
        return self.title