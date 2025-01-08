from django.test import TestCase, RequestFactory
from api_rest_babord.models import Festival, Concert, Groupe
from api_rest_babord.views.api_views import FestivalViewSet
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
            producteur="Test Producteur",
            lien_producteur="http://test.com",
            departement="00000",
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
        request = self.factory.get('/api/festivals/',headers={'permission': 'web_user'})
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
        request = self.factory.post('/api/festivals/', data, format='json',headers={'permission': 'web_user'})
        view = FestivalViewSet.as_view({'post': 'create'})
        response = view(request)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Festival.objects.count(), 2)
        self.assertEqual(Festival.objects.get(id=response.data['id']).description, 'Description du nouveau festival')

    def test_update_festival(self):
        data = {
            'date_debut': '2023-02-01',
            'lieu': 'New Lieu',
            'description': 'Description du festival mis à jour',
            'concerts': [self.concert.id]
        }
        request = self.factory.put('/api/festivals/' + str(self.festival.id) + '/', data, format='json',headers={'permission': 'web_user'}, content_type='application/json')
        view = FestivalViewSet.as_view({'put': 'update'})
        response = view(request, pk=self.festival.id)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(Festival.objects.get(id=self.festival.id).description, 'Description du festival mis à jour')
        self.assertEqual(Festival.objects.get(id=self.festival.id).lieu, 'New Lieu')
    
    def test_delete_festival(self):
        request = self.factory.delete('/api/festivals/' + str(self.festival.id) + '/',headers={'permission': 'web_user'})
        view = FestivalViewSet.as_view({'delete': 'destroy'})
        response = view(request, pk=self.festival.id)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Festival.objects.count(), 0)