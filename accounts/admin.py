from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.utils.html import format_html
from .models import User


@admin.register(User)
class UserAdmin(BaseUserAdmin):
    """Configuration de l'admin pour le modèle User personnalisé"""
    
    # Champs à afficher dans la liste des utilisateurs
    list_display = [
        'username', 'email', 'full_name', 'gender', 'birth_date', 'city', 
        'profession', 'is_active', 'is_staff', 'date_joined', 'cv_count'
    ]
    
    # Filtres disponibles
    list_filter = [
        'is_active', 'is_staff', 'is_superuser', 'gender',
        'date_joined', 'last_login', 'is_public', 'city', 'country'
    ]
    
    # Champs de recherche
    search_fields = ['username', 'email', 'first_name', 'last_name', 'profession']
    
    # Champs en lecture seule
    readonly_fields = ['date_joined', 'last_login', 'cv_count']
    
    # Organisation des champs dans le formulaire d'édition
    fieldsets = (
        ('Informations de connexion', {
            'fields': ('username', 'password', 'email')
        }),
        ('Informations personnelles', {
            'fields': ('first_name', 'last_name', 'gender', 'birth_date', 'phone', 'profile_picture')
        }),
        ('Adresse', {
            'fields': ('address', 'city', 'country', 'postal_code'),
            'classes': ('collapse',)
        }),
        ('Informations professionnelles', {
            'fields': ('profession', 'company', 'website', 'linkedin', 'github'),
            'classes': ('collapse',)
        }),
        ('Profil', {
            'fields': ('bio', 'is_public'),
            'classes': ('collapse',)
        }),
        ('Permissions', {
            'fields': ('is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions'),
            'classes': ('collapse',)
        }),
        ('Dates importantes', {
            'fields': ('date_joined', 'last_login'),
            'classes': ('collapse',)
        }),
    )
    
    # Champs pour l'ajout d'un nouvel utilisateur
    add_fieldsets = (
        ('Informations de base', {
            'classes': ('wide',),
            'fields': ('username', 'email', 'password1', 'password2'),
        }),
        ('Informations personnelles', {
            'classes': ('wide',),
            'fields': ('first_name', 'last_name', 'gender', 'birth_date', 'phone'),
        }),
    )
    
    # Tri par défaut
    ordering = ['-date_joined']
    
    # Actions personnalisées
    actions = ['make_active', 'make_inactive', 'make_public', 'make_private']
    
    def make_active(self, request, queryset):
        """Activer les utilisateurs sélectionnés"""
        queryset.update(is_active=True)
        self.message_user(request, f"{queryset.count()} utilisateur(s) activé(s).")
    make_active.short_description = "Activer les utilisateurs sélectionnés"
    
    def make_inactive(self, request, queryset):
        """Désactiver les utilisateurs sélectionnés"""
        queryset.update(is_active=False)
        self.message_user(request, f"{queryset.count()} utilisateur(s) désactivé(s).")
    make_inactive.short_description = "Désactiver les utilisateurs sélectionnés"
    
    def make_public(self, request, queryset):
        """Rendre publics les profils sélectionnés"""
        queryset.update(is_public=True)
        self.message_user(request, f"{queryset.count()} profil(s) rendu(s) public(s).")
    make_public.short_description = "Rendre publics les profils"
    
    def make_private(self, request, queryset):
        """Rendre privés les profils sélectionnés"""
        queryset.update(is_public=False)
        self.message_user(request, f"{queryset.count()} profil(s) rendu(s) privé(s).")
    make_private.short_description = "Rendre privés les profils"
    
    def cv_count(self, obj):
        """Afficher le nombre de CV de l'utilisateur"""
        count = obj.cvs.count()
        if count > 0:
            return format_html(
                '<a href="/admin/cv/cv/?user__id__exact={}">{} CV(s)</a>',
                obj.id, count
            )
        return "0 CV"
    cv_count.short_description = "Nombre de CV"
    cv_count.admin_order_field = 'cvs__count'