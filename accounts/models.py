from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils import timezone


class User(AbstractUser):
    """Modèle utilisateur étendu"""
    
    # Choix pour le sexe
    GENDER_CHOICES = [
        ('M', 'Masculin'),
        ('F', 'Féminin'),
        ('O', 'Autre'),
        ('N', 'Préfère ne pas dire'),
    ]
    
    # Informations personnelles authentiques
    first_name = models.CharField(max_length=150, verbose_name="Prénom")
    last_name = models.CharField(max_length=150, verbose_name="Nom")
    gender = models.CharField(
        max_length=1, 
        choices=GENDER_CHOICES, 
        blank=True, 
        null=True, 
        verbose_name="Sexe"
    )
    birth_date = models.DateField(blank=True, null=True, verbose_name="Date de naissance")
    
    # Informations de contact
    phone = models.CharField(max_length=20, blank=True, null=True, verbose_name="Téléphone")
    address = models.TextField(blank=True, null=True, verbose_name="Adresse")
    city = models.CharField(max_length=100, blank=True, null=True, verbose_name="Ville de résidence")
    country = models.CharField(max_length=100, blank=True, null=True, verbose_name="Pays")
    postal_code = models.CharField(max_length=20, blank=True, null=True, verbose_name="Code postal")
    
    # Informations professionnelles
    profession = models.CharField(max_length=200, blank=True, null=True, verbose_name="Profession")
    company = models.CharField(max_length=200, blank=True, null=True, verbose_name="Entreprise")
    website = models.URLField(blank=True, null=True, verbose_name="Site web")
    linkedin = models.URLField(blank=True, null=True, verbose_name="LinkedIn")
    github = models.URLField(blank=True, null=True, verbose_name="GitHub")
    
    # Photo de profil
    profile_picture = models.ImageField(
        upload_to='profile_pics/', 
        blank=True, 
        null=True, 
        verbose_name="Photo de profil"
    )
    
    # Préférences
    bio = models.TextField(blank=True, null=True, verbose_name="Biographie")
    is_public = models.BooleanField(default=True, verbose_name="Profil public")
    
    # Métadonnées
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Créé le")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="Modifié le")
    
    class Meta:
        verbose_name = "Utilisateur"
        verbose_name_plural = "Utilisateurs"
        ordering = ['-created_at']
    
    def __str__(self):
        return f"{self.first_name} {self.last_name}" if self.first_name and self.last_name else self.username
    
    @property
    def full_name(self):
        """Retourne le nom complet de l'utilisateur"""
        if self.first_name and self.last_name:
            return f"{self.first_name} {self.last_name}"
        return self.username
    
    @property
    def cv_count(self):
        """Retourne le nombre de CV de l'utilisateur"""
        return self.cvs.count()