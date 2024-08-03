from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('Test', views.Test,name='Test'),
    path('dashboard/', views.Dashboard_apprenant, name='dashboard_apprenant'),
    path('formation/', views.Formation_apprenant, name='formation_apprenant'),
    path('ressource/', views.Ressource_apprenant, name='ressource_apprenant'),
    path('chat/', views.Chat_apprenant, name='chat_apprenant'),
    path('horaire/', views.Horaire_apprenant, name='horaire_apprenant'),
]
