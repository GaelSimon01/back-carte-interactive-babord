from django.contrib.auth.models import Group, User
from rest_framework import permissions, viewsets
from rest_framework import filters


from api_rest_babord.serializers import *
from api_rest_babord.models import *

class GroupeViewSet(viewsets.ReadOnlyModelViewSet):
    """
    API endpoint that allows teachers to be viewed or edited.
    """
    queryset = Groupe.objects.all()
    serializer_class = GroupeSerializer
    filter_backends = [filters.SearchFilter]
    # search_fields = ['libelle']
    filterset_fields = ['libelle']
    permission_classes = [permissions.IsAuthenticated]