from django.test import TestCase, RequestFactory
from api_rest_babord.models import Concert, Groupe
from api_rest_babord.views.api_views import ConcertViewSet
from rest_framework.test import force_authenticate
from django.contrib.auth.models import User
from rest_framework import status
from datetime import date

class ConcertIntegrationTest(TestCase):

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
        self.concert = Concert.objects.create(
            intitule="Test Concert",
            date_debut="2023-01-01",
            lieu="Test Lieu",
            groupe=self.groupe
        )

    def test_get_concert_list(self):
        request = self.factory.get('/api/concerts/')
        force_authenticate(request, user=self.user)
        view = ConcertViewSet.as_view({'get': 'list'})
        response = view(request)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)
        self.assertEqual(response.data[0]['intitule'], "Test Concert")

    def test_create_concert(self):
        data = {
            'intitule': 'New Concert',
            'date_debut': '2023-02-01',
            'lieu': 'New Lieu',
            'groupe': self.groupe.id
        }
        request = self.factory.post('/api/concerts/', data, format='json')
        force_authenticate(request, user=self.user)
        view = ConcertViewSet.as_view({'post': 'create'})
        response = view(request)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Concert.objects.count(), 2)
        self.assertEqual(Concert.objects.get(id=response.data['id']).intitule, 'New Concert')