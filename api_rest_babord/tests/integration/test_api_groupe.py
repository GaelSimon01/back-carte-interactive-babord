from django.test import TestCase, RequestFactory
from api_rest_babord.models import Groupe
from api_rest_babord.views.api_views import GroupeViewSet
from rest_framework.test import force_authenticate
from django.contrib.auth.models import User
from rest_framework import status
from datetime import date

class GroupeIntegrationTest(TestCase):

    def setUp(self):
        self.factory = RequestFactory()
        self.user = User.objects.create_user(username='testuser', password='12345')
        self.groupe = Groupe.objects.create(
            libelle="Test Groupe",
            description="Description du groupe de test",
            nb_homme=5,
            nb_femme=3,
            date_creation="2023-01-01"
        )

    def test_get_groupe_list(self):
        request = self.factory.get('/api/groupes/')
        request.headers.permission = 'web_user'
        view = GroupeViewSet.as_view({'get': 'list'})
        response = view(request)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)
        self.assertEqual(response.data[0]['libelle'], "Test Groupe")

    def test_create_groupe(self):
        data = {
            'libelle': 'New Groupe',
            'description': 'Description du nouveau groupe',
            'nb_homme': 4,
            'nb_femme': 6,
            'date_creation': '2023-02-01'
        }
        request = self.factory.post('/api/groupes/', data, format='json')
        force_authenticate(request, user=self.user)
        view = GroupeViewSet.as_view({'post': 'create'})
        response = view(request)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Groupe.objects.count(), 2)
        self.assertEqual(Groupe.objects.get(id=response.data['id']).libelle, 'New Groupe')