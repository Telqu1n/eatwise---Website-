from django import forms
from .models import ContactUsModel


class ContactUsForm(forms.ModelForm):
    class Meta:
        model = ContactUsModel
        fields = ['FirstName','LastName', 'Email', 'Feedback']
        labels = {
            'FirstName': 'Full name',
            'LastName': 'Last name',
            'Email': 'Email address',
            'Feedback': 'Feedback',
        }