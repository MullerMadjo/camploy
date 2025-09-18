from django import forms
from .models import Certification

class CertificationCreateForm(forms.ModelForm):
    class Meta:
        model = Certification
        exclude = ['cv', 'order']
