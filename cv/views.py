
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import CV

@login_required
def delete_cv_view(request, cv_id):
    """Supprime le CV et toutes les données associées (cascade)."""
    try:
        cv = CV.objects.get(id=cv_id, user=request.user)
    except CV.DoesNotExist:
        messages.error(request, "CV introuvable.")
        return redirect('dashboard-cv-intelligent')
    if request.method == 'POST':
        cv.delete()
        messages.success(request, "CV supprimé avec succès.")
        return redirect('dashboard-cv-intelligent')
    # Redirige si accès direct GET
    return redirect('dashboard-cv-intelligent')


@login_required
def dashboard_cv_intelligent(request):
    """Dashboard CV intelligent multi-CV :
    - Liste tous les CV de l'utilisateur
    - Affiche bouton Ajouter un CV même si des CV existent
    - Affiche pour chaque CV : infos principales + boutons Compléter et Supprimer
    """
    user_cvs = CV.objects.filter(user=request.user)
    return render(request, 'dashboard-cv.html', {'user_cvs': user_cvs})
from django.contrib.auth.decorators import login_required

@login_required
def edit_certification_view(request, cert_id):
    """Vue pour modifier une certification"""
    from .forms_certification import CertificationCreateForm
    from .models import Certification
    try:
        certification = Certification.objects.get(id=cert_id, cv__user=request.user)
    except Certification.DoesNotExist:
        messages.error(request, "Certification introuvable.")
        return redirect('profile')
    if request.method == 'POST':
        if request.GET.get('delete') == '1':
            cv_id = certification.cv.id
            certification.delete()
            messages.success(request, "Certification supprimée avec succès !")
            return redirect('cv-dashboard', cv_id=cv_id)
        form = CertificationCreateForm(request.POST, instance=certification)
        if form.is_valid():
            form.save()
            messages.success(request, "Certification modifiée avec succès !")
            return redirect('cv-dashboard', cv_id=certification.cv.id)
    else:
        form = CertificationCreateForm(instance=certification)
    return render(request, 'edit-certification.html', {'form': form, 'return_url': f"/cv/dashboard/{certification.cv.id}/"})


@login_required
def edit_language_view(request, language_id):
    """Vue pour modifier une langue"""
    from .forms_language import LanguageCreateForm
    from .models import Language
    try:
        language = Language.objects.get(id=language_id, cv__user=request.user)
    except Language.DoesNotExist:
        messages.error(request, "Langue introuvable.")
        return redirect('profile')
    if request.method == 'POST':
        if request.GET.get('delete') == '1':
            cv_id = language.cv.id
            language.delete()
            messages.success(request, "Langue supprimée avec succès !")
            return redirect('cv-dashboard', cv_id=cv_id)
        form = LanguageCreateForm(request.POST, instance=language)
        if form.is_valid():
            form.save()
            messages.success(request, "Langue modifiée avec succès !")
            return redirect('cv-dashboard', cv_id=language.cv.id)
    else:
        form = LanguageCreateForm(instance=language)
    return render(request, 'edit-language.html', {'form': form, 'return_url': f"/cv/dashboard/{language.cv.id}/"})


@login_required
def edit_project_view(request, project_id):
    """Vue pour modifier un projet"""
    from .forms_project import ProjectCreateForm
    from .models import Project
    try:
        project = Project.objects.get(id=project_id, cv__user=request.user)
    except Project.DoesNotExist:
        messages.error(request, "Projet introuvable.")
        return redirect('profile')
    if request.method == 'POST':
        if request.GET.get('delete') == '1':
            cv_id = project.cv.id
            project.delete()
            messages.success(request, "Projet supprimé avec succès !")
            return redirect('cv-dashboard', cv_id=cv_id)
        form = ProjectCreateForm(request.POST, instance=project)
        if form.is_valid():
            form.save()
            messages.success(request, "Projet modifié avec succès !")
            return redirect('cv-dashboard', cv_id=project.cv.id)
    else:
        form = ProjectCreateForm(instance=project)
    return render(request, 'edit-project.html', {'form': form, 'return_url': f"/cv/dashboard/{project.cv.id}/"})


@login_required
def edit_skill_view(request, skill_id):
    """Vue pour modifier une compétence"""
    from .forms_skill import SkillCreateForm
    from .models import Skill
    try:
        skill = Skill.objects.get(id=skill_id, cv__user=request.user)
    except Skill.DoesNotExist:
        messages.error(request, "Compétence introuvable.")
        return redirect('profile')
    if request.method == 'POST':
        if request.GET.get('delete') == '1':
            cv_id = skill.cv.id
            skill.delete()
            messages.success(request, "Compétence supprimée avec succès !")
            return redirect('cv-dashboard', cv_id=cv_id)
        form = SkillCreateForm(request.POST, instance=skill)
        if form.is_valid():
            form.save()
            messages.success(request, "Compétence modifiée avec succès !")
            return redirect('cv-dashboard', cv_id=skill.cv.id)
    else:
        form = SkillCreateForm(instance=skill)
    return render(request, 'edit-skill.html', {'form': form, 'return_url': f"/cv/dashboard/{skill.cv.id}/"})


@login_required
def edit_education_view(request, edu_id):
    """Vue pour modifier une formation"""
    from .forms_education import EducationCreateForm
    from .models import Education
    try:
        education = Education.objects.get(id=edu_id, cv__user=request.user)
    except Education.DoesNotExist:
        messages.error(request, "Formation introuvable.")
        return redirect('profile')
    if request.method == 'POST':
        if request.GET.get('delete') == '1':
            cv_id = education.cv.id
            education.delete()
            messages.success(request, "Formation supprimée avec succès !")
            return redirect('cv-dashboard', cv_id=cv_id)
        form = EducationCreateForm(request.POST, instance=education)
        if form.is_valid():
            form.save()
            messages.success(request, "Formation modifiée avec succès !")
            return redirect('cv-dashboard', cv_id=education.cv.id)
    else:
        form = EducationCreateForm(instance=education)
    return render(request, 'edit-education.html', {'form': form, 'return_url': f"/cv/dashboard/{education.cv.id}/"})


@login_required
def edit_experience_view(request, exp_id):
    """Vue pour modifier une expérience professionnelle"""
    from .forms_experience import ExperienceCreateForm
    try:
        experience = Experience.objects.get(id=exp_id, cv__user=request.user)
    except Experience.DoesNotExist:
        messages.error(request, "Expérience introuvable.")
        return redirect('profile')
    if request.method == 'POST':
        if request.GET.get('delete') == '1':
            cv_id = experience.cv.id
            experience.delete()
            messages.success(request, "Expérience supprimée avec succès !")
            return redirect('cv-dashboard', cv_id=cv_id)
        form = ExperienceCreateForm(request.POST, instance=experience)
        if form.is_valid():
            form.save()
            messages.success(request, "Expérience modifiée avec succès !")
            return redirect('cv-dashboard', cv_id=experience.cv.id)
    else:
        form = ExperienceCreateForm(instance=experience)
    return render(request, 'edit-experience.html', {'form': form, 'return_url': f"/cv/dashboard/{experience.cv.id}/"})


@login_required
def cv_dashboard_view(request, cv_id):
    """Dashboard pour gérer toutes les sections d'un CV"""
    try:
        cv = CV.objects.get(id=cv_id, user=request.user)
    except CV.DoesNotExist:
        messages.error(request, "CV introuvable.")
        return redirect('profile')

    experiences = cv.experiences.all()
    educations = cv.educations.all()
    skills = cv.skills.all()
    projects = cv.projects.all()
    languages = cv.languages.all()
    certifications = cv.certifications.all()

    context = {
        'cv': cv,
        'experiences': experiences,
        'educations': educations,
        'skills': skills,
        'projects': projects,
        'languages': languages,
        'certifications': certifications,
    }
    return render(request, 'cv-dashboard.html', context)
from .forms_certification import CertificationCreateForm
from .models import Certification

@login_required
def add_certification_view(request, cv_id):
    """Vue pour ajouter une certification à un CV"""
    try:
        cv = CV.objects.get(id=cv_id, user=request.user)
    except CV.DoesNotExist:
        messages.error(request, "CV introuvable.")
        return redirect('profile')

    if request.method == 'POST':
        form = CertificationCreateForm(request.POST)
        if form.is_valid():
            certification = form.save(commit=False)
            certification.cv = cv
            certification.save()
            messages.success(request, "Certification ajoutée avec succès !")
            return redirect('cv-dashboard', cv_id=cv.id)
    else:
        form = CertificationCreateForm()

    return render(request, 'add-certification.html', {'form': form, 'return_url': f"/cv/dashboard/{cv.id}/"})
from .forms_language import LanguageCreateForm
from .models import Language

@login_required
def add_language_view(request, cv_id):
    """Vue pour ajouter une langue à un CV"""
    try:
        cv = CV.objects.get(id=cv_id, user=request.user)
    except CV.DoesNotExist:
        messages.error(request, "CV introuvable.")
        return redirect('profile')

    if request.method == 'POST':
        form = LanguageCreateForm(request.POST)
        if form.is_valid():
            language = form.save(commit=False)
            language.cv = cv
            language.save()
            messages.success(request, "Langue ajoutée avec succès !")
            return redirect('cv-dashboard', cv_id=cv.id)
    else:
        form = LanguageCreateForm()

    return render(request, 'add-language.html', {'form': form, 'return_url': f"/cv/dashboard/{cv.id}/"})
from .forms_project import ProjectCreateForm
from .models import Project

@login_required
def add_project_view(request, cv_id):
    """Vue pour ajouter un projet à un CV"""
    try:
        cv = CV.objects.get(id=cv_id, user=request.user)
    except CV.DoesNotExist:
        messages.error(request, "CV introuvable.")
        return redirect('profile')

    if request.method == 'POST':
        form = ProjectCreateForm(request.POST)
        if form.is_valid():
            project = form.save(commit=False)
            project.cv = cv
            project.save()
            messages.success(request, "Projet ajouté avec succès !")
            return redirect('cv-dashboard', cv_id=cv.id)
    else:
        form = ProjectCreateForm()

    return render(request, 'add-project.html', {'form': form, 'return_url': f"/cv/dashboard/{cv.id}/"})
from .forms_skill import SkillCreateForm
from .models import Skill

@login_required
def add_skill_view(request, cv_id):
    """Vue pour ajouter une compétence à un CV"""
    try:
        cv = CV.objects.get(id=cv_id, user=request.user)
    except CV.DoesNotExist:
        messages.error(request, "CV introuvable.")
        return redirect('profile')

    if request.method == 'POST':
        form = SkillCreateForm(request.POST)
        if form.is_valid():
            skill = form.save(commit=False)
            skill.cv = cv
            skill.save()
            messages.success(request, "Compétence ajoutée avec succès !")
            return redirect('cv-dashboard', cv_id=cv.id)
    else:
        form = SkillCreateForm()

    return render(request, 'add-skill.html', {'form': form, 'return_url': f"/cv/dashboard/{cv.id}/"})
from .forms_education import EducationCreateForm
from .models import Education

@login_required
def add_education_view(request, cv_id):
    """Vue pour ajouter une formation à un CV"""
    try:
        cv = CV.objects.get(id=cv_id, user=request.user)
    except CV.DoesNotExist:
        messages.error(request, "CV introuvable.")
        return redirect('profile')

    if request.method == 'POST':
        form = EducationCreateForm(request.POST)
        if form.is_valid():
            education = form.save(commit=False)
            education.cv = cv
            education.save()
            messages.success(request, "Formation ajoutée avec succès !")
            return redirect('cv-dashboard', cv_id=cv.id)
    else:
        form = EducationCreateForm()

    return render(request, 'add-education.html', {'form': form, 'return_url': f"/cv/dashboard/{cv.id}/"})
from .forms_experience import ExperienceCreateForm
from .models import Experience

@login_required
def add_experience_view(request, cv_id):
    """Vue pour ajouter une expérience à un CV"""
    try:
        cv = CV.objects.get(id=cv_id, user=request.user)
    except CV.DoesNotExist:
        messages.error(request, "CV introuvable.")
        return redirect('profile')

    if request.method == 'POST':
        form = ExperienceCreateForm(request.POST)
        if form.is_valid():
            experience = form.save(commit=False)
            experience.cv = cv
            experience.save()
            messages.success(request, "Expérience ajoutée avec succès !")
            return redirect('cv-dashboard', cv_id=cv.id)
    else:
        form = ExperienceCreateForm()

    return render(request, 'add-experience.html', {'form': form, 'return_url': f"/cv/dashboard/{cv.id}/"})

from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages

from .forms import CVForm
from .models import CV

@login_required
def add_cv_view(request):
    """Vue pour ajouter un CV (champs principaux uniquement)"""
    if request.method == 'POST':
        cv_form = CVForm(request.POST)
        if cv_form.is_valid():
            cv = cv_form.save(commit=False)
            cv.user = request.user
            cv.save()
            messages.success(request, 'CV ajouté avec succès !')
            return redirect('dashboard-cv-intelligent')
    else:
        cv_form = CVForm()
    return render(request, 'add-cv.html', {'cv_form': cv_form})


@login_required
def edit_cv_view(request, cv_id=None):
    """Vue pour modifier un CV"""
    from .forms import CVForm
    from .models import CV
    cv = None
    if cv_id:
        try:
            cv = CV.objects.get(id=cv_id, user=request.user)
        except CV.DoesNotExist:
            messages.error(request, "CV introuvable.")
            return redirect('dashboard-cv-intelligent')
    if request.method == 'POST':
        form = CVForm(request.POST, instance=cv)
        if form.is_valid():
            form.save()
            messages.success(request, 'CV modifié avec succès !')
            return redirect('dashboard-cv-intelligent')
    else:
        form = CVForm(instance=cv)
    return render(request, 'edit-cv.html', {'form': form, 'cv': cv})