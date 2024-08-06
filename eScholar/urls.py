from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('Test', views.test,name='Test'),
    path('dashboard_apprenant/', views.dashboard_apprenant, name='dashboard_apprenant'),
    path('formation/', views.formation_apprenant, name='formation_apprenant'),
    path('ressource/', views.ressource_apprenant, name='ressource_apprenant'),
    path('chat/', views.chat_apprenant, name='chat_apprenant'),
    path('horaire/', views.horaire_apprenant, name='horaire_apprenant'),
    path('correcton/',views.correction_enseignant,name='correction_enseignant'),
    path('cote/',views.correction_enseignant,name='cote_enseignant'),
    path('formation/',views.formation_enseignant,name='formation_enseignant'),
    path('interrogation/',views.interrogation_enseignant,name='interrogation_enseignant'),
    path('module/',views.module_enseignant,name='module_enseignant'),
    path('publication/',views.publication_enseignant,name='publication_enseignant'),
    path('dashboard_enseignant',views.dashboard_enseignant,name='dashboard_enseignant'),
    path('dashboard_admin/',views.dashboard_admin,name='dashboard_admin'),
    path('apprenant/',views.apprenant_admin,name='apprenant_admin'),
    path('enseignant/',views.enseignant_admin,name='enseignant_admin'),
    path('formation/',views.formation_admin,name='formation_admin'),
    path('modalite paiement',views.modalitepaiement,name='modalite_paiement'),
    path('niveau/',views.niveau,name='niveau_admin'),
    path('paiement/',views.paiement,name='paiement'),
    path('publication/',views.publication_admin,name='publication_admin'),
    path('ressource/',views.typeressource,name='type_ressource'),
    path('domaine/',views.domaine_admin,name='domaine_admin'),
    path('insertDomaine/', views.insertDomaine, name = 'insertDomaine'),
    path('updateDomaine/', views.updateDomaine, name='updateDomaine'),
]
