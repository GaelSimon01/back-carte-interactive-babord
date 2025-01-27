from django.test import TestCase, RequestFactory
from api_rest_babord.models import Festival, Concert, Groupe
from api_rest_babord.views.api_views import FestivalViewSet
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
        self.concert1 = Concert.objects.create(
            intitule="concert1",
            date_debut="2023-01-01",
            lieu="Test Lieu 1",
            groupe=self.groupe
        )
        self.festival = Festival.objects.create(
            date_debut="2023-01-01",
            lieu="Test Lieu",
            description="Description du festival de test"
        )
        self.festival1 = Festival.objects.create(
            date_debut="2023-03-01",
            lieu="Test Lieu 1",
            description="Description du festival de test 1"
        )
        self.festival.concerts.add(self.concert)
        self.festival1.concerts.add(self.concert1)

    def test_get_festival_list(self):
        request = self.factory.get('/api/festivals/',headers={'permission': 'web_user'})
        view = FestivalViewSet.as_view({'get': 'list'})
        response = view(request)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data['results']), 2)
        self.assertEqual(response.data['results'][0]['description'], "Description du festival de test")

    def test_get_festival_detail(self):
        request = self.factory.get('/api/festivals/' + str(self.festival.id) + '/',headers={'permission': 'web_user'})
        view = FestivalViewSet.as_view({'get': 'retrieve'})
        response = view(request, pk=self.festival.id)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['description'], "Description du festival de test")

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
        self.assertEqual(Festival.objects.count(), 3)
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
        self.assertEqual(Festival.objects.count(), 1)

    def test_get_festival_filter_lieu(self):
        request = self.factory.get('/api/festivals/', {'lieu': 'Test Lieu'},headers={'permission': 'web_user'})
        view = FestivalViewSet.as_view({'get': 'list'})
        response = view(request)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data['results']), 1)
        self.assertEqual(response.data['results'][0]['lieu'], 'Test Lieu')
    
    def test_get_festival_filter_concerts(self):
        request = self.factory.get('/api/festivals/', {'concerts__intitule': 'Test Concert'},headers={'permission': 'web_user'})
        view = FestivalViewSet.as_view({'get': 'list'})
        response = view(request)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data['results']), 1)
        self.assertEqual(response.data['results'][0]['lieu'], 'Test Lieu')

    def test_get_festival_filter_date_debut(self):
        request = self.factory.get('/api/festivals/', {'date_debut': '2023-01-01'},headers={'permission': 'web_user'})
        view = FestivalViewSet.as_view({'get': 'list'})
        response = view(request)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data['results']), 1)
    
    