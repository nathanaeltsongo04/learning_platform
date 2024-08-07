from django.shortcuts import render, redirect,get_object_or_404
from django.http import HttpResponse, JsonResponse
from django.contrib import messages
from .models import *
# Create your views here.

def index(request):
    return render(request, 'index.html')

def test(request):
    try:
      test = Test.objects.all()
      context = {'tests':test}
    except:
      print('An exception occurred')
    return render(request,'Test.html', context)

def dashboard_apprenant(request):
    return render(request, 'apprenant/dashboard.html')

def formation_apprenant(request):
    return render(request,'apprenant/formation.html')

def ressource_apprenant(request):
    return render(request,'apprenant/ressource.html')

def chat_apprenant(request):
    return render(request,'apprenant/chat.html')

def horaire_apprenant(request):
    return render(request,'apprenant/horaire.html')

def formation_enseignant(request):
    return render(request,'enseignant/formation.html')

def module_enseignant(request):
    return render(request,'enseignant/module.html')

def interrogation_enseignant(request):
    return render(request,'enseignant/interrogation.html')

def cote_enseignant(request):
    return render(request,'enseignant/cote.html')

def correction_enseignant(request):
    return render(request,'enseignant/correction.html')

def dashboard_enseignant(request):
    return render(request,'enseignant/dashboard.html')

def publication_enseignant(request):
    return render(request,'enseignant/publication.html')

def dashboard_admin(request):
    return render(request,'admin/dashboard.html')

def domaine_admin(request):
    try:
        domaine = Domaine.objects.all()
        context = {'domaines':domaine}
    except:
        messages.error(request, "Une erreur s'est produite lors de l'exécution \n Actualisez la page !")
    return render(request,'admin/domaine.html', context)

def formation_admin(request):
    return render(request,'admin/formation.html')

def modalitepaiement(request):
    return render(request,'admin/modalitepaiement.html')

def niveau(request):
    return render(request,'admin/niveau.html')

def paiement(request):
    return render(request,'admin/paiement.html')

def publication_admin(request):
    return render(request,'admin/publication.html')

def typeressource(request):
    return render(request,'admin/typeressource.html')


# =======================================================================================================
# NIVEAU
# =======================================================================================================

def insertNiveau(request):
    try:
      if request.method == "POST":
        designation = request.POST.get("designation")

        if Niveau.objects.filter(designation = designation):
            messages.error(request, "Cette information existe déjà !")
        else:
            Niveau.objects.create(
                designation = designation
            )
            messages.success(request, "Ajouté avec succès !")
    except:
      messages.error(request, "Une erreur s'est produite lors de l'exécution \n Actualisez la page !")
    return HttpResponse("Ajouté avec succès")

def updateNiveau(request, code):
    try:
      niveau = get_object_or_404(Niveau, pk = code)
      context = {'niveau':niveau}
      
      if request.method == "POST":
        designation = request.POST.get("designation")

        if Niveau.objects.filter(designation = designation):
            messages.error(request, request, "Cette information existe déjà !")
        else:
            Niveau(
                code = code,
                designation = designation
            ).save()
            messages.success(request, request, "Modifié avec succès !")
    except:
      messages.error(request, request, "Une erreur s'est produite lors de l'exécution \n Actualisez la page !")
    return HttpResponse("Modifié avec succès")

# =======================================================================================================
# DOMAINE
# =======================================================================================================

def insertDomaine(request):
    try:
      if request.method == "POST":
        designation = request.POST.get("designation")

        if Domaine.objects.filter(designation = designation):
            messages.error(request, "Cette information existe déjà !")
        else:
            Domaine.objects.create(
                designation = designation
            )
            messages.success(request, request, "Ajouté avec succès !")
            return redirect('domaine_admin')
    except:
      messages.error(request, "Une erreur s'est produite lors de l'exécution \n Actualisez la page !")
    return render(request, 'admin/domaine.html')

def updateDomaine(request):
    try:
      if request.method == "POST":
        code = request.POST.get("code")
        designation = request.POST.get("designation")
        
        if Domaine.objects.filter(designation = designation):
            messages.error(request, "Cette information existe déjà !")
        else:
            Domaine(
                code = code,
                designation = designation
            ).save()
            messages.success(request, request, "Modifié avec succès !")
            return redirect("domaine_admin")
    except:
      messages.error(request, "Une erreur s'est produite lors de l'exécution \n Actualisez la page !")
    return render(request, 'chargement_modal/domaine.html')


# =======================================================================================================
# APPRENANT
# =======================================================================================================

def apprenant_admin(request):
    try:
      apprenant = Apprenant.objects.all()
      context = {'apprenants':apprenant}
    except:
      messages.error(request, "Une erreur s'est produite lors de l'exécution \n Actualisez la page !")
    return render(request,'admin/apprenant.html', context)

def insertApprenant(request):
    try:
      if request.method == "POST":
        nom = request.POST.get("nom")
        postnom = request.POST.get("postnom")
        prenom = request.POST.get("prenom")
        genre = request.POST.get("genre")
        etatcivil = request.POST.get("etatcivil")
        addresse = request.POST.get("addresse")
        contact = request.POST.get("contact")
        profession = request.POST.get("profession")
        photo = request.FILES.get("photo")
        
        if Apprenant.objects.filter(nom = nom, postnom = postnom, prenom = prenom):
            messages.error(request, "L'apprenant existe déjà !")
            return redirect('apprenant_admin')
        else:
            Apprenant.objects.create(
                nom = nom,
                postnom = postnom,
                prenom = prenom,
                genre = genre,
                etatcivil = etatcivil,
                addresse = addresse,
                contact = contact,
                profession = profession,
                photo = photo
            )
            messages.success(request, "Apprenant ajouté avec succès !")
            return redirect('apprenant_admin')
    except:
      messages.error(request, "Une erreur s'est produite lors de l'exécution \n Actualisez la page !")
      return redirect('apprenant_admin')
    return render(request,'admin/apprenant.html')

def updateApprenant(request):
    try:
      if request.method == "POST":
        matricule = request.POST.get("matricule")
        nom = request.POST.get("nom")
        postnom = request.POST.get("postnom")
        prenom = request.POST.get("prenom")
        genre = request.POST.get("genre")
        etatcivil = request.POST.get("etatcivil")
        addresse = request.POST.get("addresse")
        contact = request.POST.get("contact")
        profession = request.POST.get("profession")
        photo = request.FILES.get("photo")
        
        if Apprenant.objects.filter(nom = nom, postnom = postnom, prenom = prenom, genre = genre, etatcivil = etatcivil, addresse = addresse, contact = contact, profession = profession):
                messages.info(request, "Ces informations existent déjà !")
                return redirect('apprenant_admin')
        else:
            if photo:
                Apprenant(
                    matricule = matricule,
                    nom = nom,
                    postnom = postnom,
                    prenom = prenom,
                    genre = genre,
                    etatcivil = etatcivil,
                    addresse = addresse,
                    contact = contact,
                    profession = profession,
                    photo = photo
                ).save()
                messages.success(request, "La modification a été appliquée avec succés !")
                return redirect('apprenant_admin')
            else:
                apprenant = get_object_or_404(Apprenant, pk = matricule)
                Apprenant(
                    matricule = matricule,
                    nom = nom,
                    postnom = postnom,
                    prenom = prenom,
                    genre = genre,
                    etatcivil = etatcivil,
                    addresse = addresse,
                    contact = contact,
                    profession = profession,
                    photo = apprenant.photo
                ).save()
                messages.success(request, "La modification a été appliquée avec succés !")
                return redirect('apprenant_admin')
    except:
      messages.error(request, "Une erreur s'est produite lors de l'exécution \n Actualisez la page !")
      return redirect('apprenant_admin')
    return render(request,'admin/apprenant.html')

# =======================================================================================================
# ENSEIGNANT
# =======================================================================================================

def enseignant_admin(request):
    try:
      enseignant = Enseignant.objects.all()
      context = {'enseignants':enseignant}
    except:
      messages.error(request, "Une erreur s'est produite lors de l'exécution \n Actualisez la page !")
      return redirect('apprenant_admin')
    return render(request,'admin/enseignant.html', context)

def insertEnseignant(request):
    try:
      if request.method == "POST":
        nom = request.POST.get("nom")
        postnom = request.POST.get("postnom")
        prenom = request.POST.get("prenom")
        genre = request.POST.get("genre")
        etatcivil = request.POST.get("etatcivil")
        addresse = request.POST.get("addresse")
        contact = request.POST.get("contact")
        profession = request.POST.get("profession")
        photo = request.FILES.get("photo")
        
        if Enseignant.objects.filter(nom = nom, postnom = postnom, prenom = prenom):
            messages.error(request, "L'enseignant existe déjà !")
        else:
            Enseignant.objects.create(
                nom = nom,
                postnom = postnom,
                prenom = prenom,
                genre = genre,
                etatcivil = etatcivil,
                addresse = addresse,
                contact = contact,
                profession = profession,
                photo = photo
            )
            messages.success(request, "Enseignant ajouté avec succès !")
            return redirect('enseignant_admin')
    except:
      messages.error(request, "Une erreur s'est produite lors de l'exécution \n Actualisez la page !")
      return redirect('enseignant_admin')
    return render(request,'admin/enseignant.html')

def updateEnseignant(request):
    try:
        if request.method == "POST":
            matricule = request.POST.get("matricule")
            nom = request.POST.get("nom")
            postnom = request.POST.get("postnom")
            prenom = request.POST.get("prenom")
            genre = request.POST.get("genre")
            etatcivil = request.POST.get("etatcivil")
            addresse = request.POST.get("addresse")
            contact = request.POST.get("contact")
            profession = request.POST.get("profession")
            photo = request.FILES.get("photo")
            
            if Enseignant.objects.filter(nom = nom, postnom = postnom, prenom = prenom, genre = genre, etatcivil = etatcivil, addresse = addresse, contact = contact,profession = profession):
                    messages.info(request, "Ces informations existent déjà !")
                    return redirect('enseignant_admin')
            else:
                if photo:
                    Enseignant(
                            matricule = matricule,
                            nom = nom,
                            postnom = postnom,
                            prenom = prenom,
                            genre = genre,
                            etatcivil = etatcivil,
                            addresse = addresse,
                            contact = contact,
                            profession = profession,
                            photo = photo
                    ).save()
                    messages.success(request, "La modification a été appliquée avec succés !")
                    return redirect('enseignant_admin')
                else:
                    enseignant = get_object_or_404(Enseignant, pk = matricule)
                    Enseignant(
                            matricule = matricule,
                            nom = nom,
                            postnom = postnom,
                            prenom = prenom,
                            genre = genre,
                            etatcivil = etatcivil,
                            addresse = addresse,
                            contact = contact,
                            profession = profession,
                            photo = enseignant.photo
                    ).save()
                    messages.success(request, "La modification a été appliquée avec succés !")
                    return redirect('enseignant_admin')
    except:
      messages.error(request, "Une erreur s'est produite lors de l'exécution \n Actualisez la page !")
      return redirect('enseignant_admin')
    return render(request,'admin/enseignant.html')

# =======================================================================================================
# TYPE RESSOURCE
# =======================================================================================================

def insertTypeRessource(request):
    try:
      if request.method == "POST":
          designation = request.POST.get("designation")
          
          if TypeRessource.objects.filter(designation = designation):
              messages.error(request, "Cette information existe déjà !")
          else:
            TypeRessource.objects.create(
                designation = designation
            )
          messages.success(request, "Ajouté avec succès !")
    except:
      messages.error(request, "Une erreur s'est produite lors de l'exécution \n Actualisez la page !")
    return HttpResponse("Ajouté avec succès")

def updateRessource(request, code):
    try:
        type_ressource = get_object_or_404(TypeRessource, pk = code)
        context = {'type_ressource':type_ressource}
        
        if request.method == "POST":
            designation = request.POST.get("designation")
            
            if TypeRessource.objects.filter(designation = designation):
                messages.error("Cette information existe déjà !")
            else:
                TypeRessource(
                    code = code,
                    designation = designation
                ).save()
                messages.success("Modifié avec succès !")
    except:
      print('An exception occurred')
    return HttpResponse("Modifié avec succès")

# =======================================================================================================
# RESSOURCE
# =======================================================================================================

def insertRessource(request):
    try:
      if request.method == "POST":
          titre = request.POST.get("titre")
          description = request.POST.get("description")
          contenu = request.POST.get("contenu")
          id_type_ressource = request.POST.get("type_ressource")
          
          type_ressource = get_object_or_404(TypeRessource, pk = id_type_ressource)
          
          if Ressource.objects.filter(titre = titre, description = description):
              messages.error("Ces informations existent déjà !")
          else:
              Ressource.objects.create(
                  titre = titre,
                  description = description,
                  contenu = contenu,
                  type_ressource = type_ressource
              )
              messages.success("Ressource ajoutée avec succès !")
    except:
      messages.error("Une erreur s'est produite lors de l'exécution \n Actualisez la page !")
    return HttpResponse("Ajouté avec succès")

def updateRessource(request, code):
    try:
      ressource = get_object_or_404(Ressource, pk = code)
      context = {'ressource':ressource}
      
      if request.method == "POST":
          titre = request.POST.get("titre")
          description = request.POST.get("description")
          contenu = request.POST.get("contenu")
          id_type_ressource = request.POST.get("type_ressource")
          
          type_ressource = get_object_or_404(TypeRessource, pk = id_type_ressource)
          
          if Ressource.objects.filter(titre = titre, description = description):
              messages.error("Ces informations existent déjà !")
          else:
              Ressource(
                  code = code,
                  titre = titre,
                  description = description,
                  contenu = contenu,
                  type_ressource = type_ressource
              ).save()
              messages.success("Ressource modifeé avec succès !")
    except:
      messages.error("Une erreur s'est produite lors de l'exécution \n Actualisez la page !")
    return HttpResponse("Modifié avec succès")

# =======================================================================================================
# MODULE
# =======================================================================================================
def insertModule(request):
    try:
      if request.method == "POST":
        titre = request.POST.get("titre")
        description = request.POST.get("description")
        prix = request.POST.get("prix")
        id_niveau = request.POST.get("niveau")
        id_ressource = request.POST.get("ressource")
        
        niveau = get_object_or_404(Niveau, pk = id_niveau)
        ressource = get_object_or_404(Ressource, pk = id_ressource)
        
        if Module.objects.filter(titre = titre, description = description):
            messages.error("Ce module eisxte déjà !")
        else:
            Module.objects.create(
                titre = titre,
                description = description,
                prix = prix,
                niveau = niveau,
                ressource = ressource
            )
            messages.success("Module ajouté avec succès !")
    except:
      messages.error("Une erreur s'est produite lors de l'exécution \n Actualisez la page !")
    return HttpResponse("Ajouté avec succès")

def updateModule(request, code):
    try:
      module = get_object_or_404(Module, pk = code)
      context = {'module':module}
      
      if request.method == "POST":
            titre = request.POST.get("titre")
            description = request.POST.get("description")
            prix = request.POST.get("prix")
            id_niveau = request.POST.get("niveau")
            id_ressource = request.POST.get("ressource")
            
            niveau = get_object_or_404(Niveau, pk = id_niveau)
            ressource = get_object_or_404(Ressource, pk = id_ressource)
            
            if Module.objects.filter(titre = titre, description = description):
                messages.error("Ce module eisxte déjà !")
            else:
                Module(
                    code = code,
                    titre = titre,
                    description = description,
                    prix = prix,
                    niveau = niveau,
                    ressource = ressource
                ).save()
                messages.success("Module modifié avec succès !")
    except:
      messages.error("Une erreur s'est produite lors de l'exécution \n Actualisez la page !")
    return HttpResponse("Modifié avec succès !")

# =======================================================================================================
# FORMATION
# =======================================================================================================
def insertFormation(request):
    try:
      if request.method == "POST":
          titre = request.POST.get("titre")
          duree = request.POST.get("duree")
          date_debut = request.POST.get("date_debut")
          date_fin = request.POST.get("date_fin")
          id_module = request.POST.get("module")
          id_enseignant = request.POST.get("enseignant")
          
          module = get_object_or_404(Module, pk = id_module)
          enseignant = get_object_or_404(Enseignant, pk = id_enseignant)
          
          Formation.objects.create(
              titre = titre,
              duree = duree,
              date_debut = date_debut,
              date_fin = date_fin,
              module = module,
              enseignant = enseignant
          )
          messages.success("Formation ajoutée avec succès !")
    except:
      messages.error("Une erreur s'est produite lors de l'exécution \n Actualisez la page !")
    return HttpResponse("Ajouté avec succès !")

def updateFormation(request, code):
    try:
      formation = get_object_or_404(Formation, pk = code)
      context = {'formation':formation}
      
      if request.method == "POST":
          titre = request.POST.get("titre")
          duree = request.POST.get("duree")
          date_debut = request.POST.get("date_debut")
          date_fin = request.POST.get("date_fin")
          id_module = request.POST.get("module")
          id_enseignant = request.POST.get("enseignant")
          
          module = get_object_or_404(Module, pk = id_module)
          enseignant = get_object_or_404(Enseignant, pk = id_enseignant)
          
          if Formation.objects.filter(
                                titre = titre,
                                duree = duree,
                                date_debut = date_debut,
                                date_fin = date_fin,
                                module = module,
                                enseignant = enseignant
                            ):
              messages.info("Ces information existent déjà !")
          else:
              Formation(
                    titre = titre,
                    duree = duree,
                    date_debut = date_debut,
                    date_fin = date_fin,
                    module = module,
                    enseignant = enseignant
                ).save()
          messages.success("Formation modifiée avec succès !")
    except:
      messages.error("Une erreur s'est produite lors de l'exécution \n Actualisez la page !")
    return HttpResponse("Modifiée avec succès")

# =======================================================================================================
# MODALITE PAIE
# =======================================================================================================

def insertModalitePaie(request):
    try:
      if request.method == "POST":
          tranche = request.POST.get("tranche")
          montant_fixe = request.POST.get("montant_fixe")
          id_module = request.POST.get("id_module")
          
          module = get_object_or_404(Module, pk = id_module)
          
          ModalitePaie.objects.create(
              tranche = tranche,
              montant_fixe = montant_fixe,
              module = module
          )
          messages.success("Ajouté avec succès !")
    except:
      messages.error("Une erreur s'est produite lors de l'exécution \n Actualisez la page !")
    return HttpResponse("Ajouté avec succès !")

def updateModulePaie(request, code):
    try:
      modalitepaie = get_object_or_404(ModalitePaie, pk = code)
      context = {'modalitepaie': modalitepaie}
      
      if request.method == "POST":
          tranche = request.POST.get("tranche")
          montant_fixe = request.POST.get("montant_fixe")
          id_module = request.POST.get("id_module")
          
          module = get_object_or_404(Module, pk = id_module)
          
          ModalitePaie(
              code = code,
              tranche = tranche,
              montant_fixe = montant_fixe,
              module = module
          ).save()
          messages.success("Modifié avec succès !")
    except:
      messages.error("Une erreur s'est produite lors de l'exécution \n Actualisez la page !")
    return HttpResponse("Modifié avec succès !")

# =======================================================================================================
# INSCRIPTION
# =======================================================================================================

def insertInscription(request):
    try:
      if request.method == "POST":
          id_apprenant = request.POST.get("apprenant")
          id_formation = request.POST.get("formation")
          id_modalite = request.POST.get("modalite")
          date_inscription = request.POST.get("date_inscription")
          
          apprenant = get_object_or_404(Apprenant, pk = id_apprenant)
          formation = get_object_or_404(Formation, pk = id_formation)
          modalite = get_object_or_404(ModalitePaie, pk = id_modalite)
          
          Inscription.objects.create(
              apprenant = apprenant,
              formation = formation,
              modalite = modalite,
              date_inscription = date_inscription
          )
          messages.success("Inscription éffectuée avec succès !")
    except:
      messages.error("Une erreur s'est produite lors de l'exécution \n Actualisez la page !")
    return HttpResponse("Inscription éffectuée avec succès !")

def updateInscription(request, code):
    try:
      inscription = get_object_or_404(Inscription, pk = code)
      context = {'inscription' : inscription}
      
      if request.method == "POST":
          id_apprenant = request.POST.get("apprenant")
          id_formation = request.POST.get("formation")
          id_modalite = request.POST.get("modalite")
          date_inscription = request.POST.get("date_inscription")
          
          apprenant = get_object_or_404(Apprenant, pk = id_apprenant)
          formation = get_object_or_404(Formation, pk = id_formation)
          modalite = get_object_or_404(ModalitePaie, pk = id_modalite)
          
          Inscription(
              code = code,
              apprenant = apprenant,
              formation = formation,
              modalite = modalite,
              date_inscription = date_inscription
          ).save()
          messages.success("Inscription modifiée avec succès !")
    except:
      messages.error("Une erreur s'est produite lors de l'exécution \n Actualisez la page !")
    return HttpResponse("Inscription modifiée avec succès !")

# =======================================================================================================
# EVALUATION
# =======================================================================================================

def insertEvaluation(request):
    try:
      if request.method == "POST":
          id_formation = request.POST.get("formation")
          maximum = request.POST.get("maximum")
          cote = request.POST.get("cote")
          date_evaluation = request.POST.get("date_evaluation")
          
          formation = get_object_or_404(Formation, pk = id_formation)
          
          Evaluation.objects.create(
              formation = formation,
              maximum = maximum,
              cote = cote,
              date_evaluation = date_evaluation
          )
          messages.success("Résultat de l'évaluation inseré avec succès !")
    except:
      messages.error("Une erreur s'est produite lors de l'exécution \n Actualisez la page !")
    return HttpResponse("Résultat de l'évaluation inseré avec succès !")

def updateEvaluation(request, code):
    try:
      evaluation = get_object_or_404(Evaluation, pk = code)
      context = {'evaluation' : evaluation}
      
      if request.method == "POST":
          id_formation = request.POST.get("formation")
          maximum = request.POST.get("maximum")
          cote = request.POST.get("cote")
          date_evaluation = request.POST.get("date_evaluation")
          
          formation = get_object_or_404(Formation, pk = id_formation)
          
          Evaluation(
              code = code,
              formation = formation,
              maximum = maximum,
              cote = cote,
              date_evaluation = date_evaluation
          ).save()
          messages.success("Résultat de l'évaluation modifié avec succès !")
    except:
      messages.error("Une erreur s'est produite lors de l'exécution \n Actualisez la page !")
    return HttpResponse("Modifié avec succès !")

# =======================================================================================================
# PUBLICATION
# =======================================================================================================

def insertPublication(request):
    try:
      if request.method == "POST":
          titre = request.POST.get("titre")
          description = request.POST.get("description")
        #   id_compte_utilisateur = request.POST.get("compte_utilisateur")
          date_publication = request.POST.get("date_publication")
          
        #   compte_utilisateur = get_object_or_404(User, pk = id_compte_utilisateur)
          
          if Publication.objects.filter(titre = titre, description = description): #compte_utilisateur = compte_utilisateur
              messages.warning("Ces informations existent déjà !")
          else:
              Publication.objects.create(
                  titre = titre,
                  description = description,
                #   compte_utilisateur = compte_utilisateur,
                date_publication = date_publication
              )
              messages.success("Publication ajoutée avec succès !")
    except:
      messages.error("Une erreur s'est produite lors de l'exécution \n Actualisez la page !")
    return HttpResponse("Ajouté avec succès !")

def updatePublication(request, code):
    try:
      publication = get_object_or_404(Publication, pk = code)
      context = {'publication' : publication}
      
      if request.method == "POST":
          titre = request.POST.get("titre")
          description = request.POST.get("description")
        #   id_compte_utilisateur = request.POST.get("compte_utilisateur")
          date_publication = request.POST.get("date_publication")
          
        #   compte_utilisateur = get_object_or_404(User, pk = id_compte_utilisateur)
          
          if Publication.objects.filter(titre = titre, description = description): #compte_utilisateur = compte_utilisateur
              messages.warning("Ces informations existent déjà !")
          else:
              Publication(
                  code = code,
                  titre = titre,
                  description = description,
                #   compte_utilisateur = compte_utilisateur,
                date_publication = date_publication
              ).save()
              messages.success("Publication modifiée avec succès !")
    except:
      messages.error("Une erreur s'est produite lors de l'exécution \n Actualisez la page !")
    return HttpResponse("Modifiée avec succès !")

# =======================================================================================================
# PAIEMENT
# =======================================================================================================

def insertPaiement(request):
    try:
      if request.method == "POST":
          id_apprenant = request.POST.get("id_apprenant")
          id_module = request.POST.get("id_module")
          montant = request.POST.get("montant")
          date_paiement = request.POST.get("date_paiement")
          
          apprenant = get_object_or_404(Apprenant, pk = id_apprenant)
          module = get_object_or_404(Module, pk = id_module)
          
          Paiement.objects.create(
              apprenant = apprenant,
              module = module,
              montant = montant,
              date_paiement = date_paiement
          )
          messages.success("Paiement éffectué avec succès !")
    except:
      messages.error("Une erreur s'est produite lors de l'exécution \n Actualisez la page !")
    return HttpResponse("Effectué avec succès !")

def updatePaiement(request, code):
    try:
      paiement = get_object_or_404(Paiement, pk = code)
      context = {'paiement' : paiement}
      
      if request.method == "POST":
          id_apprenant = request.POST.get("id_apprenant")
          id_module = request.POST.get("id_module")
          montant = request.POST.get("montant")
          date_paiement = request.POST.get("date_paiement")
          
          apprenant = get_object_or_404(Apprenant, pk = id_apprenant)
          module = get_object_or_404(Module, pk = id_module)
          
          Paiement(
              code = code,
              apprenant = apprenant,
              module = module,
              montant = montant,
              date_paiement = date_paiement
          ).save()
          messages.success("Paiement modifié avec succès !")
    except:
      messages.error("Une erreur s'est produite lors de l'exécution \n Actualisez la page !")
    return HttpResponse("Modifié avec succès !")

# =======================================================================================================
# QUESTIONNAIRE
# =======================================================================================================

def insertQuestionnaire(request):
    try:
      if request.method == "POST":
          id_module = request.POST.get("id_module")
          question = request.POST.get("question")
          reponse = request.POST.get("reponse")
          
          module = get_object_or_404(Module, pk = id_module)
          
          if Questionnaire.objects.filter(module = module, question = question, reponse = reponse):
              messages.warning("Ces informations existent déjà !")
          else:
              Questionnaire.objects.create(
                  module = module,
                  question = question,
                  reponse = reponse
              )
              messages.success("Ajouté avec succès !")
    except:
      messages.error("Une erreur s'est produite lors de l'exécution \n Actualisez la page !")
    return HttpResponse("Ajouté avec succès !")

def updateQuestionnaire(request, code):
    try:
      questionnaire = get_object_or_404(Questionnaire, pk = code)
      context = {'questionnaire' : questionnaire}
      
      if request.method == "POST":
          id_module = request.POST.get("id_module")
          question = request.POST.get("question")
          reponse = request.POST.get("reponse")
          
          module = get_object_or_404(Module, pk = id_module)
          
          if Questionnaire.objects.filter(module = module, question = question, reponse = reponse):
              messages.warning("Ces informations existent déjà !")
          else:
              Questionnaire.objects.create(
                  module = module,
                  question = question,
                  reponse = reponse
              )
              messages.success("Modifié avec succès !")
    except:
      messages.error("Une erreur s'est produite lors de l'exécution \n Actualisez la page !")
    return HttpResponse("Modifié avec succès !")

# =======================================================================================================
# TEST
# =======================================================================================================

def insertTest(request):
    try:
      if request.method == "POST":
          id_apprenant = request.POST.get("id_apprenant")
          id_questionnaire = request.POST.get("id_questionnaire")
          reponse = request.POST.get("reponse")
          
          apprenant = get_object_or_404(Apprenant, pk = id_apprenant)
          questionnaire = get_object_or_404(Questionnaire, pk = id_questionnaire)
          
          Test.objects.create(
              apprenant = apprenant,
              questionnaire = questionnaire,
              reponse = reponse
          )
          messages.success("Ajouté avec succès !")
    except:
      print('An exception occurred')
    return HttpResponse("Ajouté avec succès !")