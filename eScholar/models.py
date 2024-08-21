from django.db import models
from django.contrib.auth.models import AbstractUser


# Create your models here.
class Niveau(models.Model):
    code = models.AutoField(primary_key=True)
    designation = models.CharField(max_length=25)
    class Meta:
        db_table='Niveau'

class Domaine(models.Model):
    
    code =models.AutoField(primary_key=True)
    designation=models.CharField(max_length=50)
    
    class Meta:
        db_table='Domaine'
        
class Apprenant(models.Model):
    matricule=models.CharField(max_length=25, primary_key=True)
    nom=models.CharField(max_length=25)
    postnom=models.CharField(max_length=25)
    prenom=models.CharField(max_length=25)
    genre=models.CharField(max_length=1)
    etatcivil=models.CharField(max_length=25)
    addresse=models.CharField(max_length=50)
    contact=models.CharField(max_length=15)
    email = models.EmailField(max_length=254)
    profession=models.CharField(max_length=50)
    photo=models.ImageField(upload_to='ImageProfilApprenant/',blank=True)
    
    class Meta:
        db_table='Apprenant'
        
class Enseignant(models.Model):
    matricule=models.CharField(max_length=25, primary_key=True)
    nom=models.CharField(max_length=25)
    postnom=models.CharField(max_length=25)
    prenom=models.CharField(max_length=25)
    genre=models.CharField(max_length=1)
    etatcivil=models.CharField(max_length=25)
    addresse=models.CharField(max_length=50)
    contact=models.CharField(max_length=15)
    profession=models.CharField(max_length=50)
    photo=models.ImageField(upload_to='ImageProfilEnseignant/',blank=True)
    
    class Meta:
        db_table='Enseignant'
        
class TypeRessource(models.Model):
    code=models.AutoField(primary_key=True)
    designation=models.CharField(max_length=25)
    
    class Meta:
        db_table='TypeRessource'
        
class Ressource(models.Model):
    code=models.AutoField(primary_key=True)
    titre=models.CharField(max_length=25)
    description=models.TextField()
    contenu=models.FileField(upload_to="Ressource/", max_length=500)
    type_ressource=models.ForeignKey(TypeRessource,on_delete=models.CASCADE)
    
    class Meta:
        db_table='Ressource'

class Sous_chapitre(models.Model):
    code=models.AutoField(primary_key=True)
    titre = models.CharField(max_length=255)
    contenu=models.TextField()

    class Meta:
        db_table='Sous_chapitre'

class Chapitre(models.Model):
    code=models.AutoField(primary_key=True)
    titre = models.CharField(max_length=255)

    class Meta:
        db_table='Chapitre'

class ContenuChapitre(models.Model):
    code = models.AutoField(primary_key=True)
    chapitre = models.ForeignKey(Chapitre, on_delete=models.CASCADE)
    sous_chapitre=models.ForeignKey(Sous_chapitre, on_delete=models.CASCADE)

    class Meta:
        db_table='ContenuChapitre'

class Module(models.Model):
    code=models.AutoField(primary_key=True)
    titre=models.CharField(max_length=25)
    description=models.TextField()
    prix=models.DecimalField(max_digits=10, decimal_places=2)
    niveau=models.ForeignKey(Niveau,on_delete=models.CASCADE)
    chapitre=models.ForeignKey(Chapitre, on_delete=models.CASCADE)
    ressource=models.ForeignKey(Ressource,on_delete=models.CASCADE, null=True)
    
    class Meta:
        db_table='Module'

class Formation(models.Model):
    code=models.AutoField(primary_key=True)
    titre=models.CharField(max_length=50)
    description = models.TextField ()
    duree=models.CharField(max_length = 20)
    date_debut=models.DateField()
    date_fin=models.DateField()
    domaine = models.ForeignKey(Domaine, on_delete=models.CASCADE)
    module = models.ForeignKey(Module, on_delete=models.CASCADE)
    enseignant=models.ForeignKey(Enseignant, on_delete=models.CASCADE)
    
    class Meta:
        db_table='Formation'
        
class ModalitePaie(models.Model):
    code=models.AutoField(primary_key=True)
    tranche=models.CharField(max_length=25)
    montant_fixe=models.DecimalField(max_digits=10,decimal_places=2)
    module=models.ForeignKey(Module,on_delete=models.CASCADE)
    
    class Meta:
        db_table='ModalitePaie'
        
class Inscription(models.Model):
    code=models.AutoField(primary_key=True)
    apprenant=models.ForeignKey(Apprenant,on_delete=models.CASCADE)
    formation=models.ForeignKey(Formation,on_delete=models.CASCADE, null=True) 
    modalite=models.ForeignKey(ModalitePaie,on_delete=models.CASCADE, null=True)
    date_inscription=models.DateField(auto_now=True)
    
    class Meta:
        db_table='Inscription'
        
class Evaluation(models.Model):
    code=models.AutoField(primary_key=True)
    apprenant=models.ForeignKey(Apprenant, on_delete=models.CASCADE, null=True)
    formation=models.ForeignKey(Formation,on_delete=models.CASCADE)
    maximum=models.DecimalField(max_digits=10,decimal_places=1)
    cote=models.DecimalField(max_digits=10,decimal_places=1)
    date_evaluation=models.DateTimeField()
    
    class Meta:
        db_table='Evaluation'
        
class CompteUtilisateur(AbstractUser):
    apprenant=models.ForeignKey(Apprenant,on_delete=models.CASCADE, null=True)
    enseignant=models.ForeignKey(Enseignant,on_delete=models.CASCADE, null = True)
    
class Publication(models.Model):
    code=models.AutoField(primary_key=True)
    titre=models.CharField(max_length=255)
    description=models.TextField()
    user=models.ForeignKey(CompteUtilisateur,on_delete=models.CASCADE)
    image=models.ImageField(upload_to='publication/', blank=True)
    date_publication=models.DateTimeField(auto_now_add=True)
    
    def total_likes(self):
        return self.likes.count()

    class Meta:
        db_table='Publication'

class Like(models.Model):
    id = models.AutoField(primary_key=True)
    publication = models.ForeignKey(Publication, related_name='likes', on_delete=models.CASCADE)
    user = models.ForeignKey(CompteUtilisateur, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = 'Like'

class Commentaire(models.Model):
    id = models.AutoField(primary_key=True)
    publication = models.ForeignKey(Publication, related_name='comments', on_delete=models.CASCADE)
    user = models.ForeignKey(CompteUtilisateur, on_delete=models.CASCADE)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = 'Commentaire'
        
class Paiement(models.Model):
    code=models.AutoField(primary_key=True)
    apprenant=models.ForeignKey(Apprenant,on_delete=models.CASCADE)
    module=models.ForeignKey(Module,on_delete=models.CASCADE)
    montant=models.DecimalField(max_digits=10,decimal_places=2)
    date_paiement=models.DateTimeField()
    
    class Meta:
        db_table='Paiement'

class Questionnaire(models.Model):
    code=models.AutoField(primary_key=True)
    module=models.ForeignKey(Module, on_delete=models.CASCADE)
    question=models.TextField()
    reponse=models.TextField()
    maxima=models.IntegerField()
    
    class Meta:
        db_table='Questionnaire'

class Reponses_alternatives(models.Model):
    code = models.AutoField(primary_key=True)
    questionnaire = models.ForeignKey(Questionnaire, on_delete=models.CASCADE)
    reponse_alternative = models.CharField(max_length=255)

    class Meta:
        db_table='Reponses_alternatives'


class Test(models.Model):
    code=models.AutoField(primary_key=True)
    apprenant=models.ForeignKey(Apprenant,on_delete=models.CASCADE)
    questionnaire=models.ForeignKey(Questionnaire,on_delete=models.CASCADE)
    reponse_alternative = models.ForeignKey(Reponses_alternatives, on_delete=models.CASCADE)
    reponse=models.TextField()
    
    class Meta:
        db_table='Test'

class Interrogation(models.Model):
    code = models.AutoField(primary_key=True)
    titre = models.CharField(max_length=150)
    date_interro = models.DateField(auto_now=False, auto_now_add=False)
    duree = models.TimeField(auto_now=False, auto_now_add=False)
    module = models.ForeignKey(Module, on_delete=models.CASCADE)
    enseignant = models.ForeignKey(CompteUtilisateur, on_delete=models.CASCADE)

    class Meta:
        db_table = 'Interrogation'

class QuestionInterrogation(models.Model):
    code = models.AutoField(primary_key=True)
    enonce=models.TextField()
    interrogation = models.ForeignKey(Interrogation, on_delete=models.CASCADE)

    class Meta:
        db_table = 'QuestionInterrogation'

class Participation(models.Model):
    code = models.AutoField(primary_key=True)
    date_participation = models.DateField(auto_now=False, auto_now_add=False)
    cote_obtenu = models.DecimalField(max_digits=2, decimal_places=2)
    apprenant = models.ForeignKey(Apprenant, on_delete=models.CASCADE)
    interrogation = models.ForeignKey(Interrogation, on_delete=models.CASCADE)

    class Meta:
        db_table = 'Participation'

class ReponseInterrogation(models.Model):
    code = models.AutoField(primary_key=True)
    texte = models.TextField()
    # est_correcte = 
    question = models.ForeignKey(QuestionInterrogation, on_delete=models.CASCADE)

    class Meta:
        db_table = 'ReponseInterrogation'