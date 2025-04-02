from django.shortcuts import render
from django.views.generic import TemplateView
from django.views.generic.edit import CreateView
from .models import ContactUsModel
from .forms import ContactUsForm

# Create your views here.

class ContactUsModelCreateView(CreateView):
    template_name = 'contact_us/index.html'
    form_class = ContactUsForm
    model = ContactUsModel
    success_url = 'success'
    
    
class ContactUsModelSuccessView(TemplateView):
    template_name = 'contact_us/success.html'
    
    # def get_context_data(self, **kwargs):
    #     context = super().get_context_data(**kwargs)
    #     context['message'] = 'Thank you for your feedback!'
    #     return context