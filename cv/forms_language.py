from django import forms
from .models import Language

class LanguageCreateForm(forms.ModelForm):
    class Meta:
        model = Language
        exclude = ['cv', 'order']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Ajoute la classe 'form-control' au champ select 'level'
        if 'level' in self.fields:
            self.fields['level'].widget.attrs['class'] = 'form-control'
