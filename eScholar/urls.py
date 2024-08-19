from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('test/', views.test, name='test'),

    # Apprenant URLs
    path('dashboard_apprenant/', views.dashboard_apprenant, name='dashboard_apprenant'),
    path('formation_apprenant/', views.formation_apprenant, name='formation_apprenant'),
    path('chat/', views.chat_apprenant, name='chat_apprenant'),
    path('horaire/', views.horaire_apprenant, name='horaire_apprenant'),
    path('evaluation_apprenant/', views.affichageEvaluation, name='evaluation_apprenant'),
    path('publication_apprenant/', views.affichagePublication, name='publication_apprenant'),
    path('sous_chapitre_apprenant/', views.sous_chapitre_apprenant, name='sous_chapitre_apprenant'),
    path('chapitre_apprenant/', views.chapitre_apprenant, name='chapitre_apprenant'),
    path('liste_apprenant/', views.affichageApprenant, name='liste_apprenant'),
    path('formation_apprenants/', views.affichageFormationApprenant, name='formation_apprenants'),
    path('module_apprenant/', views.affichageModule, name='module_apprenant'),

    # Enseignant URLs
    path('correction/', views.correction_enseignant, name='correction_enseignant'),
    path('cote/', views.correction_enseignant, name='cote_enseignant'),
    path('formation_enseignant/', views.formation_enseignant, name='formation_enseignant'),
    path('interrogation/', views.interrogation_enseignant, name='interrogation_enseignant'),
    path('publication_enseignant/', views.publication_enseignant, name='publication_enseignant'),
    path('dashboard_enseignant/', views.dashboard_enseignant, name='dashboard_enseignant'),
    path('sous_chapitre_enseignant/', views.sous_chapitre_enseignant, name='sous_chapitre_enseignant'),
    path('chapitre_enseignant/', views.chapitre_enseignant, name='chapitre_enseignant'),
    path('insertSousChapitre/', views.insertSousChapitre, name='insertSousChapitre'),
    path('updateSousChapitre/', views.updateSousChapitre, name='updateSousChapitre'),
    path('insertChapitre/', views.insertChapitre, name='insertChapitre'),
    path('updateChapitre/', views.updateChapitre, name='updateChapitre'),
    path('insertContenuChapitre/', views.insertContenuChapitre, name='insertContenuChapitre'),

    # Admin URLs
    path('dashboard_admin/', views.dashboard_admin, name='dashboard_admin'),
    path('formation_admin/', views.formation_admin, name='formation_admin'),
    path('modalite_paiement/', views.modalitepaiement, name='modalite_paiement'),
    path('paiement/', views.paiement, name='paiement'),
    path('insert_paiement/', views.insertPaiement, name='insert_paiement'),
    path('update_paiement/', views.updatePaiement, name='update_paiement'),
    path('publication_admin/', views.publication_admin, name='publication_admin'),
    path('apprenant_admin/', views.apprenant_admin, name='apprenant_admin'),
    path('insert_apprenant/', views.insertApprenant, name='insert_apprenant'),
    path('update_apprenant/', views.updateApprenant, name='update_apprenant'),
    path('domaine_admin/', views.domaine_admin, name='domaine_admin'),
    path('insert_domaine/', views.insertDomaine, name='insert_domaine'),
    path('update_domaine/', views.updateDomaine, name='update_domaine'),
    path('inscription_admin/', views.inscription_admin, name='inscription_admin'),
    path('enseignant_admin/', views.enseignant_admin, name='enseignant_admin'),
    path('insert_enseignant/', views.insertEnseignant, name='insert_enseignant'),
    path('update_enseignant/', views.updateEnseignant, name='update_enseignant'),
    path('insert_formation/', views.insertFormation, name='insert_formation'),
    path('update_formation/', views.updateFormation, name='update_formation'),
    path('insertModalitePaie/', views.insertModalitePaie, name='insertModalitePaie'),
    path('updateModulePaie/', views.updateModalitePaie, name='updateModulePaie'),
    path('insertInscription/', views.insertInscription, name='insertInscription'),
    path('updateInscription/', views.updateInscription, name='updateInscription'),

    # Ressource URLs
    path('ressource_admin/', views.ressource_admin, name='ressource_admin'),
    path('ressource_apprenant/', views.ressource_apprenant, name='ressource_apprenant'),
    path('insertRessource/', views.insertRessource, name='insertRessource'),
    path('updateRessource/', views.updateRessource, name='updateRessource'),
    path('downloadFile/<int:code>/', views.download_file, name='downloadFile'),

    # Publication URLs
    path('publication/', views.publication_admin, name='publication_admin'),
    path('insertPublication/', views.insertPublication, name='insertPublication'),
    path('updatePublication/', views.updatePublication, name='updatePublication'),
    path('all_publication/', views.publication, name='post_list'),
    path('like/<int:post_id>/', views.like_post, name='like_post'),
    path('comment/<int:post_id>/', views.comment_post, name='comment_post'),
    path('popular/', views.popular_posts, name='popular_posts'),

    # Questionnaire URLs
    path('questionnaire/', views.questionnaire, name='questionnaire'),
    path('add_questionnaire/', views.add_questionnaire, name='add_questionnaire'),
    path('updateQuestionnaire/', views.updateQuestionnaire, name='updateQuestionnaire'),
    path('tester_apprenant/', views.tester_apprenant, name='tester_apprenant'),
    path('prendre_test/<int:formation_id>/<int:question_index>/', views.prendre_test, name='prendre_test'),

    # Other URLs
    path('authentification/', views.authentification, name='authentification'),
    path('creer_compte/', views.creer_compte, name='creation_compte_utilisateur'),
    path('profile/', views.profile, name='profile'),
    path('video_conference/', views.video_conference, name='video_conference'),
    path('type_publication_admin/', views.typePublication, name='type_publication_admin'),
    path('liste_formation/', views.Liste_formation, name="liste_formation"),
]
