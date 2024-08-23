from django.conf import settings
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.core.mail import send_mail
from .models import Apprenant

# @receiver(post_save, sender=Apprenant)
# def send_welcome_email(sender, instance, created, **kwargs):
#     if created:
#         subject = 'Bienvenue sur notre plateforme'
#         message = f"Bonjour {instance.prenom},\n\nMerci de vous être inscrit sur notre plateforme."
#         from_email = 'nathanaeltsongo04@gmail.com'
#         recipient_list = [instance.email]
        
#         # Send email
#         send_mail(subject, message, from_email, recipient_list)

def envoyer_matricule_par_email(sender, instance, created, **kwargs):
    if created and instance.email:
        sujet = 'Votre Matricule'
        message = f'Bonjour {instance.prenom} {instance.postnom},\n\n Merci de vous etre enregistré(e) sur notre plateforme. Voici maintenant Votre matricule : {instance.matricule}. \n Utilisez-le pour creer un compte dans notre plateforme !\n\n Merci beaucoup !'
        destinataire = [instance.email]

        send_mail(
            sujet,
            message,
            settings.EMAIL_HOST_USER,
            destinataire,
            fail_silently=False,
        )