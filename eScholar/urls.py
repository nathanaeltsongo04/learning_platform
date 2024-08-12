from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('Test', views.test,name='Test'),
    path('dashboard_apprenant/', views.dashboard_apprenant, name='dashboard_apprenant'),
    # path('formation/', views.formation_apprenant, name='formation_apprenant'),
    path('chat/', views.chat_apprenant, name='chat_apprenant'),
    path('horaire/', views.horaire_apprenant, name='horaire_apprenant'),
    path('correcton/',views.correction_enseignant,name='correction_enseignant'),
    path('cote/',views.correction_enseignant,name='cote_enseignant'),
    # path('formation/',views.formation_enseignant,name='formation_enseignant'),
    # path('interrogation/',views.interrogation_enseignant,name='interrogation_enseignant'),
    path('ressource_apprenant/', views.ressource_apprenant, name='ressource_apprenant'),
    # path('publication/',views.publication_enseignant,name='publication_enseignant'),
    path('dashboard_enseignant',views.dashboard_enseignant,name='dashboard_enseignant'),
    path('dashboard_admin/',views.dashboard_admin,name='dashboard_admin'),

    path('paiement/',views.paiement,name='paiement'),
    path('insertPaiement/',views.insertPaiement,name='insertPaiement'),
    path('updatePaiement/',views.updatePaiement,name='updatePaiement'),
    
    
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
    path('logout/',views.logout_view,name='logout'),
    path('rediriger_apprenant/',views.rediriger_apprenant,name='rediriger_apprenant'),
    # path('profile/',views.profile,name='profile'),

    path('formation/',views.formation_admin,name='formation_admin'),
    # path('formation/',views.formation_admin,name='formation_enseignant'),
    path('insertFormation/', views.insertFormation, name = 'insertFormation'),
    path('updateFormation/', views.updateFormation, name='updateFormation'),

    path('modalite_paiement/',views.modalitepaiement,name='modalite_paiement'),
    path('insertModalitePaie/', views.insertModalitePaie, name='insertModalitePaie'),
    path('updateModulePaie/', views.updateModalitePaie, name='updateModulePaie'),

    path('inscription/',views.inscription_admin,name='inscription_admin'),
    path('insertInscription/', views.insertInscription, name='insertInscription'),
    path('updateInscription/', views.updateInscription, name='updateInscription'),
    
    path('evaluation/', views.evaluation, name='evaluation'),
    path('insertEvaluation/', views.insertEvaluation, name='insertEvaluation'),
    path('updateEvaluation/', views.updateEvaluation, name='updateEvaluation'),
    
    
    path('module/',views.module_enseignant,name='module_enseignant'),
    path('insertModule/', views.insertModule, name = 'insertModule'),
    path('updateModule/', views.updateModule, name='updateModule'),
    
    path('niveau/',views.niveau,name='niveau_admin'),
    path('insertNiveau/', views.insertNiveau, name = 'insertNiveau'),
    path('updateNiveau/', views.updateNiveau, name='updateNiveau'),
    
    path('typeressource/',views.typeressource,name='typeressource'),
    path('insertTypeRessource/',views.insertTypeRessource,name='insertTypeRessource'),
    path('updateTypeRessource/',views.updateTypeRessource,name='updateTypeRessource'),
    
    path('ressource/', views.ressource_admin, name='ressource_admin'),
    path('insertRessource/', views.insertRessource, name='insertRessource'),
    path('updateRessource/', views.updateRessource, name='updateRessource'),
    path('downloadFile/<int:code>', views.download_file, name='downloadFile'),


    path('publication/',views.publication_admin,name='publication_admin'),
    path('insertPublication/',views.insertPublication,name='insertPublication'),
    path('updatePublication/',views.updatePublication,name='updatePublication'),

    path('all_publication', views.publication, name='post_list'),
    path('like/<int:post_id>/', views.like_post, name='like_post'),
    path('comment/<int:post_id>/', views.comment_post, name='comment_post'),
    path('popular/', views.popular_posts, name='popular_posts'),

    path('add_questionnaire', views.add_questionnaire, name='add_questionnaire'),
    path('updateQuestionnaire', views.updateQuestionnaire, name='updateQuestionnaire'),

    path('tester_apprenant', views.tester_apprenant, name='tester_apprenant'),

    path('prendre_test/<int:formation_id>/<int:question_index>/', views.prendre_test, name='prendre_test'),



# ===============================================================================
# ============================== Partie Apprenant ================================
    path('module_apprenant/',views.affichageModule,name='module_apprenant'),
    path('formation_apprenants/',views.affichageFormationApprenant,name='formation_apprenants'),
    path('evaluation_apprenant/',views.affichageEvaluation,name='evaluation_apprenant'),
    path('publication_apprenant/',views.affichagePublication,name='publication_apprenant'),
    
    
    path('sous_chapitre_apprenant/',views.sous_chapitre_apprenant,name='sous_chapitre_apprenant'),
    path('chapitre_apprenant/',views.chapitre_apprenant,name='chapitre_apprenant'),
    
    
    # ============================== Partie Enseignant ================================
    path('liste_apprenant/',views.affichageApprenant,name='liste_apprenant'),
    path('formation_enseignant/',views.affichageFormationEnseignant,name='formation_enseignant'),
    
    path('sous_chapitre_enseignant/',views.sous_chapitre_enseignant,name='sous_chapitre_enseignant'),
    path('chapitre_enseignant/',views.chapitre_enseignant,name='chapitre_enseignant'),
    
    
    # ============================== Partie Admin ================================
    path('type_publication_admin/',views.typePublication,name='type_publication_admin'), 
]
