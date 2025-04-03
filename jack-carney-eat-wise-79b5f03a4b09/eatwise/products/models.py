from django.db import models
import datetime
from django.utils.text import slugify
# Create your models here.

#product model 
class Products(models.Model):
    name = models.CharField(max_length=100)
    price = models.FloatField()
    description = models.TextField()
    image = models.ImageField(upload_to='product_images')
    category = models.CharField(max_length=100)
    rating = models.FloatField(default=0.0)  # New field for ratings
    date_created = models.DateTimeField(auto_now_add=True)
    slug = models.SlugField(unique=True, blank=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)
    
    
    def __str__(self):
        return self.name
#product model

