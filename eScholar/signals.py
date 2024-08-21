from django.db.models.signals import post_save
from django.dispatch import receiver
from django.core.mail import send_mail
from django.conf import settings
from .models import Apprenant

@receiver(post_save, sender=Apprenant)
def envoyer_matricule_par_email(sender, instance, created, **kwargs):
    if created and instance.email:
        sujet = 'Votre Matricule'
        message = f'Bonjour {instance.prenom} {instance.postnom},\n\n Merci de vous etre enregistré(e) sur notre plateforme. Voici maintenant Votre matricule : {instance.matricule}. \n Utilisez-le pour creer un compte dans notre plateforme !\n\n Merci beaucoup !'
        destinataire = [instance.email]

        send_mail(
            sujet,
            message,
            settings.DEFAULT_FROM_EMAIL,
            destinataire,
            fail_silently=False,
        )
