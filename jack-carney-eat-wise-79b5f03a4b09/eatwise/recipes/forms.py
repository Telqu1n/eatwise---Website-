from django import forms
from .models import Recipe
from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _


class RecipeForm(forms.ModelForm):
    class Meta:
        model = Recipe
        fields = ['title', 'description', 'ingredients', 'directions', 'image', 'category', 'rating']
        widgets = {
            'description': forms.Textarea(attrs={'rows': 4, 'cols': 40}),
            'ingredients': forms.Textarea(attrs={'rows': 4, 'cols': 40}),
            'directions': forms.Textarea(attrs={'rows': 4, 'cols': 40}),
        }

    def clean_rating(self):
        rating = self.cleaned_data.get('rating')
        if rating < 0 or rating > 5:
            raise ValidationError(_('Rating must be between 0 and 5.'))
        return rating
