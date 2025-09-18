from django import forms
from .models import Experience

class ExperienceCreateForm(forms.ModelForm):
    class Meta:
        model = Experience
        exclude = ['cv', 'order']
