from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='home'),
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
    path('formation/',views.formation_admin,name='formation_admin'),
    path('modalite_paiement',views.modalitepaiement,name='modalite_paiement'),
    path('niveau/',views.niveau,name='niveau_admin'),
    path('paiement/',views.paiement,name='paiement'),
    path('publication/',views.publication_admin,name='publication_admin'),
    path('ressource/',views.typeressource,name='type_ressource'),
    
    
    path('apprenant/',views.apprenant_admin,name='apprenant_admin'),
    path('insert_apprenant/',views.insertApprenant,name='insert_apprenant'),
    path('update_apprenant/',views.updateApprenant,name='update_apprenant'),
    
    path('domaine/',views.domaine_admin,name='domaine_admin'),
    path('insertDomaine/', views.insertDomaine, name = 'insertDomaine'),
    path('updateDomaine/', views.updateDomaine, name='updateDomaine'),
    
    path('enseignant/',views.enseignant_admin,name='enseignant_admin'),
    path('insert_enseignant/', views.insertEnseignant, name = 'insert_enseignant'),
    path('update_enseignant/', views.updateEnseignant, name='update_enseignant'),
    
    path('authentification/',views.authentification,name='authentification'),
    path('creer_compte/',views.creer_compte,name='creation_compte_utilisateur'),
    path('profile/',views.profile,name='profile'),

    path('insertFormation/', views.insertFormation, name = 'insertFormation'),
    path('updateFormation/', views.updateFormation, name='updateFormation'),
    path('insertModalitePaie/', views.insertModalitePaie, name='insertModalitePaie'),
    path('updateModulePaie/', views.updateModalitePaie, name='updateModulePaie'),
    path('inscription/',views.inscription_admin,name='inscription_admin'),
    path('insertInscription/', views.insertInscription, name='insertInscription'),
    path('updateInscription/', views.updateInscription, name='updateInscription'),
    
    path('Evaluation/', views.evaluation, name='Evaluation'),
    path('insertEvaluation/', views.insertEvaluation, name='insertEvaluation'),
]
