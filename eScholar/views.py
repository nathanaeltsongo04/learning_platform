from django.shortcuts import render

# Create your views here.

def Index(request):
    return render(request, 'index.html')

def Test(request):
    return render(request,'Test.html')

def Dashboard_apprenant(request):
    return render(request, 'apprenant/dashboard.html')

def Formation_apprenant(request):
    return render(request,'apprenant/formation.html')

def Ressource_apprenant(request):
    return render(request,'apprenant/ressource.html')

def Chat_apprenant(request):
    return render(request,'apprenant/chat.html')

def Horaire_apprenant(request):
    return render(request,'apprenant/horaire.html')

def Formation_enseignant(request):
    return render(request,'enseignant/formation.html')

def Module_enseignant(request):
    return render(request,'enseignant/module.html')

def Interrogation_enseignant(request):
    return render(request,'enseignant/interrogation.html')

def Cote_enseignant(request):
    return render(request,'enseignant/cote.html')

def Correction_enseignant(request):
    return render(request,'enseignant/correction.html')

def Dashboard_enseignant(request):
    return render(request,'enseignant/dashboard.html')

def Publication_enseignant(request):
    return render(request,'enseignant/publication.html')

def Dashboard_admin(request):
    return render(request,'admin/dashboard.html')

def Apprenant_admin(request):
    return render(request,'admin/apprenant.html')

def Enseignant_admin(request):
    return render(request,'admin/enseignant.html')

def Domaine_admin(request):
    return render(request,'admin/domain.html')

def Formation_admin(request):
    return render(request,'admin/formation.html')

def Modalitepaiement(request):
    return render(request,'admin/modalitepaiement.html')

def Niveau(request):
    return render(request,'admin/niveau.html')

def Paiement(request):
    return render(request,'admin/paiement.html')

def Publication_admin(request):
    return render(request,'admin/publication.html')

def Typeressource(request):
    return render(request,'admin/typeressource.html')

