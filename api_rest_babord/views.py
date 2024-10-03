from django.contrib.auth.models import Group, User
from rest_framework import permissions, viewsets

from api_rest_babord.serializers import *
from api_rest_babord.models import *

class GroupeViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows teachers to be viewed or edited.
    """
    queryset = Groupe.objects.all()
    serializer_class = GroupeSerializer
    permission_classes = [permissions.IsAuthenticated]