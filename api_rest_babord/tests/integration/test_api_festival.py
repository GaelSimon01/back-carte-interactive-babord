from django.test import TestCase, RequestFactory
from api_rest_babord.models import Festival, Concert, Groupe
from api_rest_babord.views import FestivalViewSet
from rest_framework.test import force_authenticate
from django.contrib.auth.models import User
from rest_framework import status
from datetime import date

class FestivalIntegrationTest(TestCase):

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
        self.festival = Festival.objects.create(
            date_debut="2023-01-01",
            lieu="Test Lieu",
            description="Description du festival de test"
        )
        self.festival.concerts.add(self.concert)

    def test_get_festival_list(self):
        request = self.factory.get('/api/festivals/')
        force_authenticate(request, user=self.user)
        view = FestivalViewSet.as_view({'get': 'list'})
        response = view(request)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)
        self.assertEqual(response.data[0]['description'], "Description du festival de test")

    def test_create_festival(self):
        data = {
            'date_debut': '2023-02-01',
            'lieu': 'New Lieu',
            'description': 'Description du nouveau festival',
            'concerts': [self.concert.id]
        }
        request = self.factory.post('/api/festivals/', data, format='json')
        force_authenticate(request, user=self.user)
        view = FestivalViewSet.as_view({'post': 'create'})
        response = view(request)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Festival.objects.count(), 2)
        self.assertEqual(Festival.objects.get(id=response.data['id']).description, 'Description du nouveau festival')