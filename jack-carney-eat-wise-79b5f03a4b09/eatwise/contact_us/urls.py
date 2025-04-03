from django.urls import path
from .import views

app_name = 'contact_us'  

urlpatterns = [
  path('', views.ContactUsModelCreateView.as_view(), name='contact-us'),
  path('success/', views.ContactUsModelSuccessView.as_view(), name='success'),
]