from django.contrib import admin
from django.utils.html import format_html
from django.urls import reverse
from django.utils.safestring import mark_safe
from .models import (
    CV, PersonalInfo, Experience, Education, 
    Skill, Project, Language, Certification
)


class PersonalInfoInline(admin.StackedInline):
    """Inline pour les informations personnelles"""
    model = PersonalInfo
    extra = 0
    fields = [
        'full_name', 'email', 'phone', 'address', 'city', 'country',
        'website', 'linkedin', 'github', 'portfolio', 'profile_picture', 'objective'
    ]


class ExperienceInline(admin.TabularInline):
    """Inline pour les expériences"""
    model = Experience
    extra = 0
    fields = ['job_title', 'company', 'start_date', 'end_date', 'is_current', 'order']
    ordering = ['-start_date']


class EducationInline(admin.TabularInline):
    """Inline pour les formations"""
    model = Education
    extra = 0
    fields = ['degree', 'institution', 'start_date', 'end_date', 'is_current', 'order']
    ordering = ['-start_date']


class SkillInline(admin.TabularInline):
    """Inline pour les compétences"""
    model = Skill
    extra = 0
    fields = ['name', 'category', 'level', 'percentage', 'order']
    ordering = ['category', 'order']


class ProjectInline(admin.TabularInline):
    """Inline pour les projets"""
    model = Project
    extra = 0
    fields = ['name', 'technologies', 'start_date', 'end_date', 'order']
    ordering = ['-start_date']


class LanguageInline(admin.TabularInline):
    """Inline pour les langues"""
    model = Language
    extra = 0
    fields = ['name', 'level', 'certification', 'order']
    ordering = ['order']


class CertificationInline(admin.TabularInline):
    """Inline pour les certifications"""
    model = Certification
    extra = 0
    fields = ['name', 'issuer', 'issue_date', 'expiry_date', 'order']
    ordering = ['-issue_date']


@admin.register(CV)
class CVAdmin(admin.ModelAdmin):
    """Configuration de l'admin pour le modèle CV"""
    
    # Champs à afficher dans la liste
    list_display = [
        'title', 'user', 'status', 'template', 'is_public', 
        'created_at', 'updated_at', 'view_cv_link'
    ]
    
    # Filtres disponibles
    list_filter = [
        'status', 'template', 'is_public', 'color_scheme',
        'created_at', 'updated_at'
    ]
    
    # Champs de recherche
    search_fields = ['title', 'description', 'user__username', 'user__email']
    
    # Champs en lecture seule
    readonly_fields = ['created_at', 'updated_at', 'last_viewed']
    
    # Organisation des champs dans le formulaire d'édition
    fieldsets = (
        ('Informations de base', {
            'fields': ('title', 'description', 'user')
        }),
        ('Statut et visibilité', {
            'fields': ('status', 'is_public')
        }),
        ('Personnalisation', {
            'fields': ('template', 'color_scheme'),
            'classes': ('collapse',)
        }),
        ('Métadonnées', {
            'fields': ('created_at', 'updated_at', 'last_viewed'),
            'classes': ('collapse',)
        }),
    )
    
    # Inlines pour les modèles associés
    inlines = [
        PersonalInfoInline,
        ExperienceInline,
        EducationInline,
        SkillInline,
        ProjectInline,
        LanguageInline,
        CertificationInline,
    ]
    
    # Tri par défaut
    ordering = ['-updated_at']
    
    # Actions personnalisées
    actions = ['publish_cvs', 'unpublish_cvs', 'archive_cvs']
    
    def publish_cvs(self, request, queryset):
        """Publier les CV sélectionnés"""
        queryset.update(status='published')
        self.message_user(request, f"{queryset.count()} CV(s) publié(s).")
    publish_cvs.short_description = "Publier les CV sélectionnés"
    
    def unpublish_cvs(self, request, queryset):
        """Dépublier les CV sélectionnés"""
        queryset.update(status='draft')
        self.message_user(request, f"{queryset.count()} CV(s) dépublié(s).")
    unpublish_cvs.short_description = "Dépublier les CV sélectionnés"
    
    def archive_cvs(self, request, queryset):
        """Archiver les CV sélectionnés"""
        queryset.update(status='archived')
        self.message_user(request, f"{queryset.count()} CV(s) archivé(s).")
    archive_cvs.short_description = "Archiver les CV sélectionnés"
    
    def view_cv_link(self, obj):
        """Lien pour voir le CV"""
        if obj.id:
            return format_html(
                '<a href="/cv/view/{}/" target="_blank">Voir le CV</a>',
                obj.id
            )
        return "-"
    view_cv_link.short_description = "Voir le CV"


@admin.register(Experience)
class ExperienceAdmin(admin.ModelAdmin):
    """Configuration de l'admin pour le modèle Experience"""
    
    list_display = ['job_title', 'company', 'cv', 'start_date', 'end_date', 'is_current']
    list_filter = ['is_current', 'start_date', 'cv__user']
    search_fields = ['job_title', 'company', 'cv__title', 'cv__user__username']
    ordering = ['-start_date']


@admin.register(Education)
class EducationAdmin(admin.ModelAdmin):
    """Configuration de l'admin pour le modèle Education"""
    
    list_display = ['degree', 'institution', 'cv', 'start_date', 'end_date', 'is_current']
    list_filter = ['is_current', 'start_date', 'cv__user']
    search_fields = ['degree', 'institution', 'cv__title', 'cv__user__username']
    ordering = ['-start_date']


@admin.register(Skill)
class SkillAdmin(admin.ModelAdmin):
    """Configuration de l'admin pour le modèle Skill"""
    
    list_display = ['name', 'category', 'level', 'percentage', 'cv']
    list_filter = ['level', 'category', 'cv__user']
    search_fields = ['name', 'category', 'cv__title', 'cv__user__username']
    ordering = ['category', 'name']


@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    """Configuration de l'admin pour le modèle Project"""
    
    list_display = ['name', 'cv', 'start_date', 'end_date', 'github_url']
    list_filter = ['start_date', 'cv__user']
    search_fields = ['name', 'technologies', 'cv__title', 'cv__user__username']
    ordering = ['-start_date']


@admin.register(Language)
class LanguageAdmin(admin.ModelAdmin):
    """Configuration de l'admin pour le modèle Language"""
    
    list_display = ['name', 'level', 'certification', 'cv']
    list_filter = ['level', 'cv__user']
    search_fields = ['name', 'certification', 'cv__title', 'cv__user__username']
    ordering = ['name']


@admin.register(Certification)
class CertificationAdmin(admin.ModelAdmin):
    """Configuration de l'admin pour le modèle Certification"""
    
    list_display = ['name', 'issuer', 'issue_date', 'expiry_date', 'cv']
    list_filter = ['issue_date', 'cv__user']
    search_fields = ['name', 'issuer', 'cv__title', 'cv__user__username']
    ordering = ['-issue_date']


# Configuration du site admin
admin.site.site_header = "Administration Camploy"
admin.site.site_title = "Camploy Admin"
admin.site.index_title = "Gestion de la plateforme Camploy"