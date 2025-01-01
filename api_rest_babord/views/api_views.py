"""
Ce fichier contient les classes de vue de l'application api_rest_babord.
"""

from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import ModelViewSet



from api_rest_babord.serializers import GroupeSerializer, \
    AlbumSerializer, ConcertSerializer, FestivalSerializer, InfoSerializer

from api_rest_babord.models import Groupe, Album, Concert, Festival, Info

class GroupeViewSet(ModelViewSet):
    """
    Classe de vue du modèle Groupe
    """

    queryset = Groupe.objects.all()
    serializer_class = GroupeSerializer
    permission_classes = [IsAuthenticated]



class AlbumViewSet(ModelViewSet):
    """
    Classe de vue du modèle Album
    """

    queryset = Album.objects.all()
    serializer_class = AlbumSerializer
    permission_classes = [IsAuthenticated]

class ConcertViewSet(ModelViewSet):
    """
    Classe de vue du modèle Concert
    """

    queryset = Concert.objects.all()
    serializer_class = ConcertSerializer
    permission_classes = [IsAuthenticated]

class FestivalViewSet(ModelViewSet):
    """
    Classe de vue du modèle Festival
    """

    queryset = Festival.objects.all()
    serializer_class = FestivalSerializer
    permission_classes = [IsAuthenticated]

class InfoViewSet(ModelViewSet):
    """
    Classe de vue du modèle Info
    """

    queryset = Info.objects.all()
    serializer_class = InfoSerializer
    permission_classes = [IsAuthenticated]
