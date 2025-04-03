from django.db import models

# Create your models here.

class ContactUsModel(models.Model):
    FirstName = models.CharField(max_length=100)
    LastName = models.CharField(max_length=100)
    Email = models.EmailField(max_length=100)
    Feedback = models.TextField(max_length=1000)
