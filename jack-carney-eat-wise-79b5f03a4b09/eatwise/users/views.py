from django.shortcuts import render
from .forms import UserRegisterForm, UserLoginForm
from django.contrib.auth import login, logout
from django.views.generic.edit import CreateView
from django.contrib.auth.views import LoginView
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.urls import reverse_lazy
from django.contrib.auth.decorators import login_required

# Create your views here.

class RegistrationCreateView(CreateView):
    form_class = UserRegisterForm
    template_name = 'users/register.html'
    success_url = '/'
    
    def form_valid(self, form):
      response = super().form_valid(form)
      user = self.object
      login(self.request, user)
      return response
    
    
class UserLoginFormCreateView(LoginView):  
    form_class = UserLoginForm  
    template_name = 'users/login.html'  
    redirect_authenticated_user = True
    success_url = reverse_lazy('home_page:home')
    
    def get_success_url(self):
        return self.request.GET.get('next') or reverse_lazy('home_page:home')


@login_required
def profile(request):
    return render(request, 'users/profile.html')

