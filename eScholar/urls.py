from django.urls import path
from . import views

urlpatterns = [
    path('', views.Index, name='home'),
    path('Test', views.Test,name='Test'),
    path('dashboard_apprenant/', views.Dashboard_apprenant, name='dashboard_apprenant'),
    path('formation/', views.Formation_apprenant, name='formation_apprenant'),
    path('ressource/', views.Ressource_apprenant, name='ressource_apprenant'),
    path('chat/', views.Chat_apprenant, name='chat_apprenant'),
    path('horaire/', views.Horaire_apprenant, name='horaire_apprenant'),
    path('correcton/',views.Correction_enseignant,name='correction_enseignant'),
    path('cote/',views.Correction_enseignant,name='cote_enseignant'),
    path('formation/',views.Formation_enseignant,name='formation_enseignant'),
    path('interrogation/',views.Interrogation_enseignant,name='interrogation_enseignant'),
    path('module/',views.Module_enseignant,name='module_enseignant'),
    path('publication/',views.Publication_enseignant,name='publication_enseignant'),
    path('dashboard_enseignant',views.Dashboard_enseignant,name='dashboard_enseignant'),
    path('dashboard_admin/',views.Dashboard_admin,name='dashboard_admin'),
    path('apprenant/',views.Apprenant_admin,name='apprenant_admin'),
    path('domaine/',views.Domaine_admin,name='domaine_admin'),
    path('enseignant/',views.Enseignant_admin,name='enseignant_admin'),
    path('formation/',views.Formation_admin,name='formation_admin'),
    path('modalite paiement',views.Modalitepaiement,name='modalite_paiement'),
    path('niveau/',views.Niveau,name='niveau_admin'),
    path('paiement/',views.Paiement,name='paiement'),
    path('publication/',views.Publication_admin,name='publication_admin'),
    path('ressource/',views.Typeressource,name='type_ressource')
]
