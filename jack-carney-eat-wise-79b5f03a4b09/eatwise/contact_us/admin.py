from django.contrib import admin
from .models import ContactUsModel

# Register your models here.

class AdminContactUs(admin.ModelAdmin):
    list_display = ('FirstName', 'LastName', 'Email')
    

admin.site.register(ContactUsModel, AdminContactUs)