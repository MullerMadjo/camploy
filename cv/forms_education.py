from django import forms
from .models import Education

class EducationCreateForm(forms.ModelForm):
    class Meta:
        model = Education
        exclude = ['cv', 'order']
