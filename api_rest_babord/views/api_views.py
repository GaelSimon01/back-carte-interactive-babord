"""
Ce fichier contient les classes de vue de l'application api_rest_babord.
"""

from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import ModelViewSet
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters




from api_rest_babord.serializers import GroupeSerializer, \
    AlbumSerializer, ConcertSerializer, FestivalSerializer, InfoSerializer \
    , UtilisateurMobileSerializer

from api_rest_babord.models import Groupe, Album, Concert, Festival, Info, UtilisateurMobile

from api_rest_babord.permissions import WebUserPermission, MobileUserPermission, NewMobileUserPermission


class GroupeViewSet(ModelViewSet):
    """
    Classe de vue du modèle Groupe
    """

    queryset = Groupe.objects.all()
    serializer_class = GroupeSerializer

    filter_backends = [DjangoFilterBackend, filters.SearchFilter]
    search_fields = ['libelle', 'departement','producteur']
    filterset_fields = ['libelle', 'departement','producteur']
    
    def get_permissions(self):
        """
        Renvoie la liste des permissions en fonction de l'action
        """
        if  self.request.method in ['GET']:
            permission_classes = [WebUserPermission or MobileUserPermission]
        else:
            permission_classes = [WebUserPermission]
        return [permission() for permission in permission_classes]



class AlbumViewSet(ModelViewSet):
    """
    Classe de vue du modèle Album
    """

    queryset = Album.objects.all()
    serializer_class = AlbumSerializer

    filter_backends = [DjangoFilterBackend, filters.SearchFilter]
    search_fields = ['libelle', 'groupe__libelle', 'date_sortie', 'lieu']
    filterset_fields = ['libelle', 'groupe__libelle', 'date_sortie', 'lieu']
    
    def get_permissions(self):
        """
        Renvoie la liste des permissions en fonction de l'action
        """
        if  self.request.method in ['GET']:
            permission_classes = [WebUserPermission or MobileUserPermission]
        else:
            permission_classes = [WebUserPermission]
        return [permission() for permission in permission_classes]

class ConcertViewSet(ModelViewSet):
    """
    Classe de vue du modèle Concert
    """

    queryset = Concert.objects.all()
    serializer_class = ConcertSerializer

    filter_backends = [DjangoFilterBackend, filters.SearchFilter]
    search_fields = ['intitule', 'groupe__libelle', 'date_debut', 'lieu']
    filterset_fields = ['intitule', 'groupe__libelle', 'date_debut', 'lieu']
    
    def get_permissions(self):
        """
        Renvoie la liste des permissions en fonction de l'action
        """
        if  self.request.method in ['GET']:
            permission_classes = [WebUserPermission or MobileUserPermission]
        else:
            permission_classes = [WebUserPermission]
        return [permission() for permission in permission_classes]

class FestivalViewSet(ModelViewSet):
    """
    Classe de vue du modèle Festival
    """

    queryset = Festival.objects.all()
    serializer_class = FestivalSerializer

    filter_backends = [DjangoFilterBackend, filters.SearchFilter]
    search_fields = ['date_debut', 'lieu', 'concerts__intitule']
    filterset_fields = ['date_debut', 'lieu', 'concerts__intitule']
    
    def get_permissions(self):
        """
        Renvoie la liste des permissions en fonction de l'action
        """
        if  self.request.method in ['GET']:
            permission_classes = [WebUserPermission or MobileUserPermission]
        else:
            permission_classes = [WebUserPermission]
        return [permission() for permission in permission_classes]

class InfoViewSet(ModelViewSet):
    """
    Classe de vue du modèle Info
    """

    queryset = Info.objects.all()
    serializer_class = InfoSerializer

    filter_backends = [DjangoFilterBackend, filters.SearchFilter]
    search_fields = ['titre', 'type_info']
    filterset_fields = ['titre', 'type_info']
    
    def get_permissions(self):
        """
        Renvoie la liste des permissions en fonction de l'action
        """
        if  self.request.method in ['GET']:
            permission_classes = [WebUserPermission or MobileUserPermission]
        else:
            permission_classes = [WebUserPermission]
        return [permission() for permission in permission_classes]


class UtilisateurMobileViewSet(ModelViewSet):
    """
    Classe de vue du modèle UtilisateurMobile
    """

    queryset = UtilisateurMobile.objects.all()
    serializer_class = UtilisateurMobileSerializer

    def get_permissions(self):
        """
        Renvoie la liste des permissions en fonction de l'action
        """
        if self.action == 'create':
            permission_classes = [NewMobileUserPermission]
        else:
            permission_classes = [MobileUserPermission]
        return [permission() for permission in permission_classes]