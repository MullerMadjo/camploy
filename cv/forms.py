from django import forms
from .models import CV, PersonalInfo, Experience, Education, Skill, Project, Language, Certification

class CVForm(forms.ModelForm):
    class Meta:
        model = CV
        fields = ['title', 'description', 'github', 'linkedin']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'description': forms.Textarea(attrs={'class': 'form-control', 'rows': 4}),
            'github': forms.URLInput(attrs={'class': 'form-control'}),
            'linkedin': forms.URLInput(attrs={'class': 'form-control'}),
        }

class PersonalInfoForm(forms.ModelForm):
    class Meta:
        model = PersonalInfo
        exclude = ['cv']

class ExperienceForm(forms.ModelForm):
    class Meta:
        model = Experience
        exclude = ['cv']

class EducationForm(forms.ModelForm):
    class Meta:
        model = Education
        exclude = ['cv']

class SkillForm(forms.ModelForm):
    class Meta:
        model = Skill
        exclude = ['cv']

class ProjectForm(forms.ModelForm):
    class Meta:
        model = Project
        exclude = ['cv']

class LanguageForm(forms.ModelForm):
    class Meta:
        model = Language
        exclude = ['cv']

class CertificationForm(forms.ModelForm):
    class Meta:
        model = Certification
        exclude = ['cv']
