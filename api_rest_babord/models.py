from django.db import models
from datetime import date, datetime
from django.contrib.auth.models import User

class Groupe(models.Model):
    libelle =models.CharField()
    description = models.CharField()
    nb_homme = models.IntegerField()
    nb_femme = models.IntegerField()
    date_creation = models.DateField(default=date.today())

class Utilisateur(models.Model):
    nom_utilisateur = models.CharField()
    admin = models.BooleanField(default=False)
    user = models.OneToOneField(User, on_delete=models.CASCADE, blank=True, null=True)
    groupe = models.ManyToManyField(Groupe)

class UtilisateurMobile(models.Model):
    nom = models.CharField()
    prenom = models.CharField()
    mail = models.EmailField()
    password = models.CharField()
    

class Lieu(models.Model):
    latitude = models.CharField()
    logitude = models.CharField()
    libelle_lieu = models.CharField()
    nom_image = models.CharField()

class Album(models.Model):
    libelle = models.CharField()
    description = models.CharField()
    date_sortie = models.DateField(default=date.today())
    lieux = models.ForeignKey(Lieu, on_delete=models.SET_NULL,blank=True,null=True)
    groupe = models.ForeignKey(Groupe, on_delete=models.CASCADE)

class Concert(models.Model):
    intitule = models.CharField()
    date_debut = models.DateField(default=date.today())
    lieu = models.ForeignKey(Lieu, on_delete=models.SET_NULL,blank=True,null=True)
    groupe = models.ForeignKey(Groupe, on_delete=models.SET_NULL,blank=True,null=True)

class Festival(models.Model):
    date_debut = models.DateField(default=date.today())
    lieux = models.ForeignKey(Lieu, on_delete=models.SET_NULL,blank=True,null=True)
    description = models.CharField()
    concerts = models.ManyToManyField(Concert)

type_info = [
    ("ACTU","Actualité"),
    ("INFO_DIVER","Information diverse"),
]

class Info(models.Model):
    titre = models.CharField()
    description = models.CharField()
    nom_image = models.CharField()
    type_info = models.CharField(choices=type_info)