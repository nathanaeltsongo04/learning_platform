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

class Module(models.Model):
    code=models.AutoField(primary_key=True)
    titre=models.CharField(max_length=25)
    description=models.TextField()
    prix=models.DecimalField(max_digits=10, decimal_places=2)
    niveau=models.ForeignKey(Niveau,on_delete=models.CASCADE)
    ressource=models.ForeignKey(Ressource,on_delete=models.CASCADE)
    
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
    formation=models.ForeignKey(Formation,on_delete=models.CASCADE)
    modalite=models.ForeignKey(ModalitePaie,on_delete=models.CASCADE)
    date_inscription=models.DateTimeField()
    
    class Meta:
        db_table='Inscription'
        
class Evaluation(models.Model):
    code=models.AutoField(primary_key=True)
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
    titre=models.CharField(max_length=50)
    description=models.TextField()
    compte_utilisateur=models.ForeignKey(CompteUtilisateur,on_delete=models.CASCADE)
    date_publication=models.DateTimeField()
    
    class Meta:
        db_table='Publication'
        
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
    
    class Meta:
        db_table='Questionnaire'
            
class Test(models.Model):
    code=models.AutoField(primary_key=True)
    apprenant=models.ForeignKey(Apprenant,on_delete=models.CASCADE)
    questionnaire=models.ForeignKey(Questionnaire,on_delete=models.CASCADE)
    reponse=models.TextField()
    
    class Meta:
        db_table='Test'