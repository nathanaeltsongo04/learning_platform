from django.shortcuts import render

# Create your views here.

def index(request):
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
