from django.db import models
from datetime import date, datetime

class Groupe(models.Model):
    libelle =models.CharField()
    description = models.CharField()
    nb_homme = models.IntegerField()
    nb_femme = models.IntegerField()
    date_creation = models.DateField(default=date.today())

class Utilisateur(models.Model):
    nom_utilisateur = models.IntegerField()
    mdp = models.CharField()
    adresse_mail = models.CharField(max_length=80)
    admin = models.BooleanField(default=False)
    groupe = models.ManyToManyField(Groupe)

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
    date_debut = models.DateField(default=date.today())
    lieux = models.ForeignKey(Lieu, on_delete=models.SET_NULL,blank=True,null=True)
    groupe = models.ForeignKey(Groupe, on_delete=models.SET_NULL,blank=True,null=True)
    groupe = models.ForeignKey(Groupe, on_delete=models.CASCADE)

class Festival(models.Model):
    date_debut = models.DateField(default=date.today())
    lieux = models.ForeignKey(Lieu, on_delete=models.SET_NULL,blank=True,null=True)
    description = models.CharField()
    concerts = models.ManyToManyField(Concert)

type_info = {
    "ACTU" : "Actualité",
    "INFO_DIVER" : "Information diverse",
}

class Info(models.Model):
    titre = models.CharField()
    description = models.CharField()
    nom_image = models.CharField()
    type_info = models.CharField(choices=type_info)