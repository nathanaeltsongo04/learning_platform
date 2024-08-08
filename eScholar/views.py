import os
from django.conf import settings
from django.shortcuts import render, redirect,get_object_or_404
from django.http import Http404, HttpResponse, JsonResponse
from django.contrib import messages
from django.shortcuts import render
from .models import *
# Create your views here.

def index(request):
    return render(request, 'index.html')

<<<<<<< HEAD
def video_conference(request):
    return render(request, 'video_conference.html')

def authentification(request):
    return render(request,'authentification.html')

def creer_compte(request):
    return render(request,'creer_compte.html')

def profile(request):
    return render(request,'profile.html')
=======
def test(request):
    try:
      test = Test.objects.all()
      context = {'tests':test}
    except:
      print('An exception occurred')
    return render(request,'Test.html', context)
>>>>>>> jean-louis

def dashboard_apprenant(request):
    return render(request, 'apprenant/dashboard.html')

def formation_apprenant(request):
    return render(request,'apprenant/formation.html')

def ressource_apprenant(request):
    try:
        type = TypeRessource.objects.all()
        ressource = Ressource.objects.all()
        context = {'ressources':ressource, 'types':type}
    except:
        messages.error(request, "Une erreur s'est produite lors de l'exécution \n Actualisez la page !")
    return render(request,'apprenant/ressource.html', context)


def chat_apprenant(request):
    return render(request,'apprenant/chat.html')

def horaire_apprenant(request):
    return render(request,'apprenant/horaire.html')

def formation_enseignant(request):
    return render(request,'enseignant/formation.html')

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

def modalitepaiement(request):
    try:
      modalite = ModalitePaie.objects.all()
      module = Module.objects.all()
      context = {'modalitepaies':modalite, 'modules':module}
    except:
        messages.error(request, "Une erreur s'est produite lors de l'exécution \n Actualisez la page !")
    return render(request,'admin/modalitepaiement.html', context)

def niveau(request):
    try:
        niveau = Niveau.objects.all()
        context = {'niveaux':niveau}
    except:
        messages.error("Une erreur s'est produite lors de l'exécution \n Actualisez la page !")
    return render(request,'admin/niveau.html',context)

def paiement(request):
    try:
        paiement = Paiement.objects.all()
        apprenant = Apprenant.objects.all()
        module = Module.objects.all()
        context = {'paiements':paiement, 'apprenants':apprenant, 'modules':module}
    except:
        messages.error("Une erreur s'est produite lors de l'exécution \n Actualisez la page !")
        return redirect('paiement')
    return render(request,'admin/paiement.html', context)

def publication_admin(request):
    return render(request,'admin/publication.html')

def typeressource(request):
    try:
        type = TypeRessource.objects.all()
        context = {'types':type}
    except:
        messages.error(request, "Une erreur s'est produite lors de l'exécution \n Actualisez la page !")
        return redirect('inscription_admin')
    return render(request,'admin/typeressource.html', context)


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
            messages.success(request,"Ajouté avec succès !")
            return redirect('niveau_admin')
    except:
      messages.error(request, "Une erreur s'est produite lors de l'exécution \n Actualisez la page !")
      return redirect('niveau_admin')
    return render(request,'admin/niveau.html')

def updateNiveau(request):
    try:
      if request.method == "POST":
        code = request.POST.get("code")
        designation = request.POST.get("designation")

        if Niveau.objects.filter(designation = designation):
            messages.error(request, "Cette information existe déjà !")
        else:
            Niveau(
                code = code,
                designation = designation
            ).save()
            messages.success(request,"Modifié avec succès !")
            return redirect('niveau_admin')
    except:
      messages.error(request, "Une erreur s'est produite lors de l'exécution \n Actualisez la page !")
      return redirect('niveau_admin')
    return render(request, 'admin/niveau.html')

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
            messages.success(request, "Ajouté avec succès !")
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
            messages.success(request, "Modifié avec succès !")
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
              return redirect('typeressource')
          else:
            TypeRessource.objects.create(
                designation = designation
            )
          messages.success(request,"Ajouté avec succès !")
          return redirect('typeressource')
    except:
      messages.error(request,"Une erreur s'est produite lors de l'exécution \n Actualisez la page !")
      return redirect('typeressource')
    return render(request, "admin/typeressource.html")

def updateTypeRessource(request, code):
    try:
        type_ressource = get_object_or_404(TypeRessource, pk = code)
        context = {'type_ressource':type_ressource}
        
        if request.method == "POST":
            designation = request.POST.get("designation")
            
            if TypeRessource.objects.filter(designation = designation):
                messages.error(request,"Cette information existe déjà !")
            else:
                TypeRessource(
                    code = code,
                    designation = designation
                ).save()
                messages.success(request,"Modifié avec succès !")
    except:
      print('An exception occurred')
    return render(request, "admin/typeRessource.html")

# =======================================================================================================
# RESSOURCE
# =======================================================================================================

def ressource_admin(request):
    try:
        type = TypeRessource.objects.all()
        ressource = Ressource.objects.all()
        context = {'ressources':ressource, 'types':type}
    except:
        messages.error(request, "Une erreur s'est produite lors de l'exécution \n Actualisez la page !")
    return render(request, 'admin/ressource.html', context)

def insertRessource(request):
    try:
      if request.method == "POST":
          titre = request.POST.get("titre")
          description = request.POST.get("description")
          contenu = request.FILES.get("contenu")
          id_type_ressource = request.POST.get("type_ressource")
          
          type_ressource = get_object_or_404(TypeRessource, pk = id_type_ressource)
          
          if Ressource.objects.filter(titre = titre, description = description):
              messages.error(request,"Ces informations existent déjà !")
              return redirect('ressource_admin')
          else:
              Ressource.objects.create(
                  titre = titre,
                  description = description,
                  contenu = contenu,
                  type_ressource = type_ressource
              )
              messages.success(request,"Ressource ajoutée avec succès !")
              return redirect('ressource_admin')
    except:
      messages.error(request,"Une erreur s'est produite lors de l'exécution \n Actualisez la page !")
    return render(request,'admin/ressource.html')

def updateRessource(request):
    try:
      if request.method == "POST":
          code = request.POST.get("code")
          titre = request.POST.get("titre")
          description = request.POST.get("description")
          contenu = request.FILES.get("contenu")
          id_type_ressource = request.POST.get("type_ressource")
          
          type_ressource = get_object_or_404(TypeRessource, pk = id_type_ressource)
          
          if Ressource.objects.filter(titre = titre, description = description, contenu = contenu):
              messages.error(request, "Ces informations existent déjà !")
              return redirect('ressource_admin')
          else:
              if contenu:
                    Ressource(
                        code = code,
                        titre = titre,
                        description = description,
                        contenu = contenu,
                        type_ressource = type_ressource
                    ).save()
                    messages.success(request,"Ressource modifeé avec succès !")
                    return redirect('ressource_admin')
              else:
                    ressource = get_object_or_404(Ressource, pk = code)
                    Ressource(
                        code = code,
                        titre = titre,
                        description = description,
                        contenu = ressource.contenu,
                        type_ressource = type_ressource
                    ).save()
                    messages.success(request,"Ressource modifeé avec succès !")
                    return redirect('ressource_admin')
    except:
      messages.error(request, "Une erreur s'est produite lors de l'exécution \n Actualisez la page !")
      return redirect('ressource_admin')
    return render(request,'admin/ressource.html')

def download_file(request, code):
    uploaded_file = get_object_or_404(Ressource, pk=code)
    file_path = os.path.join(settings.MEDIA_ROOT, uploaded_file.contenu.name)
    if os.path.exists(file_path):
        with open(file_path, 'rb') as f:
            response = HttpResponse(f.read(), content_type='application/pdf')
            response['Content-Disposition'] = f'attachment; filename={uploaded_file.contenu.name}'
            return response
    raise Http404("File does not exist")


# =======================================================================================================
# MODULE
# =======================================================================================================

def module_enseignant(request):
    try:
        module = Module.objects.all()
        niveau = Niveau.objects.all()
        ressource = Ressource.objects.all()
        context = {'modules': module, 'niveaux':niveau, 'ressources':ressource}
    except:
        messages.error(request, "Une erreur s'est produite lors de l'exécution \n Actualisez la page !")
        return redirect('module_enseignant')
    return render(request,'enseignant/module.html', context)

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
            return redirect('module_enseignant')
        else:
            Module.objects.create(
                titre = titre,
                description = description,
                prix = prix,
                niveau = niveau,
                ressource = ressource
            )
            messages.success(request,"Module ajouté avec succès !")
            return redirect('module_enseignant')
    except:
      messages.error(request, "Une erreur s'est produite lors de l'exécution \n Actualisez la page !")
      return redirect('module_enseignant')
    return render(request,"ensignant/module.html")

def updateModule(request):
    try:
      if request.method == "POST":
            code = request.POST.get("code")
            titre = request.POST.get("titre")
            description = request.POST.get("description")
            prix = request.POST.get("prix")
            id_niveau = request.POST.get("niveau")
            id_ressource = request.POST.get("ressource")
            
            niveau = get_object_or_404(Niveau, pk = id_niveau)
            ressource = get_object_or_404(Ressource, pk = id_ressource)
            
            if Module.objects.filter(titre = titre, description = description, prix = prix, niveau = niveau, ressource = ressource):
                messages.error(request, "Ce module existe déjà !")
                return redirect('module_enseignant')
            else:
                Module(
                    code = code,
                    titre = titre,
                    description = description,
                    prix = prix,
                    niveau = niveau,
                    ressource = ressource
                ).save()
                messages.success(request, "Module modifié avec succès !")
                return redirect('module_enseignant')
    except:
      messages.error(request, "Une erreur s'est produite lors de l'exécution \n Actualisez la page !")
      return redirect('module_enseignant')
    return render(request,"enseignant/module.html")

# =======================================================================================================
# FORMATION
# =======================================================================================================

def formation_admin(request):
    try:
      formation = Formation.objects.all()
      module = Module.objects.all()
      enseignant = Enseignant.objects.all()
      domaine = Domaine.objects.all()
      context = {'formations':formation, 'enseignants':enseignant, 'modules':module, 'domaines':domaine}
    except:
        messages.success(request,"Formation ajoutée avec succès !")
        return redirect('formation_admin')    
    return render(request,'admin/formation.html', context)

def insertFormation(request):
    try:
      if request.method == "POST":
          titre = request.POST.get("titre")
          description = request.POST.get("description")
          duree = request.POST.get("duree")
          date_debut = request.POST.get("date_debut")
          date_fin = request.POST.get("date_fin")
          id_domaine = request.POST.get("domaine")
          id_module = request.POST.get("module")
          id_enseignant = request.POST.get("enseignant")
          
          module = get_object_or_404(Module, pk = id_module)
          enseignant = get_object_or_404(Enseignant, pk = id_enseignant)
          domaine = get_object_or_404(Domaine, pk = id_domaine)
          
          if Formation.objects.filter(
                                titre = titre,
                                duree = duree,
                                date_debut = date_debut,
                                date_fin = date_fin,
                                module = module,
                                enseignant = enseignant
                            ):
              messages.info(request, "Ces information existent déjà !")
              return redirect('formation_admin')
          else:
            Formation.objects.create(
                titre = titre,
                duree = duree,
                description = description,
                date_debut = date_debut,
                date_fin = date_fin,
                module = module,
                enseignant = enseignant,
                domaine = domaine
            )
            messages.success(request,"Formation ajoutée avec succès !")
            return redirect('formation_admin')
    except:
      messages.error(request, "Une erreur s'est produite lors de l'exécution \n Actualisez la page !")
      return redirect('formation_admin')
    return render(request,'admin/formation.html')

def updateFormation(request):
    try:
      if request.method == "POST":
          code = request.POST.get("code")
          titre = request.POST.get("titre")
          description = request.POST.get("description")
          duree = request.POST.get("duree")
          date_debut = request.POST.get("date_debut")
          date_fin = request.POST.get("date_fin")
          id_domaine = request.POST.get("domaine")
          id_module = request.POST.get("module")
          id_enseignant = request.POST.get("enseignant")
          
          module = get_object_or_404(Module, pk = id_module)
          enseignant = get_object_or_404(Enseignant, pk = id_enseignant)
          domaine = get_object_or_404(Domaine, pk = id_domaine)
          
          if Formation.objects.filter(
                                titre = titre,
                                duree = duree,
                                date_debut = date_debut,
                                date_fin = date_fin,
                                module = module,
                                enseignant = enseignant
                            ):
              messages.info(request, "Ces information existent déjà !")
              return redirect('formation_admin')
          else:
              Formation(
                    code = code,
                    titre = titre,
                    description = description,
                    duree = duree,
                    date_debut = date_debut,
                    date_fin = date_fin,
                    module = module,
                    enseignant = enseignant,
                    domaine = domaine
                ).save()
          messages.success(request,"Formation modifiée avec succès !")
          return redirect('formation_admin')
    except:
      messages.error(request, "Une erreur s'est produite lors de l'exécution \n Actualisez la page !")
      return redirect('formation_admin')
    return render(request,'Apprenant/formation.html')

# =======================================================================================================
# MODALITE PAIE
# =======================================================================================================

def insertModalitePaie(request):
    try:
      if request.method == "POST":
          tranche = request.POST.get("tranche")
          montant_fixe = request.POST.get("montant_fixe")
          id_module = request.POST.get("module")
          
          module = get_object_or_404(Module, pk = id_module)
          
          ModalitePaie.objects.create(
              tranche = tranche,
              montant_fixe = montant_fixe,
              module = module
          )
          messages.success(request,"Ajouté avec succès !")
          return redirect('modalite_paiement')
    except:
      messages.error(request, "Une erreur s'est produite lors de l'exécution \n Actualisez la page !")
      return redirect('modalite_paiement')
    return render(request,'Admin/modalitepaiement.html')

def updateModalitePaie(request):
    try:
      if request.method == "POST":
          code = request.POST.get("code")
          tranche = request.POST.get("tranche")
          montant_fixe = request.POST.get("montant_fixe")
          id_module = request.POST.get("module")
          
          module = get_object_or_404(Module, pk = id_module)
          
          ModalitePaie(
              code = code,
              tranche = tranche,
              montant_fixe = montant_fixe,
              module = module
          ).save()
          messages.success(request,"Modifié avec succès !")
          return redirect('modalite_paiement')
    except:
      messages.error(request, "Une erreur s'est produite lors de l'exécution \n Actualisez la page !")
      return redirect('modalite_paiement')
    return render(request,'Admin/modalitepaiement.html')

# =======================================================================================================
# INSCRIPTION
# =======================================================================================================

def inscription_admin(request):
    try:
      inscription = Inscription.objects.all()
      apprenant = Apprenant.objects.all()
      formation = Formation.objects.all()
      modalite = ModalitePaie.objects.all()
      context = {'inscriptions':inscription, 'apprenants':apprenant, 'modalites':modalite, 'formations':formation}
    except:
      messages.error(request, "Une erreur s'est produite lors de l'exécution \n Actualisez la page !")
      return redirect('inscription_admin')
    return render(request, "admin/inscription.html", context)

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
          messages.success(request, "Inscription éffectuée avec succès !")
          return redirect('inscription_admin')
    except:
      messages.error(request, "Une erreur s'est produite lors de l'exécution \n Actualisez la page !")
      return redirect('inscription_admin')
    return render(request, 'admin/inscription.html')

def updateInscription(request):
    try:
      if request.method == "POST":
          code = request.POST.get("code")
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
          messages.success(request, "Inscription modifiée avec succès !")
    except:
      messages.error(request, "Une erreur s'est produite lors de l'exécution \n Actualisez la page !")
      return redirect('inscription_admin')
    return render(request, 'admin/inscription.html')

# =======================================================================================================
# EVALUATION
# =======================================================================================================

def evaluation(request):
    try:
        evaluation = Evaluation.objects.all()
        formation = Formation.objects.all()
        context = {'evaluations':evaluation, 'formations':formation}
    except:
        messages.error(request, "Une erreur s'est produite lors de l'exécution \n Actualisez la page !")
        return redirect('evaluation')    
    return render(request, "enseignant/interrogation.html", context)

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
          messages.success(request, "Résultat de l'évaluation inseré avec succès !")
          return redirect('evaluation')
    except:
      messages.error(request, "Une erreur s'est produite lors de l'exécution \n Actualisez la page !")
      return redirect('evaluation')
    return render(request, "enseignant/interrogation.html")

def updateEvaluation(request):
    try:
      if request.method == "POST":
          code = request.POST.get("code")
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
          messages.success(request, "Résultat de l'évaluation modifié avec succès !")
          return redirect('evaluation')
    except:
      messages.error(request, "Une erreur s'est produite lors de l'exécution \n Actualisez la page !")
      return redirect('evaluation')
    return render(request, "enseignant/interrogation.html")

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
          id_apprenant = request.POST.get("apprenant")
          id_module = request.POST.get("module")
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
          messages.success(request, "Paiement éffectué avec succès !")
          return redirect('paiement')
    except:
      messages.error("Une erreur s'est produite lors de l'exécution \n Actualisez la page !")
      return redirect('paiement')
    return render(request,'admin/paiement.html')

def updatePaiement(request):
    try:
      if request.method == "POST":
          code = request.POST.get("code")
          id_apprenant = request.POST.get("apprenant")
          id_module = request.POST.get("module")
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
          messages.success(request, "Paiement modifié avec succès !")
          return redirect('paiement')
    except:
      messages.error(request, "Une erreur s'est produite lors de l'exécution \n Actualisez la page !")
      return redirect('paiement')
    return render(request,'admin/paiement.html')

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