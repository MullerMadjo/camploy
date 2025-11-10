 
from django.urls import path
from . import views

urlpatterns = [
    path('dashboard/', views.dashboard_cv_intelligent, name='dashboard-cv-intelligent'),
    path('delete-cv/<int:cv_id>/', views.delete_cv_view, name='delete-cv'),
    path('add-cv/', views.add_cv_view, name='add-cv'),
    path('edit-cv/<int:cv_id>/', views.edit_cv_view, name='edit-cv'),
    path('add-experience/<int:cv_id>/', views.add_experience_view, name='add-experience'),
    path('add-education/<int:cv_id>/', views.add_education_view, name='add-education'),
    path('add-skill/<int:cv_id>/', views.add_skill_view, name='add-skill'),
    path('add-project/<int:cv_id>/', views.add_project_view, name='add-project'),
    path('add-language/<int:cv_id>/', views.add_language_view, name='add-language'),
    path('add-certification/<int:cv_id>/', views.add_certification_view, name='add-certification'),
    path('dashboard/<int:cv_id>/', views.cv_dashboard_view, name='cv-dashboard'),
    path('edit-experience/<int:exp_id>/', views.edit_experience_view, name='edit-experience'),
    path('edit-education/<int:edu_id>/', views.edit_education_view, name='edit-education'),
    path('edit-skill/<int:skill_id>/', views.edit_skill_view, name='edit-skill'),
    path('edit-project/<int:project_id>/', views.edit_project_view, name='edit-project'),
    path('edit-language/<int:language_id>/', views.edit_language_view, name='edit-language'),
    path('edit-certification/<int:cert_id>/', views.edit_certification_view, name='edit-certification'),
    path('cv/<int:cv_id>/pdf/', views.cv_pdf_view, name='cv_pdf'),
]
