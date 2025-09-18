from django import forms
from .models import Skill

class SkillCreateForm(forms.ModelForm):
    class Meta:
        model = Skill
        exclude = ['cv', 'order']
