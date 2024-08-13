import os
from django.conf import settings
from django.shortcuts import render, redirect,get_object_or_404
from django.http import Http404, HttpResponse, JsonResponse, HttpResponseRedirect
from django.urls import reverse
from django.contrib import messages
from .models import *
from django.contrib.auth import authenticate, login, logout
import random
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
    try:
        publications = Publication.objects.all()
        total_publications = publications.count()
        total_modules = Module.objects.all().count()
        total_evaluations=Formation.objects.all().count()
        context = {
            'publications': publications, 
            'total_publications':total_publications,
            'total_modules':total_modules,
            'total_evaluations':total_evaluations
            }
    except Exception as e:
        messages.error(request, f"Une erreur s'est produite lors de l'exécution : {str(e)} \n Actualisez la page !")
    return render(request,'apprenant/dashboard.html', context)

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
    try:
        ressources = Ressource.objects.all()
        total_ressources = ressources.count()
        total_publications = Publication.objects.all().count()
        total_modules=Module.objects.all().count()
        context = {
            'ressources': ressources, 
            'total_ressources':total_ressources,
            'total_publications':total_publications,
            'total_modules':total_modules
            }
    except Exception as e:
        messages.error(request, f"Une erreur s'est produite lors de l'exécution : {str(e)} \n Actualisez la page !")
    return render(request,'enseignant/dashboard.html', context)


def publication_enseignant(request):
    return render(request,'enseignant/publication.html')

def authentification(request):
    try:
        if request.method == "POST":
            username = request.POST.get("nomdutilisateur")
            password = request.POST.get("password")

            # Authentification de l'utilisateur
            user = authenticate(request, username=username, password=password)

            if user is not None:
                login(request, user)  # Connexion de l'utilisateur
                messages.success(request, f"Bienvenue, {user.username}!")
                return redirect('rediriger_apprenant')  # Redirige vers la page d'accueil ou une autre page sécurisée
            else:
                messages.warning(request, "Nom d'utilisateur ou mot de passe incorrect.")
                return redirect('authentification')  # Redirige vers la page de connexion en cas d'échec

    except Exception as e:
        messages.error(request, f"Une erreur s'est produite : {str(e)}")
        return redirect('authentification')

    return render(request, 'authentification.html')

def creer_compte(request):
    try:
        if request.method == "POST":
            matricule = request.POST.get("matricule")
            username = request.POST.get("nomdutilisateur")
            password = request.POST.get("password")
            confirmpassword = request.POST.get("confirmpassword")

            # Vérification si le matricule ou le nom d'utilisateur existe déjà
            if CompteUtilisateur.objects.filter(enseignant=matricule).exists() or CompteUtilisateur.objects.filter(apprenant=matricule).exists():
                messages.warning(request, "Ce Matricule a déjà un compte !")
                return redirect('creation_compte_utilisateur')
            elif CompteUtilisateur.objects.filter(username=username).exists():
                messages.warning(request, "Ce nom d'utilisateur a déjà un compte !")
                return redirect('creation_compte_utilisateur')
            else:
                # Vérification si le matricule correspond à un enseignant
                if Enseignant.objects.filter(matricule=matricule).exists():
                    enseignant = get_object_or_404(Enseignant, pk=matricule)
                    if password == confirmpassword:
                        user = CompteUtilisateur(
                            username=username,
                            enseignant=enseignant
                        )
                        user.set_password(password)  # Hachage du mot de passe
                        user.save()
                        messages.success(request, "Votre compte a été créé avec succès ! \n Authentifiez-vous maintenant !")
                        return redirect('authentification')
                    else:
                        messages.warning(request, "Le premier mot de passe doit être identique au second !")
                        return redirect('creation_compte_utilisateur')
                # Vérification si le matricule correspond à un apprenant
                elif Apprenant.objects.filter(matricule=matricule).exists():
                    apprenant = get_object_or_404(Apprenant, pk=matricule)
                    if password == confirmpassword:
                        user = CompteUtilisateur(
                            username=username,
                            apprenant=apprenant
                        )
                        user.set_password(password)  # Hachage du mot de passe
                        user.save()
                        messages.success(request, "Votre compte a été créé avec succès ! \n Authentifiez-vous maintenant !")
                        return redirect('authentification')
                    else:
                        messages.warning(request, "Le premier mot de passe doit être identique au second !")
                        return redirect('creation_compte_utilisateur')
                else:
                    messages.warning(request, "Vous ne pouvez pas créer un compte sur cette plateforme ! \n Veuillez contacter le bureau du CFPI !")
                    return redirect('creation_compte_utilisateur')

    except Exception as e:
        messages.error(request, f"Une erreur s'est produite lors de l'exécution : {str(e)} \n Actualisez la page !")
    return render(request, 'creer_compte.html')

def logout_view(request):
    logout(request)
    return redirect('home')

def dashboard_admin(request):
    try:
        apprenants = Apprenant.objects.all()
        total_apprenants = apprenants.count()
        total_enseignants = Enseignant.objects.all().count()
        total_formations=Formation.objects.all().count()
        context = {
            'apprenants': apprenants, 
            'total_apprenants':total_apprenants,
            'total_enseignants':total_enseignants,
            'total_formations':total_formations
            }
    except Exception as e:
        messages.error(request, f"Une erreur s'est produite lors de l'exécution : {str(e)} \n Actualisez la page !")
    return render(request,'admin/dashboard.html', context)

def domaine_admin(request):
    try:
        domaine = Domaine.objects.all()
        context = {'domaines':domaine}
    except Exception as e:
        messages.error(request, f"Une erreur s'est produite lors de l'exécution : {str(e)} \n Actualisez la page !")
    return render(request,'admin/domaine.html', context)

def modalitepaiement(request):
    try:
      modalite = ModalitePaie.objects.all()
      module = Module.objects.all()
      context = {'modalitepaies':modalite, 'modules':module}
    except Exception as e:
        messages.error(request, f"Une erreur s'est produite lors de l'exécution : {str(e)} \n Actualisez la page !")
    return render(request,'admin/modalitepaiement.html', context)

def niveau(request):
    try:
        niveau = Niveau.objects.all()
        context = {'niveaux':niveau}
    except Exception as e:
        messages.error("Une erreur s'est produite lors de l'exécution \n Actualisez la page !")
    return render(request,'admin/niveau.html',context)

def paiement(request):
    try:
        paiement = Paiement.objects.all()
        apprenant = Apprenant.objects.all()
        module = Module.objects.all()
        context = {'paiements':paiement, 'apprenants':apprenant, 'modules':module}
    except Exception as e:
        messages.error(request, f"Une erreur s'est produite lors de l'exécution : {str(e)} \n Actualisez la page !")
        return redirect('paiement')
    return render(request,'admin/paiement.html', context)

def typeressource(request):
    try:
        type = TypeRessource.objects.all()
        context = {'types':type}
    except Exception as e:
        messages.error(request, f"Une erreur s'est produite lors de l'exécution : {str(e)} \n Actualisez la page !")
        return redirect('inscription_admin')
    return render(request,'enseignant/typeressource.html', context)


# =======================================================================================================
# NIVEAU
# =======================================================================================================

def insertNiveau(request):
    try:
      if request.method == "POST":
        designation = request.POST.get("designation")

        if Niveau.objects.filter(designation = designation.capitalize()):
            messages.warning(request, "Cette information existe déjà !")
        else:
            Niveau.objects.create(
                designation = designation.capitalize()
            )
            messages.success(request,"Ajouté avec succès !")
            return redirect('niveau_admin')
    except Exception as e:
      messages.error(request, f"Une erreur s'est produite lors de l'exécution : {str(e)} \n Actualisez la page !")
      return redirect('niveau_admin')
    return render(request,'admin/niveau.html')

def updateNiveau(request):
    try:
      if request.method == "POST":
        code = request.POST.get("code")
        designation = request.POST.get("designation")

        if Niveau.objects.filter(designation = designation.capitalize()):
            messages.warning(request, "Cette information existe déjà !")
        else:
            Niveau(
                code = code,
                designation = designation.capitalize()
            ).save()
            messages.success(request,"Modifié avec succès !")
            return redirect('niveau_admin')
    except Exception as e:
      messages.error(request, f"Une erreur s'est produite lors de l'exécution : {str(e)} \n Actualisez la page !")
      return redirect('niveau_admin')
    return render(request, 'admin/niveau.html')

# =======================================================================================================
# DOMAINE
# =======================================================================================================

def insertDomaine(request):
    try:
      if request.method == "POST":
        designation = request.POST.get("designation")

        if Domaine.objects.filter(designation = designation.capitalize()):
            messages.warning(request, "Cette information existe déjà !")
        else:
            Domaine.objects.create(
                designation = designation.capitalize()
            )
            messages.success(request, "Ajouté avec succès !")
            return redirect('domaine_admin')
    except Exception as e:
      messages.error(request, f"Une erreur s'est produite lors de l'exécution : {str(e)} \n Actualisez la page !")
    return render(request, 'admin/domaine.html')

def updateDomaine(request):
    try:
      if request.method == "POST":
        code = request.POST.get("code")
        designation = request.POST.get("designation")
        
        if Domaine.objects.filter(designation = designation.capitalize()):
            messages.error(request, "Cette information existe déjà !")
        else:
            Domaine(
                code = code,
                designation = designation.capitalize()
            ).save()
            messages.success(request, "Modifié avec succès !")
            return redirect("domaine_admin")
    except Exception as e:
      messages.error(request, f"Une erreur s'est produite lors de l'exécution : {str(e)} \n Actualisez la page !")
    return render(request, 'chargement_modal/domaine.html')


# =======================================================================================================
# APPRENANT
# =======================================================================================================

def apprenant_admin(request):
    try:
      apprenant = Apprenant.objects.all()
      context = {'apprenants':apprenant}
    except Exception as e:
      messages.error(request, f"Une erreur s'est produite lors de l'exécution : {str(e)} \n Actualisez la page !")
    return render(request,'admin/apprenant.html', context)

def generer_matricule_apprenant():
        # Récupérer le dernier matricule pour déterminer le prochain
        dernier_etudiant = Apprenant.objects.last()
        if dernier_etudiant:
            dernier_numero = int(dernier_etudiant.matricule[3:])  # Extrait le numéro après "ETU"
        else:
            dernier_numero = 0
        prochain_numero = dernier_numero + 1
        return f"ETU{prochain_numero:04d}"

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
        
        if Apprenant.objects.filter(nom = nom.capitalize(), postnom = postnom.capitalize(), prenom = prenom.title()):
            messages.warning(request, "L'apprenant existe déjà !")
            return redirect('apprenant_admin')
        else:
            Apprenant.objects.create(
                matricule = generer_matricule_apprenant(),
                nom = nom.capitalize(),
                postnom = postnom.capitalize(),
                prenom = prenom.title(),
                genre = genre.capitalize(),
                etatcivil = etatcivil.capitalize(),
                addresse = addresse.capitalize(),
                contact = contact.capitalize(),
                profession = profession.capitalize(),
                photo = photo
            )
            messages.success(request, "Apprenant ajouté avec succès !")
            return redirect('apprenant_admin')
    except Exception as e:
      messages.error(request, f"Une erreur s'est produite lors de l'exécution : {str(e)} \n Actualisez la page !")
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
        
        if Apprenant.objects.filter(nom = nom.capitalize(), postnom = postnom.capitalize(), prenom = prenom.title(), genre = genre.capitalize(), etatcivil = etatcivil.capitalize(), addresse = addresse.capitalize(), contact = contact, profession = profession.capitalize(), photo = photo):
                messages.warning(request, "Ces informations existent déjà !")
                return redirect('apprenant_admin')
        else:
            if photo:
                Apprenant(
                    matricule = matricule,
                    nom = nom.capitalize(),
                    postnom = postnom.capitalize(),
                    prenom = prenom.capitalize(),
                    genre = genre.capitalize(),
                    etatcivil = etatcivil.capitalize(),
                    addresse = addresse.capitalize(),
                    contact = contact.capitalize(),
                    profession = profession.capitalize(),
                    photo = photo
                ).save()
                messages.success(request, "La modification a été appliquée avec succés !")
                return redirect('apprenant_admin')
            else:
                apprenant = get_object_or_404(Apprenant, pk = matricule)
                Apprenant(
                    matricule = matricule,
                    nom = nom.capitalize(),
                    postnom = postnom.capitalize(),
                    prenom = prenom.capitalize(),
                    genre = genre.capitalize(),
                    etatcivil = etatcivil.capitalize(),
                    addresse = addresse.capitalize(),
                    contact = contact.capitalize(),
                    profession = profession.capitalize(),
                    photo = apprenant.photo
                ).save()
                messages.success(request, "La modification a été appliquée avec succés !")
                return redirect('apprenant_admin')
    except Exception as e:
      messages.error(request, f"Une erreur s'est produite lors de l'exécution : {str(e)} \n Actualisez la page !")
      return redirect('apprenant_admin')
    return render(request,'admin/apprenant.html')

# =======================================================================================================
# ENSEIGNANT
# =======================================================================================================

def enseignant_admin(request):
    try:
      enseignant = Enseignant.objects.all()
      context = {'enseignants':enseignant}
    except Exception as e:
      messages.error(request, f"Une erreur s'est produite lors de l'exécution : {str(e)} \n Actualisez la page !")
      return redirect('apprenant_admin')
    return render(request,'admin/enseignant.html', context)

def generer_matricule_enseignant():
    # Récupérer le dernier matricule pour déterminer le prochain
    dernier_enseignant = Enseignant.objects.last()
    if dernier_enseignant:
        dernier_numero = int(dernier_enseignant.matricule[3:])  # Extrait le numéro après "ETU"
    else:
        dernier_numero = 0
    prochain_numero = dernier_numero + 1
    return f"ENS{prochain_numero:04d}"

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
        
        if Enseignant.objects.filter(nom = nom.capitalize(), postnom = postnom.capitalize(), prenom = prenom.title()):
            messages.error(request, "L'enseignant existe déjà !")
        else:
            Enseignant.objects.create(
                matricule = generer_matricule_enseignant(),
                nom = nom.capitalize(),
                postnom = postnom.capitalize(),
                prenom = prenom.capitalize(),
                genre = genre.capitalize(),
                etatcivil = etatcivil.capitalize(),
                addresse = addresse.capitalize(),
                contact = contact.capitalize(),
                profession = profession.capitalize(),
                photo = photo
            )
            messages.success(request, "Enseignant ajouté avec succès !")
            return redirect('enseignant_admin')
    except Exception as e:
      messages.error(request, f"Une erreur s'est produite lors de l'exécution : {str(e)} \n Actualisez la page !")
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
            
            if Enseignant.objects.filter(nom = nom.capitalize(), postnom = postnom.capitalize(), prenom = prenom.title(), genre = genre.capitalize(), etatcivil = etatcivil.capitalize(), addresse = addresse.capitalize(), contact = contact, profession = profession.capitalize(), photo = photo):
                    messages.warning(request, "Ces informations existent déjà !")
                    return redirect('enseignant_admin')
            else:
                if photo:
                    Enseignant(
                            matricule = matricule,
                            nom = nom.capitalize(),
                            postnom = postnom.capitalize(),
                            prenom = prenom.capitalize(),
                            genre = genre.capitalize(),
                            etatcivil = etatcivil.capitalize(),
                            addresse = addresse.capitalize(),
                            contact = contact.capitalize(),
                            profession = profession.capitalize(),
                            photo = photo
                    ).save()
                    messages.success(request, "La modification a été appliquée avec succés !")
                    return redirect('enseignant_admin')
                else:
                    enseignant = get_object_or_404(Enseignant, pk = matricule)
                    Enseignant(
                            matricule = matricule,
                            nom = nom.capitalize(),
                            postnom = postnom.capitalize(),
                            prenom = prenom.capitalize(),
                            genre = genre.capitalize(),
                            etatcivil = etatcivil.capitalize(),
                            addresse = addresse.capitalize(),
                            contact = contact.capitalize(),
                            profession = profession.capitalize(),
                            photo = enseignant.photo
                    ).save()
                    messages.success(request, "La modification a été appliquée avec succés !")
                    return redirect('enseignant_admin')
    except Exception as e:
      messages.error(request, f"Une erreur s'est produite lors de l'exécution : {str(e)} \n Actualisez la page !")
      return redirect('enseignant_admin')
    return render(request,'admin/enseignant.html')

# =======================================================================================================
# TYPE RESSOURCE
# =======================================================================================================

def insertTypeRessource(request):
    try:
      if request.method == "POST":
          designation = request.POST.get("designation")
          
          if TypeRessource.objects.filter(designation = designation.capitalize()):
              messages.warning(request, "Cette information existe déjà !")
              return redirect('typeressource')
          else:
            TypeRessource.objects.create(
                designation = designation.capitalize()
            )
          messages.success(request,"Ajouté avec succès !")
          return redirect('typeressource')
    except Exception as e:
      messages.error(request, f"Une erreur s'est produite lors de l'exécution : {str(e)} \n Actualisez la page !")
      return redirect('typeressource')
    return render(request, "enseignant/typeressource.html")

def updateTypeRessource(request):
    try:
        if request.method == "POST":
            code = request.POST.get("code")
            designation = request.POST.get("designation")
            
            if TypeRessource.objects.filter(designation = designation.capitalize()):
                messages.error(request,"Cette information existe déjà !")
            else:
                TypeRessource(
                    code = code,
                    designation = designation.capitalize()
                ).save()
                messages.success(request,"Modifié avec succès !")
                return redirect('typeressource')
    except Exception as e:
      messages.error(request, f"Une erreur s'est produite lors de l'exécution : {str(e)} \n Actualisez la page !")
      return redirect('typeressource')
    return render(request, "enseignant/typeRessource.html")

# =======================================================================================================
# RESSOURCE
# =======================================================================================================

def ressource_admin(request):
    try:
        type = TypeRessource.objects.all()
        ressource = Ressource.objects.all()
        context = {'ressources':ressource, 'types':type}
    except Exception as e:
        messages.error(request, f"Une erreur s'est produite lors de l'exécution : {str(e)} \n Actualisez la page !")
    return render(request, 'enseignant/ressource.html', context)

def insertRessource(request):
    try:
      if request.method == "POST":
          titre = request.POST.get("titre")
          description = request.POST.get("description")
          contenu = request.FILES.get("contenu")
          id_type_ressource = request.POST.get("type_ressource")
          
          type_ressource = get_object_or_404(TypeRessource, pk = id_type_ressource)
          
          if Ressource.objects.filter(titre = titre.capitalize(), description = description.capitalize()):
              messages.warning(request,"Ces informations existent déjà !")
              return redirect('ressource_admin')
          else:
              Ressource.objects.create(
                  titre = titre.capitalize(),
                  description = description.capitalize(),
                  contenu = contenu,
                  type_ressource = type_ressource
              )
              messages.success(request,"Ressource ajoutée avec succès !")
              return redirect('ressource_admin')
    except Exception as e:
      messages.error(request, f"Une erreur s'est produite lors de l'exécution : {str(e)} \n Actualisez la page !")
    return render(request,'enseignant/ressource.html')

def updateRessource(request):
    try:
      if request.method == "POST":
          code = request.POST.get("code")
          titre = request.POST.get("titre")
          description = request.POST.get("description")
          contenu = request.FILES.get("contenu")
          id_type_ressource = request.POST.get("type_ressource")
          
          type_ressource = get_object_or_404(TypeRessource, pk = id_type_ressource)
          
          if Ressource.objects.filter(titre = titre.capitalize(), description = description.capitalize(), contenu = contenu):
              messages.warning(request, "Ces informations existent déjà !")
              return redirect('ressource_admin')
          else:
              if contenu:
                    Ressource(
                        code = code,
                        titre = titre.capitalize(),
                        description = description.capitalize(),
                        contenu = contenu,
                        type_ressource = type_ressource
                    ).save()
                    messages.success(request,"Ressource modifeé avec succès !")
                    return redirect('ressource_admin')
              else:
                    ressource = get_object_or_404(Ressource, pk = code)
                    Ressource(
                        code = code,
                        titre = titre.capitalize(),
                        description = description.capitalize(),
                        contenu = ressource.contenu,
                        type_ressource = type_ressource
                    ).save()
                    messages.success(request,"Ressource modifeé avec succès !")
                    return redirect('ressource_admin')
    except Exception as e:
      messages.error(request, f"Une erreur s'est produite lors de l'exécution : {str(e)} \n Actualisez la page !")
      return redirect('ressource_admin')
    return render(request,'enseignant/ressource.html')

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
        chapitre = Chapitre.objects.all()
        ressource = Ressource.objects.all()
        context = {'modules': module, 'niveaux':niveau, 'ressources':ressource, 'chapitres':chapitre}
    except Exception as e:
        messages.error(request, f"Une erreur s'est produite lors de l'exécution : {str(e)} \n Actualisez la page !")
        return redirect('module_enseignant')
    return render(request,'enseignant/module.html', context)

# def insertModule(request):
#     # try:
#       if request.method == "POST":
#         titre = request.POST.get("titre")
#         description = request.POST.get("description")
#         prix = request.POST.get("prix")
#         id_niveau = request.POST.get("niveau")
#         id_chapitre = request.POST.get("chapitre")
#         id_ressource = request.POST.get("ressource")
        
#         print(f"{id_chapitre}")
#         niveau = get_object_or_404(Niveau, pk = id_niveau)
#         chapitre = get_object_or_404(Chapitre, pk = id_chapitre)
#         ressource = get_object_or_404(Ressource, pk = id_ressource)
        
#         if Module.objects.filter(titre = titre.capitalize(), description = description.capitalize(), prix=prix, niveau=niveau,chapitre=chapitre):
#             messages.warning("Ce module eisxte déjà !")
#             return redirect('module_enseignant')
#         else:
#             Module.objects.create(
#                 titre = titre.capitalize(),
#                 description = description.capitalize(),
#                 prix = prix,
#                 niveau = niveau,
#                 chapitre = chapitre,
#                 ressource = ressource
#             )
#             messages.success(request,"Module ajouté avec succès !")
#             return redirect('module_enseignant')
#     # except Exception as e:
#     #   messages.error(request, f"Une erreur s'est produite lors de l'exécution : {str(e)} \n Actualisez la page !")
#     #   return redirect('module_enseignant')
#         return render(request,"ensignant/module.html")

def insertModule(request):
    if request.method == "POST":
        titre = request.POST.get("titre")
        description = request.POST.get("description")
        prix = request.POST.get("prix")
        id_niveau = request.POST.get("niveau")
        id_chapitre = request.POST.get("chapitre")
        id_ressource = request.POST.get("ressource")

        if not id_niveau or not id_chapitre:
            messages.error(request, "Veuillez sélectionner un niveau et un chapitre.")
            return redirect('module_enseignant')
        
        niveau = get_object_or_404(Niveau, pk=id_niveau)
        chapitre = get_object_or_404(Chapitre, pk=id_chapitre)

        # Ressource peut être optionnelle selon votre modèle
        ressource = get_object_or_404(Ressource, pk=id_ressource) if id_ressource else None
        
        if Module.objects.filter(titre=titre.capitalize(), description=description.capitalize(), prix=prix, niveau=niveau, chapitre=chapitre).exists():
            messages.warning(request, "Ce module existe déjà !")
            return redirect('module_enseignant')
        else:
            Module.objects.create(
                titre=titre.capitalize(),
                description=description.capitalize(),
                prix=prix,
                niveau=niveau,
                chapitre=chapitre,
                ressource=ressource
            )
            messages.success(request, "Module ajouté avec succès !")
            return redirect('module_enseignant')

    return render(request, "ensignant/module.html")

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
            
            if Module.objects.filter(titre = titre.capitalize(), description = description.capitalize(), prix = prix, niveau = niveau, ressource = ressource):
                messages.warning(request, "Ce module existe déjà !")
                return redirect('module_enseignant')
            else:
                Module(
                    code = code,
                    titre = titre.capitalize(),
                    description = description.capitalize(),
                    prix = prix,
                    niveau = niveau,
                    ressource = ressource
                ).save()
                messages.success(request, "Module modifié avec succès !")
                return redirect('module_enseignant')
    except Exception as e:
      messages.error(request, f"Une erreur s'est produite lors de l'exécution : {str(e)} \n Actualisez la page !")
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
    except Exception as e:
        messages.error(request, f"Une erreur s'est produite lors de l'exécution : {str(e)} \n Actualisez la page !")
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
                                titre = titre.capitalize(),
                                duree = duree,
                                date_debut = date_debut,
                                date_fin = date_fin,
                                module = module,
                                enseignant = enseignant
                            ):
              messages.warning(request, "Ces information existent déjà !")
              return redirect('formation_admin')
          else:
            Formation.objects.create(
                titre = titre.capitalize(),
                duree = duree,
                description = description.capitalize(),
                date_debut = date_debut,
                date_fin = date_fin,
                module = module,
                enseignant = enseignant,
                domaine = domaine
            )
            messages.success(request,"Formation ajoutée avec succès !")
            return redirect('formation_admin')
    except Exception as e:
      messages.error(request, f"Une erreur s'est produite lors de l'exécution : {str(e)} \n Actualisez la page !")
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
                                titre = titre.capitalize(),
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
                    titre = titre.capitalize(),
                    description = description.capitalize(),
                    duree = duree,
                    date_debut = date_debut,
                    date_fin = date_fin,
                    module = module,
                    enseignant = enseignant,
                    domaine = domaine
                ).save()
          messages.success(request,"Formation modifiée avec succès !")
          return redirect('formation_admin')
    except Exception as e:
      messages.error(request, f"Une erreur s'est produite lors de l'exécution : {str(e)} \n Actualisez la page !")
      return redirect('formation_admin')
    return render(request,'Apprenant/formation.html')

# =======================================================================================================
# MODALITE PAIE
# =======================================================================================================

def insertModalitePaie(request):
    try:
      if request.method == "POST":
          tranche = request.POST.get("tranche")
          id_module = request.POST.get("module")
          
          module = get_object_or_404(Module, pk = id_module)
          
          if tranche == "Une Tranche":
            montant_fixe = module.prix
          elif tranche == "Deux Tranches":
            montant_fixe = module.prix/2
          else:
            montant_fixe = module.prix/3


          ModalitePaie.objects.create(
              tranche = tranche.capitalize(),
              montant_fixe = montant_fixe,
              module = module
          )
          messages.success(request,"Ajouté avec succès !")
          return redirect('modalite_paiement')
    except Exception as e:
      messages.error(request, f"Une erreur s'est produite lors de l'exécution : {str(e)} \n Actualisez la page !")
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
              tranche = tranche.capitalize(),
              montant_fixe = montant_fixe,
              module = module
          ).save()
          messages.success(request,"Modifié avec succès !")
          return redirect('modalite_paiement')
    except Exception as e:
      messages.error(request, f"Une erreur s'est produite lors de l'exécution : {str(e)} \n Actualisez la page !")
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
    except Exception as e:
      messages.error(request, f"Une erreur s'est produite lors de l'exécution : {str(e)} \n Actualisez la page !")
      return redirect('inscription_admin')
    return render(request, "admin/inscription.html", context)

def insertInscription(request):
    try:
      if request.method == "POST":
          id_apprenant = request.POST.get("apprenant")
          # id_formation = request.POST.get("formation")
          id_modalite = request.POST.get("modalite")
          date_inscription = request.POST.get("date_inscription")
          
          apprenant = get_object_or_404(Apprenant, pk = id_apprenant)
          # formation = get_object_or_404(Formation, pk = id_formation)
          modalite = get_object_or_404(ModalitePaie, pk = id_modalite)
          
          Inscription.objects.create(
              apprenant = apprenant,
              # formation = formation,
              modalite = modalite,
              date_inscription = date_inscription
          )
          messages.success(request, "Inscription éffectuée avec succès !")
          return redirect('inscription_admin')
    except Exception as e:
      messages.error(request, f"Une erreur s'est produite lors de l'exécution : {str(e)} \n Actualisez la page !")
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
          return redirect('inscription_admin')
    except Exception as e:
      messages.error(request, f"Une erreur s'est produite lors de l'exécution : {str(e)} \n Actualisez la page !")
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
    except Exception as e:
        messages.error(request, f"Une erreur s'est produite lors de l'exécution : {str(e)} \n Actualisez la page !")
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
    except Exception as e:
      messages.error(request, f"Une erreur s'est produite lors de l'exécution : {str(e)} \n Actualisez la page !")
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
    except Exception as e:
      messages.error(request, f"Une erreur s'est produite lors de l'exécution : {str(e)} \n Actualisez la page !")
      return redirect('evaluation')
    return render(request, "enseignant/interrogation.html")

# =======================================================================================================
# PUBLICATION
# =======================================================================================================

def publication(request):
    try:
        posts = Publication.objects.all().order_by('-date_publication')
        context = {'posts':posts}
    except Exception as e:
      messages.error(request, f"Une erreur s'est produite lors de l'exécution : {str(e)} \n Actualisez la page !")
    return render(request, "publications.html", context)

def comment_post(request, post_id):
    try:
        post = get_object_or_404(Publication, code=post_id)
        if request.method == "POST" and request.user.is_authenticated:
            content = request.POST.get('content')
            Commentaire.objects.create(publication=post, user=request.user, content=content)
    except Exception as e:
              messages.error(request, f"Une erreur s'est produite lors de l'exécution : {str(e)} \n Actualisez la page !")
    return HttpResponseRedirect(reverse('post_list'))

def popular_posts(request):
    try:
        posts = Publication.objects.annotate(like_count=models.Count('likes')).order_by('-like_count')
    except Exception as e:
        messages.error(request, f"Une erreur s'est produite lors de l'exécution : {str(e)} \n Actualisez la page !")
    return render(request, 'publications_populaires.html', {'posts': posts})

def like_post(request, post_id):
    try:
        post = get_object_or_404(Publication, code=post_id)
        if request.user.is_authenticated:
            like, created = Like.objects.get_or_create(publication=post, user=request.user)
            if not created:
                like.delete()  # Si l'utilisateur a déjà liké, on supprime le like
    except Exception as e:
        messages.error(request, f"Une erreur s'est produite lors de l'exécution : {str(e)} \n Actualisez la page !")
    return HttpResponseRedirect(reverse('post_list'))

def publication_admin(request):
    try:
        publication = Publication.objects.all()
        context = {'publications':publication}
    except Exception as e:
      messages.error(request, f"Une erreur s'est produite lors de l'exécution : {str(e)} \n Actualisez la page !")
    return render(request,'admin/publication.html', context)

def insertPublication(request):
    try:
      if request.method == "POST":
          titre = request.POST.get("titre")
          description = request.POST.get("description")
          id_compte_utilisateur = request.POST.get("compte_utilisateur")
          date_publication = request.POST.get("date_publication")
          
          compte_utilisateur = get_object_or_404(CompteUtilisateur, pk = id_compte_utilisateur)
          # compte_utilisateur = CompteUtilisateur.objects.filter()
          
          if Publication.objects.filter(titre = titre.capitalize(), description = description.capitalize(), compte_utilisateur = compte_utilisateur):
            messages.warning("Ces informations existent déjà !")
            return redirect('publication_admin')
          else:

            Publication.objects.create(
                  titre = titre.capitalize(),
                  description = description.capitalize(),
                  user = compte_utilisateur,
                date_publication = date_publication
            )
            messages.success(request, "Publication ajoutée avec succès !")
            return redirect('publication_admin')
    except Exception as e:
      messages.error(request, f"Une erreur s'est produite lors de l'exécution : {str(e)} \n Actualisez la page !")
      return redirect('publication_admin')
    return render(request, 'admin/publication.html')

def updatePublication(request):
    try:
      if request.method == "POST":
          code = request.POST.get("code")
          titre = request.POST.get("titre")
          description = request.POST.get("description")
          id_compte_utilisateur = request.POST.get("compte_utilisateur")
          date_publication = request.POST.get("date_publication")
          
          compte_utilisateur = get_object_or_404(CompteUtilisateur, pk = id_compte_utilisateur)
          
          if Publication.objects.filter(titre = titre.capitalize(), description = description.capitalize(), compte_utilisateur = compte_utilisateur):
              messages.warning("Ces informations existent déjà !")
              return redirect('publication_admin')
          else:
              Publication(
                code = code,
                titre = titre.capitalize(),
                description = description.capitalize(),
                compte_utilisateur = compte_utilisateur,
                date_publication = date_publication
              ).save()
              messages.success(request, "Publication modifiée avec succès !")
              return redirect('publication_admin')
    except Exception as e:
      messages.error(request, f"Une erreur s'est produite lors de l'exécution : {str(e)} \n Actualisez la page !")
      return redirect('publication_admin')
    return render(request, 'admin/publication.html')

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
    except Exception as e:
      messages.error(request, f"Une erreur s'est produite lors de l'exécution : {str(e)} \n Actualisez la page !")
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
    except Exception as e:
      messages.error(request, f"Une erreur s'est produite lors de l'exécution : {str(e)} \n Actualisez la page !")
      return redirect('paiement')
    return render(request,'admin/paiement.html')

# =======================================================================================================
# QUESTIONNAIRE
# =======================================================================================================

def questionnaire(request):
    try:
        modules = Module.objects.all()
        questionnaire = Questionnaire.objects.all()
    except Exception as e:
      messages.error(request, f"Une erreur s'est produite lors de l'exécution : {str(e)} \n Actualisez la page !")
    
    return render(request, 'admin/questionnaire.html', {'modules': modules, 'questionnaire':questionnaire})

def add_questionnaire(request):
    try:
        if request.method == "POST":
            module_id = request.POST.getlist('module')
            questions = request.POST.getlist('question')
            responses = request.POST.getlist('reponse')
            maxima = request.POST.getlist('maxima')

            for i in range(len(questions)):
                Questionnaire.objects.create(
                    module_id=module_id[i],
                    question=questions[i].capitalize(),
                    reponse=responses[i].capitalize(),
                    maxima=maxima[i]
                )
            
            messages.success(request, "Question(s) Ajouté(s) avec succès !")
            return redirect('questionnaire')
        
        # If GET request, render the form
        
    except Exception as e:
      messages.error(request, f"Une erreur s'est produite lors de l'exécution : {str(e)} \n Actualisez la page !")
    return render(request, 'admin/questionnaire.html')

def updateQuestionnaire(request):
    try:
      if request.method == "POST":
          code = request.POST.get("code")
          id_module = request.POST.get("module")
          question = request.POST.get("question")
          reponse = request.POST.get("reponse")
          maxima = request.POST.get("maxima")
          
          module = get_object_or_404(Module, pk = id_module)
          
          if Questionnaire.objects.filter(module = module, question = question.capitalize(), reponse = reponse.capitalize()):
              messages.warning("Ces informations existent déjà !")
          else:
              Questionnaire(
                  code = code,
                  module = module,
                  question = question,
                  reponse = reponse,
                  maxima = maxima
              ).save()
              messages.success(request, "Modifié avec succès !")
              return redirect('questionnaire')
    except Exception as e:
      messages.error(request, f"Une erreur s'est produite lors de l'exécution : {str(e)} \n Actualisez la page !")
    return render(request, 'admin/questionnaire.html')

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
              questionnaire = questionnaire.capitalize(),
              reponse = reponse.capitalize()
          )
          messages.success(request, "Ajouté avec succès !")
    except Exception as e:
      messages.error(request, f"Une erreur s'est produite lors de l'exécution : {str(e)} \n Actualisez la page !")
    return HttpResponse("Ajouté avec succès !")

# =====================================================================================================================
# TESTER SI APPRENANT A UN TEST A PASSER
# =====================================================================================================================

def rediriger_utilisateur(request):
    user = request.user  # Récupération de l'utilisateur connecté

    if user.apprenant is not None:  # Vérification si l'attribut `apprenant` n'est pas nul
        if Apprenant.objects.filter(matricule=user.apprenant.matricule).exists():  # Vérification si le matricule de l'apprenant existe
            apprenant = user.apprenant
            inscription = Inscription.objects.filter(apprenant=apprenant).last()

            if inscription:
                if inscription.formation is None:
                    messages.warning(request, "Vous devez répondre à ces questions !")
                    return redirect('tester_apprenant')
                else:
                    return redirect('dashboard_apprenant')
            else:
                messages.warning(request, "Vous n'etes pas encore inscrit ! \n Contactez le bureau du CFPI !")
                logout(request)
                return redirect('home')
        else:
            return HttpResponse("Le matricule de l'apprenant n'est pas valide.")
    
    elif user.enseignant is not None:  # Vérification si l'attribut `enseignant` n'est pas nul
        if Enseignant.objects.filter(matricule=user.enseignant.matricule).exists():  # Vérification si le matricule de l'enseignant existe
                return redirect('dashboard_enseignant')
        else:
            return HttpResponse("Le matricule de l'enseignant n'est pas valide.")
    
    else:  # Si les deux attributs `apprenant` et `enseignant` sont nuls
        return redirect('dashboard_admin')
    return HttpResponse("Une erreur s'est produite !")

# def tester_apprenant(request):
#     try:
#         formation = Formation.objects.all()
#         context = {'formations':formation}

#         if request.method == "POST":
#             id_formation = request.POST.get("formation")
#             formation = get_object_or_404(Formation, code=id_formation)
#             user = request.user

#             inscription = Inscription.objects.filter(apprenant=user.apprenant, formation__isnull=True).last()
#             code = inscription.code
#             Inscription(
#                     code = inscription.code,
#                     apprenant = inscription.apprenant,
#                     formation = formation,
#                     modalite = inscription.modalite,
#                     date_inscription = inscription.date_inscription
#                 ).save()
#             return redirect('prendre_test', formation_id=formation.code)
#     except Exception as e:
#       messages.error(request, f"Une erreur s'est produite lors de l'exécution : {str(e)} \n Actualisez la page !")
#     return render(request,'apprenant/pretestis.html', context)

def tester_apprenant(request):
    formations = Formation.objects.all()
    context = {'formations':formations}
    if request.method == "POST":
        id_formation = request.POST.get("formation")
        formation = get_object_or_404(Formation, code=id_formation)
        
        return redirect('prendre_test', formation_id=formation.code, question_index=0)
    return render(request,'apprenant/pretestis.html', context)


def prendre_test(request, formation_id, question_index=0):
    # Récupérer la formation spécifique
    formation = get_object_or_404(Formation, code=formation_id)
    
    # Filtrer les questions par formation
    questions = Questionnaire.objects.filter(module=formation.module.code)
    
    if question_index >= len(questions):
        # Si toutes les questions ont été répondues, rediriger vers une page de succès ou de résultats
        return redirect('test_termine')

    question_actuelle = questions[question_index]
    reponses_alternatives = list(Reponses_alternatives.objects.filter(questionnaire=question_actuelle))
    
    # Assurez-vous que la liste des réponses alternatives n'est pas vide
    if reponses_alternatives:
        # Ajouter la réponse correcte comme une alternative
        # Ici, on suppose que `question_actuelle.reponse` est le code de la réponse correcte
        reponse_correcte = Questionnaire.objects.filter(reponse=question_actuelle.reponse)
        reponses_alternatives.append(reponse_correcte)
        random.shuffle(reponses_alternatives)  # Mélanger les réponses
    
    if request.method == "POST":
        # Enregistrer la réponse
        texte_reponse = request.POST.get('reponses')
        Test.objects.create(
            apprenant=request.user.apprenant,  # Assurez-vous que l'utilisateur est lié à un apprenant
            questionnaire=question_actuelle,
            reponse=texte_reponse
        )
        # Passer à la question suivante
        return redirect('prendre_test', formation_id=formation_id, question_index=question_index+1)

    context = {
        'formation': formation,
        'question': question_actuelle,
        'question_index': question_index,
        'total_questions': len(questions),
        'reponses_alternatives': reponses_alternatives
    }
    return render(request, 'take_test.html', context)


def test_termine(request):
    return render(request, 'test_complete.html')







# ===============================================================================
# ============================== Partie Apprenant ================================
# ============================= Affichage module dans Apprenant===================
def affichageModule(request):
    return render(request,'apprenant/module.html')

# ============================= Affichage formation dans Apprenant=================
def affichageFormationApprenant(request):
    return render(request,'apprenant/formation.html')

# ============================ Affichage evaluation dans Apprenant=================
def affichageEvaluation(request):
    return render(request,'apprenant/evaluation.html')

# =========================== Affichage publication dans Apprenant=================
def affichagePublication(request):
    return render(request,'apprenant/publication.html')



# ============================= Affichage sous chapitre dans Apprenant=================
def sous_chapitre_apprenant(request):
    try:
        sous_chapitre = Sous_chapitre.objects.all()
        conrext = {'sous_chapitres': sous_chapitre}
    except Exception as e:
        raise e
    return render(request,'apprenant/souschapitre.html')

# ============================= Affichage chapitre dans Apprenant=================
def chapitre_apprenant(request):
    return render(request,'apprenant/chapitre.html')


# ============================== Partie Enseignant ================================
# ============================= Affichage Apprenant dans Enseignant===================
def affichageApprenant(request):
    return render(request,'enseignant/listeApprenant.html')

# ============================= Affichage formation dans Enseignant=================
def affichageFormationEnseignant(request):
    return render(request,'enseignant/formation.html')

# ============================= Affichage sous chapitre dans Enseignant=================
def sous_chapitre_enseignant(request):
    try:
        sous_chapitre = Sous_chapitre.objects.all()
        context = {'sous_chapitres': sous_chapitre}
    except Exception as e:
      messages.error(request, f"Une erreur s'est produite lors de l'exécution : {str(e)} \n Actualisez la page !")
    return render(request,'enseignant/souschapitre.html', context)

def insertSousChapitre(request):
    try:
        if request.method == "POST":
            titre = request.POST.get("titre")
            contenu = request.POST.get("contenu")

            if Sous_chapitre.objects.filter(titre = titre, contenu = contenu):
                messages.warning(request, "Ces informations existent déjà !")
                return redirect('sous_chapitre_enseignant')
            else:
                Sous_chapitre.objects.create(
                    titre = titre,
                    contenu = contenu
                )
                messages.success(request, "Ajouté avec succès !")
                return redirect('sous_chapitre_enseignant')
    except Exception as e:
      messages.error(request, f"Une erreur s'est produite lors de l'exécution : {str(e)} \n Actualisez la page !")
    return render(request, "enseignant/souschapitre.html")

def updateSousChapitre(request):
    try:
        if request.method == "POST":
            code = request.POST.get("code")
            titre = request.POST.get("titre")
            contenu = request.POST.get("contenu")

            if Sous_chapitre.objects.filter(titre = titre, contenu = contenu):
                messages.warning(request, "Ces informations existent déjà !")
                return redirect('sous_chapitre_enseignant')
            else:
                Sous_chapitre(
                    code = code,
                    titre = titre,
                    contenu = contenu
                ).save()
                messages.success(request, "Modifié avec succès !")
                return redirect('sous_chapitre_enseignant')
    except Exception as e:
      messages.error(request, f"Une erreur s'est produite lors de l'exécution : {str(e)} \n Actualisez la page !")
    return render(request, "enseignant/souschapitre.html")

# ============================= Affichage chapitre dans Enseignant=================
def chapitre_enseignant(request):
    try:
        chapitre = Chapitre.objects.all()
        sous_chapitre = Sous_chapitre.objects.all()
        contenu_chapitre = ContenuChapitre.objects.all()
        context = {'chapitres': chapitre, 'sous_chapitres':sous_chapitre, 'contenu_chapitre':contenu_chapitre}
    except Exception as e:
      messages.error(request, f"Une erreur s'est produite lors de l'exécution : {str(e)} \n Actualisez la page !")
    return render(request,'enseignant/chapitre.html', context)

def insertChapitre(request):
    try:
        if request.method == "POST":
            titre = request.POST.get("titre")

            if Chapitre.objects.filter(titre = titre):
                messages.warning(request, "Ces informations existent déjà !")
                return redirect('chapitre_enseignant')
            else:
                Chapitre.objects.create(
                    titre = titre
                )
                messages.success(request, "Ajouté avec succès !")
                return redirect('chapitre_enseignant')
    except Exception as e:
      messages.error(request, f"Une erreur s'est produite lors de l'exécution : {str(e)} \n Actualisez la page !")
    return render(request, "enseignant/chapitre.html")

def updateChapitre(request):
    try:
        if request.method == "POST":
            code = request.POST.get("code")
            titre = request.POST.get("titre")

            if Chapitre.objects.filter(titre = titre):
                messages.warning(request, "Ces informations existent déjà !")
                return redirect('chapitre_enseignant')
            else:
                Chapitre(
                    code = code,
                    titre = titre
                ).save()
                messages.success(request, "Modifié avec succès !")
                return redirect('chapitre_enseignant')
    except Exception as e:
      messages.error(request, f"Une erreur s'est produite lors de l'exécution : {str(e)} \n Actualisez la page !")
    return render(request, "enseignant/chapitre.html")

def insertContenuChapitre(request):
    try:
        if request.method == "POST":
            id_chapitre = request.POST.get("chapitre")
            id_sous_chapitre = request.POST.get("sous_chapitre")

            chapitre = get_object_or_404(Chapitre, pk = id_chapitre)
            sous_chapitre = get_object_or_404(Sous_chapitre, pk = id_sous_chapitre)

            if ContenuChapitre.objects.filter(chapitre = chapitre, sous_chapitre=sous_chapitre):
                messages.warning(request, "Ces informations existent déjà !")
                return redirect('chapitre_enseignant')
            else:
                ContenuChapitre.objects.create(
                    chapitre = chapitre, 
                    sous_chapitre=sous_chapitre
                )
                messages.success(request, "Ajouté avec succès !")
                return redirect('chapitre_enseignant')
    except Exception as e:
      messages.error(request, f"Une erreur s'est produite lors de l'exécution : {str(e)} \n Actualisez la page !")
    return render(request, "enseignant/chapitre.html")


# =========================== Admin & Type de publications ============================
def typePublication(request):
    return render(request,'admin/typepublication.html')

# ====================================================================================================
# 