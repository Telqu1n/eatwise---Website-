from django.urls import path, include
from .import views

app_name = 'recipes'  

urlpatterns = [
  # path('', views.HomePageView.as_view(), name='home-page'),
  path('', views.RecipePageView.as_view(), name='recipe-page'),
]

