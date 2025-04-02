from django.urls import path, include
from .import views

app_name = 'products'  

urlpatterns = [
  path('', views.ProductPageView.as_view(), name='product-page'),
]