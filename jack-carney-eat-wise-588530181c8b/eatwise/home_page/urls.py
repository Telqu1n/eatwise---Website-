from django.urls import path, include
from .import views

app_name = 'home_page'  

urlpatterns = [
    path('', views.HomePageView.as_view(), name='home'),
]