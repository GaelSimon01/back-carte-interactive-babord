from django.contrib.auth.models import Group, User
from rest_framework import serializers
from api_rest_babord.models import *


class GroupeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Groupe
        fields = ['libelle','description','nb_homme','nb_femme','date_creation']


class UtilisateurSerializer(serializers.ModelSerializer):
    groupe = GroupeSerializer(many=True)
    
    class Meta:
        model = Utilisateur
        fields = ['nom_utilisateur','admin','groupe','adresse_mail']

class AlbumSerializer(serializers.ModelSerializer):
    class Meta:
        model = Album
        fields = ['libelle','description','date_sortie','lieux','groupe']

class ConcertSerializer(serializers.ModelSerializer):
    class Meta:
        model = Concert
        fields = ['date_debut','lieux','groupe']

class FestivalSerializer(serializers.ModelSerializer):
    class Meta:
        model = Festival
        fields = ['date_debut','lieux','description','concerts']

class InfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Info
        fields = ['titre','description','nom_image','type_info']
