"""
    Ce fichier contient les modèles de données de l'application.
"""
from datetime import date

from django.db import models


class Groupe(models.Model):
    """
    Classe de définition du modèle Groupe
    """

    libelle = models.CharField()
    description = models.CharField(blank=True, null=True)
    nb_homme = models.IntegerField(blank=True, null=True)
    nb_femme = models.IntegerField(blank=True, null=True)
    producteur = models.CharField(blank=True, null=True)
    lien_producteur = models.CharField(blank=True, null=True)
    departement = models.CharField(blank=True, null=True)

    def __str__(self):
        return self.libelle

class UtilisateurMobile(models.Model):
    """
    Classe de définition du modèle UtilisateurMobile
    """

    nom = models.CharField()
    prenom = models.CharField()
    mail = models.EmailField()
    password = models.CharField()
    ville = models.CharField(blank=True, null=True)
    code_postal = models.CharField(blank=True, null=True)
    suivre_groupe = models.ManyToManyField(Groupe)

class Album(models.Model):
    """
    Classe de définition du modèle Album
    """

    libelle = models.CharField()
    description = models.CharField()
    date_sortie = models.DateField(default=date.today())
    lieu = models.CharField(blank=True,null=True)
    groupe = models.ForeignKey(Groupe, on_delete=models.CASCADE)

    def __str__(self):
        return self.libelle

class Concert(models.Model):
    """
    Classe de définition du modèle Concert
    """
    intitule = models.CharField()
    date_debut = models.DateField(default=date.today())
    lieu = models.CharField(blank=True,null=True)
    groupe = models.ForeignKey(
        Groupe, on_delete=models.SET_NULL,blank=True,null=True, related_name='concerts'
    )

    def __str__(self):
        return self.intitule

class Festival(models.Model):
    """
    Classe de définition du modèle Festival
    """
    date_debut = models.DateField(default=date.today())
    lieu = models.CharField(blank=True,null=True)
    description = models.CharField()
    concerts = models.ManyToManyField(Concert)

    def __str__(self):
        return self.date_debut + " " + self.lieu + " (" + str(len(self.concerts.all())) +")"

type_info = [
    ("ACTU","Actualité"),
    ("INFO_DIVER","Information diverse")
]

class Info(models.Model):
    """
    Classe de définition du modèle Info
    """

    titre = models.CharField()
    description = models.CharField()
    nom_image = models.CharField()
    type_info = models.CharField(choices=type_info)

    def __str__(self):
        return self.titre
