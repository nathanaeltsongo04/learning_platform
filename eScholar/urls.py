from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('Test', views.test,name='Test'),
    path('dashboard_apprenant/', views.dashboard_apprenant, name='dashboard_apprenant'),
    path('formation/', views.formation_apprenant, name='formation_apprenant'),
    path('chat/', views.chat_apprenant, name='chat_apprenant'),
    path('horaire/', views.horaire_apprenant, name='horaire_apprenant'),
    path('correcton/',views.correction_enseignant,name='correction_enseignant'),
    path('cote/',views.correction_enseignant,name='cote_enseignant'),
    path('formation/',views.formation_enseignant,name='formation_enseignant'),
    path('interrogation/',views.interrogation_enseignant,name='interrogation_enseignant'),
    path('publication/',views.publication_enseignant,name='publication_enseignant'),
    path('dashboard_enseignant',views.dashboard_enseignant,name='dashboard_enseignant'),
    path('dashboard_admin/',views.dashboard_admin,name='dashboard_admin'),
    path('apprenant/',views.apprenant_admin,name='apprenant_admin'),
    path('enseignant/',views.enseignant_admin,name='enseignant_admin'),
    path('formation/',views.formation_admin,name='formation_admin'),
    path('modalite paiement',views.modalitepaiement,name='modalite_paiement'),
    path('paiement/',views.paiement,name='paiement'),
    path('publication/',views.publication_admin,name='publication_admin'),
    
    path('domaine/',views.domaine_admin,name='domaine_admin'),
    path('insertDomaine/', views.insertDomaine, name = 'insertDomaine'),
    path('updateDomaine/', views.updateDomaine, name='updateDomaine'),
    
    
    
    path('module/',views.module_enseignant,name='module_enseignant'),
    path('insertModule/', views.insertModule, name = 'insertModule'),
    path('updateModule/', views.updateModule, name='updateModule'),
    
    path('niveau/',views.niveau,name='niveau_admin'),
    path('insertNiveau/', views.insertNiveau, name = 'insertNiveau'),
    path('updateNiveau/', views.updateNiveau, name='updateNiveau'),
    
    path('typeressource/',views.typeressource,name='typeressource'),
    path('insertTypeRessource/',views.insertTypeRessource,name='insertTypeRessource'),
    path('updateTypeRessource/',views.updateTypeRessource,name='updateTypeRessource'),
    
    path('ressource/', views.ressource_apprenant, name='ressource_apprenant'),
    path('insertRessource/', views.insertRessource, name='insertRessource'),
    path('updateRessource/', views.updateRessource, name='updateRessource'),
]
