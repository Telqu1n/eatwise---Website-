from django.urls import path, include
from .import views
from .views import profile
from django.contrib.auth import views as auth_views

app_name = 'users'  

urlpatterns = [
  path('', views.UserLoginFormCreateView.as_view(), name='login-page'),
  path('register/', views.RegistrationCreateView.as_view(), name='registration-page'),
  path('profile/', profile, name='users-profile'),
  path('logout/', auth_views.LogoutView.as_view(), name='logout'),
]
