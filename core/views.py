from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.shortcuts import redirect
from django.contrib.auth import get_user_model

User = get_user_model()


def home(request):
    """Vue pour la page d'accueil"""
    return render(request, 'index.html')


def login_view(request):
    """Vue pour la page de connexion"""
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        if username and password:
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                messages.success(request, 'Connexion réussie !')
                return redirect('home')
            else:
                messages.error(request, 'Nom d\'utilisateur ou mot de passe incorrect.')
        else:
            messages.error(request, 'Veuillez remplir tous les champs.')
    
    return render(request, 'login.html')


def register_view(request):
    """Vue pour la page d'inscription"""
    if request.method == 'POST':
        # Récupération des données du formulaire
        username = request.POST.get('username')
        email = request.POST.get('email')
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        gender = request.POST.get('gender')
        birth_date = request.POST.get('birth_date')
        city = request.POST.get('city')
        phone = request.POST.get('phone')
        password = request.POST.get('password')
        confirm_password = request.POST.get('confirm_password')
        
        # Validation des mots de passe
        if password != confirm_password:
            messages.error(request, 'Les mots de passe ne correspondent pas.')
            return render(request, 'register.html')
        
        # Validation de l'unicité du nom d'utilisateur
        if User.objects.filter(username=username).exists():
            messages.error(request, 'Ce nom d\'utilisateur existe déjà.')
            return render(request, 'register.html')
        
        # Validation de l'unicité de l'email
        if User.objects.filter(email=email).exists():
            messages.error(request, 'Cette adresse email est déjà utilisée.')
            return render(request, 'register.html')
        
        # Validation des champs obligatoires
        if not all([username, email, first_name, last_name, city, password]):
            messages.error(request, 'Veuillez remplir tous les champs obligatoires.')
            return render(request, 'register.html')
        
        try:
            # Création de l'utilisateur avec tous les champs
            user = User.objects.create_user(
                username=username,
                email=email,
                first_name=first_name,
                last_name=last_name,
                password=password
            )
            
            # Ajout des champs optionnels
            if gender:
                user.gender = gender
            if birth_date:
                user.birth_date = birth_date
            if city:
                user.city = city
            if phone:
                user.phone = phone
            
            user.save()
            
            messages.success(request, 'Compte créé avec succès ! Vous pouvez maintenant vous connecter.')
            return redirect('login')
            
        except Exception as e:
            messages.error(request, f'Erreur lors de la création du compte: {str(e)}')
    
    return render(request, 'register.html')



@login_required
def profile_view(request):
    """Vue pour la page de profil avec statistiques dynamiques"""
    user = request.user
    # Statistique 1 : Nombre de CV créés
    cv_count = user.cv_count

    # Statistique 2 : Nombre de compétences (tous CV confondus)
    skill_count = sum(cv.skills.count() for cv in user.cvs.all())

    # Statistique 3 : Nombre de langues (tous CV confondus)
    language_count = sum(cv.languages.count() for cv in user.cvs.all())

    # Statistique 4 : Pourcentage de complétion du profil utilisateur
    important_fields = [user.first_name, user.last_name, user.email, user.gender, user.birth_date, user.city, user.phone, user.profile_picture]
    filled_fields = [f for f in important_fields if f]
    profile_completion = int(len(filled_fields) / len(important_fields) * 100)

    context = {
        'cv_count': cv_count,
        'skill_count': skill_count,
        'language_count': language_count,
        'profile_completion': profile_completion,
    }
    return render(request, 'profile.html', context)


def logout_view(request):
    """Vue pour la déconnexion"""
    logout(request)
    messages.success(request, 'Vous avez été déconnecté avec succès.')
    return redirect('home')