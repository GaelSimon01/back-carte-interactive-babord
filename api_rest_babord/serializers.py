"""
Ce fichier contient les classes de sérialisation des modèles de l'application api_rest_babord.
"""
import bcrypt
from rest_framework import serializers
from api_rest_babord.models import Groupe, Album, Concert, Festival, Info, UtilisateurMobile
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework_simplejwt.tokens import RefreshToken
from api_rest_babord.models import UtilisateurMobile

class UtilisateurMobileTokenObtainPairSerializer(TokenObtainPairSerializer):

    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)
        # Ajouter des claims personnalisés ici
        token['mail'] = user.mail
        return token

    def validate(self, attrs):
        try:
            user = UtilisateurMobile.objects.get(mail=attrs['mail'])
        except UtilisateurMobile.DoesNotExist:
            raise serializers.ValidationError('No active account found with the given credentials')

        if not user.check_password(attrs['password']):
            raise serializers.ValidationError('No active account found with the given credentials')

        refresh = self.get_token(user)

        data = {}
        data['refresh'] = str(refresh)
        data['access'] = str(refresh.access_token)

        return data

class GroupeSerializer(serializers.ModelSerializer):
    """
    Classe de sérialisation du modèle Groupe
    """
    class Meta:
        model = Groupe
        fields = ['id','libelle','description','nb_homme','nb_femme','producteur','lien_producteur','lien_twitter','lien_facebook','lien_youtube','lien_instagram','departement']
        

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

class UtilisateurMobileSerializer(serializers.ModelSerializer):
    """
    Classe de sérialisation du modèle UtilisateurMobile
    """

    class Meta:
        model = UtilisateurMobile
        fields = ['id','nom','prenom','mail','password','code_postal','suivre_groupe']

    def create(self, validated_data):
        """
        Création d'un utilisateur mobile avec mot de passe haché
        """
        # Hacher le mot de passe
        try : 
            UtilisateurMobile.objects.get(mail=validated_data['mail'])
            raise serializers.ValidationError('email_already_exists')
        except UtilisateurMobile.DoesNotExist:
            password = validated_data.pop('password')
            suivre_groupe = validated_data.pop('suivre_groupe')
            hashed_password = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())
            validated_data['password'] = hashed_password.decode('utf-8')
            
            # Créer l'utilisateur mobile et lui associer les groupes suivis
            utilisateur_mobile = UtilisateurMobile.objects.create(**validated_data)
            utilisateur_mobile.suivre_groupe.set(suivre_groupe)
            return utilisateur_mobile
        

        
        return UtilisateurMobile.objects.create(**validated_data)
    
    def delete(self, validated_data):
        """
        Suppression d'un utilisateur mobile
        """
        mail = validated_data.pop('mail')
        password = validated_data.pop('password')
        hashed_password = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())
        hash_password = hashed_password.decode('utf-8')
        user = UtilisateurMobile.objects.get(mail=mail,password=hash_password)
        user.delete()
        return user
    
    def update(self, instance, validated_data):
        """
        Mise à jour d'un utilisateur mobile
        """
        print(validated_data)
        if('password' in validated_data):
            password = validated_data.pop('password')
            hashed_password = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())
            instance.password = hashed_password.decode('utf-8')
        if('suivre_groupe' in validated_data):
            suivre_groupe = validated_data.pop('suivre_groupe')
            instance.suivre_groupe.set(suivre_groupe)
        if('nom' in validated_data):
            instance.nom = validated_data.pop('nom')
        if('prenom' in validated_data):
            instance.prenom = validated_data.pop('prenom')
        if('mail' in validated_data):
            instance.mail = validated_data.pop('mail')
        if('code_postal' in validated_data):
            instance.code_postal = validated_data.pop('code_postal')
        instance.save()
        return instance
    
    
    def get(self, instance, validated_data):
        """
        Récupération d'un utilisateur mobile
        """
        mail = validated_data.pop('mail')
        password = validated_data.pop('password')
        hashed_password = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())
        hash_password = hashed_password.decode('utf-8')
        user = UtilisateurMobile.objects.get(mail=mail,password=hash_password)
        return user
