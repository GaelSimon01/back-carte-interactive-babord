from django.contrib.auth.models import Group, User
from rest_framework import permissions, viewsets
from rest_framework import filters


from api_rest_babord.serializers import *
from api_rest_babord.models import *

class GroupeViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows teachers to be viewed or edited.
    """
    queryset = Groupe.objects.all()
    serializer_class = GroupeSerializer
    permission_classes = [permissions.IsAuthenticated]

class UtilisateurViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows teachers to be viewed or edited.
    """
    queryset = Utilisateur.objects.all()
    serializer_class = UtilisateurSerializer
    permission_classes = [permissions.IsAuthenticated]


class AlbumViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows teachers to be viewed or edited.
    """
    queryset = Album.objects.all()
    serializer_class = AlbumSerializer
    permission_classes = [permissions.IsAuthenticated]

class ConcertViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows teachers to be viewed or edited.
    """
    queryset = Concert.objects.all()
    serializer_class = ConcertSerializer
    permission_classes = [permissions.IsAuthenticated]

class FestivalViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows teachers to be viewed or edited.
    """
    queryset = Festival.objects.all()
    serializer_class = FestivalSerializer
    permission_classes = [permissions.IsAuthenticated]

class InfoViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows teachers to be viewed or edited.
    """
    queryset = Info.objects.all()
    serializer_class = InfoSerializer
    permission_classes = [permissions.IsAuthenticated]

