from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('authentification', views.authentification, name='authentification'),
    path('rediriger_utilisateur', views.rediriger_utilisateur, name='rediriger_utilisateur'),
    path('creer_compte', views.creer_compte, name='creation_compte_utilisateur'),
    path('logout', views.logout_view, name='logout'),
    path('logged_out', views.logged_out, name='logged_out'),
    path('profile', views.profile, name='profile'),
#=========================================================================================================
# ADMINISTRATEUR
# ========================================================================================================
 
    path('dashboard_admin', views.dashboard_admin, name='dashboard_admin'),
    path('niveau_admin', views.niveau, name='niveau_admin'),
    path('insertNiveau', views.insertNiveau, name='insertNiveau'),
    path('updateNiveau', views.updateNiveau, name='updateNiveau'),

    path('domaine_admin', views.domaine_admin, name='domaine_admin'),
    path('insertDomaine', views.insertDomaine, name='insertDomaine'),
    path('updateDomaine', views.updateDomaine, name='updateDomaine'),

    path('apprenant_admin', views.apprenant_admin, name='apprenant_admin'),
    path('insertApprenant', views.insertApprenant, name='insert_apprenant'),
    path('updateApprenant', views.updateApprenant, name='update_apprenant'),

    path('enseignant_admin', views.enseignant_admin, name='enseignant_admin'),
    path('insertEnseignant', views.insertEnseignant, name='insert_enseignant'),
    path('updateEnseignant', views.updateEnseignant, name='update_enseignant'),

    path('formation_admin', views.formation_admin, name='formation_admin'),
    path('insertFormation', views.insertFormation, name='insertFormation'),
    path('updateFormation', views.updateFormation, name='updateFormation'),

    path('modalitepaiement', views.modalitepaiement, name='modalitepaiement'),
    path('insertModalitePaie', views.insertModalitePaie, name='insertModalitePaie'),
    path('updateModalitePaie', views.updateModalitePaie, name='updateModalitePaie'),

    path('paiement', views.paiement, name='paiement'),
    path('insertPaiement', views.insertPaiement, name='insertPaiement'),
    path('updatePaiement', views.updatePaiement, name='updatePaiement'),

    path('inscription_admin', views.inscription_admin, name='inscription_admin'),
    path('insertInscription', views.insertInscription, name='insertInscription'),
    path('updateInscription', views.updateInscription, name='updateInscription'),

    path('all_publications', views.publication, name='all_publications'),
    path('publication_admin', views.publication_admin, name='publication_admin'),
    path('insertPublication', views.insertPublication, name='insertPublication'),
    path('updatePublication', views.updatePublication, name='updatePublication'),

# ========================================================================================================
# ENSEIGNANT
# ========================================================================================================

    path('dashboard_enseignant', views.dashboard_enseignant, name='dashboard_enseignant'),
    path('formation_enseignant', views.formation_enseignant, name='formation_enseignant'),
    path('updateFormationEnseignant', views.updateFormation, name='updateFormationEnseignant'),

    path('enseignant_liste_apprenant', views.enseignant_liste_apprenant, name='enseignant_liste_apprenant'),

    path('sous_chapitre_enseignant', views.sous_chapitre_enseignant, name='sous_chapitre_enseignant'),
    path('insertSousChapitre', views.insertSousChapitre, name='insertSousChapitre'),
    path('updateSousChapitre', views.updateSousChapitre, name='updateSousChapitre'),

    path('chapitre_enseignant', views.chapitre_enseignant, name='chapitre_enseignant'),
    path('insertChapitre', views.insertChapitre, name='insertChapitre'),
    path('updateChapitre', views.updateChapitre, name='updateChapitre'),
    path('insertContenuChapitre', views.insertContenuChapitre, name='insertContenuChapitre'),

    path('module_enseignant', views.module_enseignant, name='module_enseignant'),
    path('insertModule', views.insertModule, name='insertModule'),
    path('updateModule', views.updateModule, name='updateModule'),

    path('questionnaire', views.questionnaire, name='questionnaire'),
    path('add_questionnaire', views.add_questionnaire, name='add_questionnaire'),
    path('updateQuestionnaire', views.updateQuestionnaire, name='updateQuestionnaire'),

    path('reponsesAlternatives', views.reponsesAlternatives, name='reponsesAlternatives'),
    path('insertReponseAlternative', views.insertReponseAlternative, name='insertReponseAlternative'),
    path('updateReponseAlternative', views.updateReponseAlternative, name='updateReponseAlternative'),

    path('typeressource', views.typeressource, name='typeressource'),
    path('insertTypeRessource', views.insertTypeRessource, name='insertTypeRessource'),
    path('updateTypeRessource', views.updateTypeRessource, name='updateTypeRessource'),

    path('ressource', views.ressource, name='ressource'),
    path('insertRessource', views.insertRessource, name='insertRessource'),
    path('updateRessource', views.updateRessource, name='updateRessource'),    
    path('downloadFile/<int:code>', views.download_file, name='downloadFile'),

    path('participation', views.participation, name='participation'),
    path('evaluation', views.evaluation, name='evaluation'),
    path('insertInterrogation', views.insertInterrogation, name='insertInterrogation'),
    path('updateInterrogation', views.updateInterrogation, name='updateInterrogation'),

    path('questionInterro', views.questionInterro, name='questionInterro'),
    path('insertQuestionInterro', views.insertQuestionInterro, name='insertQuestionInterro'),
    path('updateQuestionInterro', views.updateQuestionInterro, name='updateQuestionInterro'),
    path('reponsesAlternativesInterro', views.reponsesAlternativesInterro, name='reponsesAlternativesInterro'),
    path('insertReponseAlternativeInterro', views.insertReponseAlternativeInterro, name='insertReponseAlternativeInterro'),
    path('updateReponseAlternativeInterro', views.updateReponseAlternativeInterro, name='updateReponseAlternativeInterro'),

    path('publication_enseignant', views.publication_enseignant, name='publication_enseignant'),
    path('video_conference', views.video_conference, name='video_conference'),

# ========================================================================================================
# APPRENANT
# ========================================================================================================
    path('tester_apprenant', views.tester_apprenant, name='tester_apprenant'),
    path('prendre_test/<int:formation_id>/<int:question_index>', views.prendre_test, name='prendre_test'),
    path('test_termine/<int:formation_id>/', views.test_termine, name='test_termine'),
    path('confirmer_modification/<int:formation_id>/<str:niveau>', views.confirmer_modification, name='confirmer_modification'),

    path('dashboard_apprenant', views.dashboard_apprenant, name='dashboard_apprenant'),
    path('liste_formation', views.liste_formation, name="liste_formation"),
    path('contenu_formation/<int:code>', views.contenu_formation, name='contenu_formation'),
    path('module_apprenant', views.affichageModule, name='module_apprenant'),
    path('evaluation_apprenant', views.interrogations_apprenant , name='evaluation_apprenant'),
    path('voirInterro/<int:code>/<int:question_index>/', views.voirInterro, name='voirInterro'),
    
    path('chat_apprenant', views.chat_apprenant , name='chat_apprenant'),

    path('pdf_preview_recu/<int:code>', views.pdf_preview_recu, name='pdf_preview_recu'),
    path('generate_pdf_recu/<int:code>', views.generate_pdf_recu, name='generate_pdf_recu'),

    path('pdf_preview_certificate/<int:code>', views.pdf_preview_certificate, name='pdf_preview_certificate'),
    path('generate_pdf_certificate/<int:code>', views.generate_pdf_certificate, name='generate_pdf_certificate'),
]
