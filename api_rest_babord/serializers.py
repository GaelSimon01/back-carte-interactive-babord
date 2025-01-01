"""
Ce fichier contient les classes de sérialisation des modèles de l'application api_rest_babord.
"""

from rest_framework import serializers
from api_rest_babord.models import Groupe, Album, Concert, Festival, Info


class GroupeSerializer(serializers.ModelSerializer):
    """
    Classe de sérialisation du modèle Groupe
    """
    class Meta:
        model = Groupe
        fields = ['id','libelle','description','nb_homme','nb_femme','date_creation']

class AlbumSerializer(serializers.ModelSerializer):
    """
    Classe de sérialisation du modèle Album
    """
    class Meta:
        model = Album
        fields = ['id','libelle','description','date_sortie','lieu','groupe']

class ConcertSerializer(serializers.ModelSerializer):
    """
    Classe de sérialisation du modèle Concert
    """
    class Meta:
        model = Concert
        fields = ['id','intitule','date_debut','lieu','groupe']

class FestivalSerializer(serializers.ModelSerializer):
    """
    Classe de sérialisation du modèle Festival
    """
    class Meta:
        model = Festival
        fields = ['id','date_debut','lieu','description','concerts']

class InfoSerializer(serializers.ModelSerializer):
    """
    Classe de sérialisation du modèle Info
    """
    class Meta:
        model = Info
        fields = ['id','titre','description','nom_image','type_info']
