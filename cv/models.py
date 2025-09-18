from django.db import models
from django.contrib.auth import get_user_model
from django.utils import timezone
from django.core.validators import MinLengthValidator

User = get_user_model()


class CV(models.Model):
    """Modèle pour les CV"""
    
    STATUS_CHOICES = [
        ('draft', 'Brouillon'),
        ('published', 'Publié'),
        ('archived', 'Archivé'),
    ]
    
    TEMPLATE_CHOICES = [
        ('modern', 'Moderne'),
        ('classic', 'Classique'),
        ('creative', 'Créatif'),
        ('minimal', 'Minimaliste'),
    ]
    
    # Informations de base
    title = models.CharField(
        max_length=200, 
        verbose_name="Titre du CV",
        validators=[MinLengthValidator(3)]
    )
    description = models.TextField(
        blank=True, 
        null=True, 
        verbose_name="Description"
    )
    
    # Propriétaire du CV
    user = models.ForeignKey(
        User, 
        on_delete=models.CASCADE, 
        related_name='cvs',
        verbose_name="Propriétaire"
    )
    
    # Statut et visibilité
    status = models.CharField(
        max_length=20, 
        choices=STATUS_CHOICES, 
        default='draft',
        verbose_name="Statut"
    )
    is_public = models.BooleanField(
        default=False, 
        verbose_name="Public"
    )
    
    # Liens professionnels
    github = models.URLField(blank=True, null=True, verbose_name="Lien GitHub")
    linkedin = models.URLField(blank=True, null=True, verbose_name="Lien LinkedIn")

    # Template et personnalisation (optionnel, masqué à la création)
    template = models.CharField(
        max_length=20, 
        choices=TEMPLATE_CHOICES, 
        default='modern',
        verbose_name="Template"
    )
    color_scheme = models.CharField(
        max_length=50, 
        default='blue',
        verbose_name="Schéma de couleurs"
    )
    
    # Métadonnées
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Créé le")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="Modifié le")
    last_viewed = models.DateTimeField(null=True, blank=True, verbose_name="Dernière consultation")
    
    class Meta:
        verbose_name = "CV"
        verbose_name_plural = "CVs"
        ordering = ['-updated_at']
        unique_together = ['user', 'title']
    
    def __str__(self):
        return f"{self.title} - {self.user.username}"
    
    def save(self, *args, **kwargs):
        # Mettre à jour la date de modification
        self.updated_at = timezone.now()
        super().save(*args, **kwargs)


class PersonalInfo(models.Model):
    """Informations personnelles pour un CV"""
    
    cv = models.OneToOneField(
        CV, 
        on_delete=models.CASCADE, 
        related_name='personal_info',
        verbose_name="CV"
    )
    
    # Informations personnelles
    full_name = models.CharField(max_length=200, verbose_name="Nom complet")
    email = models.EmailField(verbose_name="Email")
    phone = models.CharField(max_length=20, blank=True, null=True, verbose_name="Téléphone")
    address = models.TextField(blank=True, null=True, verbose_name="Adresse")
    city = models.CharField(max_length=100, blank=True, null=True, verbose_name="Ville")
    country = models.CharField(max_length=100, blank=True, null=True, verbose_name="Pays")
    postal_code = models.CharField(max_length=20, blank=True, null=True, verbose_name="Code postal")
    
    # Liens professionnels
    website = models.URLField(blank=True, null=True, verbose_name="Site web")
    linkedin = models.URLField(blank=True, null=True, verbose_name="LinkedIn")
    github = models.URLField(blank=True, null=True, verbose_name="GitHub")
    portfolio = models.URLField(blank=True, null=True, verbose_name="Portfolio")
    
    # Photo de profil
    profile_picture = models.ImageField(
        upload_to='cv_photos/', 
        blank=True, 
        null=True, 
        verbose_name="Photo de profil"
    )
    
    # Objectif professionnel
    objective = models.TextField(
        blank=True, 
        null=True, 
        verbose_name="Objectif professionnel"
    )
    
    class Meta:
        verbose_name = "Informations personnelles"
        verbose_name_plural = "Informations personnelles"
    
    def __str__(self):
        return f"Infos personnelles - {self.cv.title}"


class Experience(models.Model):
    """Expérience professionnelle"""
    
    cv = models.ForeignKey(
        CV, 
        on_delete=models.CASCADE, 
        related_name='experiences',
        verbose_name="CV"
    )
    
    # Informations de l'expérience
    job_title = models.CharField(max_length=200, verbose_name="Poste")
    company = models.CharField(max_length=200, verbose_name="Entreprise")
    location = models.CharField(max_length=200, blank=True, null=True, verbose_name="Lieu")
    
    # Dates
    start_date = models.DateField(verbose_name="Date de début")
    end_date = models.DateField(blank=True, null=True, verbose_name="Date de fin")
    is_current = models.BooleanField(default=False, verbose_name="Poste actuel")
    
    # Description
    description = models.TextField(verbose_name="Description")
    achievements = models.TextField(blank=True, null=True, verbose_name="Réalisations")
    
    # Ordre d'affichage
    order = models.PositiveIntegerField(default=0, verbose_name="Ordre")
    
    class Meta:
        verbose_name = "Expérience"
        verbose_name_plural = "Expériences"
        ordering = ['-start_date', '-order']
    
    def __str__(self):
        return f"{self.job_title} chez {self.company}"


class Education(models.Model):
    """Formation et éducation"""
    
    cv = models.ForeignKey(
        CV, 
        on_delete=models.CASCADE, 
        related_name='educations',
        verbose_name="CV"
    )
    
    # Informations de la formation
    degree = models.CharField(max_length=200, verbose_name="Diplôme")
    institution = models.CharField(max_length=200, verbose_name="Établissement")
    location = models.CharField(max_length=200, blank=True, null=True, verbose_name="Lieu")
    field_of_study = models.CharField(max_length=200, blank=True, null=True, verbose_name="Domaine d'études")
    
    # Dates
    start_date = models.DateField(verbose_name="Date de début")
    end_date = models.DateField(blank=True, null=True, verbose_name="Date de fin")
    is_current = models.BooleanField(default=False, verbose_name="Formation en cours")
    
    # Notes et réalisations
    gpa = models.CharField(max_length=10, blank=True, null=True, verbose_name="Moyenne")
    description = models.TextField(blank=True, null=True, verbose_name="Description")
    achievements = models.TextField(blank=True, null=True, verbose_name="Réalisations")
    
    # Ordre d'affichage
    order = models.PositiveIntegerField(default=0, verbose_name="Ordre")
    
    class Meta:
        verbose_name = "Formation"
        verbose_name_plural = "Formations"
        ordering = ['-start_date', '-order']
    
    def __str__(self):
        return f"{self.degree} - {self.institution}"


class Skill(models.Model):
    """Compétences"""
    
    SKILL_LEVEL_CHOICES = [
        ('beginner', 'Débutant'),
        ('intermediate', 'Intermédiaire'),
        ('advanced', 'Avancé'),
        ('expert', 'Expert'),
    ]
    
    cv = models.ForeignKey(
        CV, 
        on_delete=models.CASCADE, 
        related_name='skills',
        verbose_name="CV"
    )
    
    # Informations de la compétence
    name = models.CharField(max_length=100, verbose_name="Nom de la compétence")
    category = models.CharField(max_length=100, blank=True, null=True, verbose_name="Catégorie")
    level = models.CharField(
        max_length=20, 
        choices=SKILL_LEVEL_CHOICES, 
        default='intermediate',
        verbose_name="Niveau"
    )
    percentage = models.PositiveIntegerField(
        default=50, 
        verbose_name="Pourcentage",
        help_text="Pourcentage de maîtrise (0-100)"
    )
    
    # Ordre d'affichage
    order = models.PositiveIntegerField(default=0, verbose_name="Ordre")
    
    class Meta:
        verbose_name = "Compétence"
        verbose_name_plural = "Compétences"
        ordering = ['category', 'order', 'name']
    
    def __str__(self):
        return f"{self.name} ({self.get_level_display()})"


class Project(models.Model):
    """Projets"""
    
    cv = models.ForeignKey(
        CV, 
        on_delete=models.CASCADE, 
        related_name='projects',
        verbose_name="CV"
    )
    
    # Informations du projet
    name = models.CharField(max_length=200, verbose_name="Nom du projet")
    description = models.TextField(verbose_name="Description")
    technologies = models.CharField(
        max_length=500, 
        blank=True, 
        null=True, 
        verbose_name="Technologies utilisées",
        help_text="Séparez les technologies par des virgules"
    )
    
    # Liens
    github_url = models.URLField(blank=True, null=True, verbose_name="Lien GitHub")
    live_url = models.URLField(blank=True, null=True, verbose_name="Lien du projet")
    
    # Dates
    start_date = models.DateField(blank=True, null=True, verbose_name="Date de début")
    end_date = models.DateField(blank=True, null=True, verbose_name="Date de fin")
    
    # Ordre d'affichage
    order = models.PositiveIntegerField(default=0, verbose_name="Ordre")
    
    class Meta:
        verbose_name = "Projet"
        verbose_name_plural = "Projets"
        ordering = ['-start_date', '-order']
    
    def __str__(self):
        return self.name


class Language(models.Model):
    """Langues"""
    
    LANGUAGE_LEVEL_CHOICES = [
        ('basic', 'Notions de base'),
        ('intermediate', 'Intermédiaire'),
        ('advanced', 'Avancé'),
        ('native', 'Langue maternelle'),
        ('fluent', 'Courant'),
    ]
    
    cv = models.ForeignKey(
        CV, 
        on_delete=models.CASCADE, 
        related_name='languages',
        verbose_name="CV"
    )
    
    # Informations de la langue
    name = models.CharField(max_length=100, verbose_name="Langue")
    level = models.CharField(
        max_length=20, 
        choices=LANGUAGE_LEVEL_CHOICES,
        verbose_name="Niveau"
    )
    certification = models.CharField(
        max_length=200, 
        blank=True, 
        null=True, 
        verbose_name="Certification"
    )
    
    # Ordre d'affichage
    order = models.PositiveIntegerField(default=0, verbose_name="Ordre")
    
    class Meta:
        verbose_name = "Langue"
        verbose_name_plural = "Langues"
        ordering = ['order', 'name']
    
    def __str__(self):
        return f"{self.name} ({self.get_level_display()})"


class Certification(models.Model):
    """Certifications"""
    
    cv = models.ForeignKey(
        CV, 
        on_delete=models.CASCADE, 
        related_name='certifications',
        verbose_name="CV"
    )
    
    # Informations de la certification
    name = models.CharField(max_length=200, verbose_name="Nom de la certification")
    issuer = models.CharField(max_length=200, verbose_name="Organisme émetteur")
    credential_id = models.CharField(
        max_length=100, 
        blank=True, 
        null=True, 
        verbose_name="ID de la certification"
    )
    
    # Dates
    issue_date = models.DateField(verbose_name="Date d'obtention")
    expiry_date = models.DateField(blank=True, null=True, verbose_name="Date d'expiration")
    
    # Liens
    credential_url = models.URLField(blank=True, null=True, verbose_name="Lien de vérification")
    
    # Ordre d'affichage
    order = models.PositiveIntegerField(default=0, verbose_name="Ordre")
    
    class Meta:
        verbose_name = "Certification"
        verbose_name_plural = "Certifications"
        ordering = ['-issue_date', '-order']
    
    def __str__(self):
        return f"{self.name} - {self.issuer}"