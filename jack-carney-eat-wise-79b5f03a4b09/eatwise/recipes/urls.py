from django.urls import path
from . import views

app_name = 'recipes'

urlpatterns = [
    path('', views.RecipePageView.as_view(), name='recipe-page'),
    path('upload/', views.RecipeUploadView.as_view(), name='upload-recipe'),  # This comes first
    path('<slug:slug>/', views.RecipeDetailView.as_view(), name='recipe-detail'),
]