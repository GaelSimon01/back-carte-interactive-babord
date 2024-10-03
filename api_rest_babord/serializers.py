from django.contrib.auth.models import Group, User
from rest_framework import serializers
from api_rest_babord.models import *


class GroupeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Groupe
        fields = ['libelle','description','nb_homme','nb_femme','date_creation']

class UtilisateurSerializer(serializers.ModelSerializer):
    class Meta:
        model = Utilisateur
        fields = ['nom_utilisateur','admin']

class LieuSerializer(serializers.ModelSerializer):
    class Meta:
        model = Lieu
        fields = ['latitude','logitude']

class AlbumSerializer(serializers.ModelSerializer):
    class Meta:
        model = Album
        fields = ['libelle','description']