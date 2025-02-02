from django.test import TestCase, RequestFactory
from api_rest_babord.models import Concert, Groupe
from api_rest_babord.views.api_views import ConcertViewSet
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
        self.concert2 = Concert.objects.create(
            intitule="concert2",
            date_debut="2023-01-01",
            lieu="Test Lieu 2",
            groupe=self.groupe
        )

    def test_get_concert_list(self):
        request = self.factory.get('/api/concerts/',headers={'permission': 'web_user'})
        view = ConcertViewSet.as_view({'get': 'list'})
        response = view(request)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data['results']), 3)
        self.assertEqual(response.data['results'][0]['intitule'], "Test Concert")

    def test_get_concert_detail(self):
        request = self.factory.get('/api/concerts/' + str(self.concert.id) + '/',headers={'permission': 'web_user'})
        view = ConcertViewSet.as_view({'get': 'retrieve'})
        response = view(request, pk=self.concert.id)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['intitule'], "Test Concert")

    def test_create_concert(self):
        data = {
            'intitule': 'New Concert',
            'date_debut': '2023-02-01',
            'lieu': 'New Lieu',
            'groupe': self.groupe.id
        }
        request = self.factory.post('/api/concerts/', data, format='json',headers={'permission': 'web_user'})
        view = ConcertViewSet.as_view({'post': 'create'})
        response = view(request)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Concert.objects.count(), 4)
        self.assertEqual(Concert.objects.get(id=response.data['id']).intitule, 'New Concert')

    def test_update_concert(self):
        data = {
            'intitule': 'Updated Concert',
            'date_debut': '2023-02-01',
            'lieu': 'New Lieu',
            'groupe': self.groupe.id
        }
        request = self.factory.put('/api/concerts/' + str(self.concert.id) + '/', data, format='json',headers={'permission': 'web_user'},content_type='application/json')
        view = ConcertViewSet.as_view({'put': 'update'})
        response = view(request, pk=self.concert.id)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(Concert.objects.get(id=self.concert.id).intitule, 'Updated Concert')
        self.assertEqual(Concert.objects.get(id=self.concert.id).lieu, 'New Lieu')

    def test_delete_concert(self):
        request = self.factory.delete('/api/concerts/' + str(self.concert.id) + '/',headers={'permission': 'web_user'})
        view = ConcertViewSet.as_view({'delete': 'destroy'})
        response = view(request, pk=self.concert.id)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Concert.objects.count(), 2)

    def test_get_concert_filter_intitule(self):
        request = self.factory.get('/api/concerts/', {'intitule': 'Test Concert'},headers={'permission': 'web_user'})
        view = ConcertViewSet.as_view({'get': 'list'})
        response = view(request)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data['results']), 1)
        self.assertEqual(response.data['results'][0]['intitule'], 'Test Concert')
    
    def test_get_concert_filter_groupe(self):
        request = self.factory.get('/api/concerts/', {'groupe__libelle': 'Test Groupe'},headers={'permission': 'web_user'})
        view = ConcertViewSet.as_view({'get': 'list'})
        response = view(request)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data['results']), 3)
        self.assertEqual(response.data['results'][0]['intitule'], 'Test Concert')

    def test_get_concert_filter_date_debut(self):
        request = self.factory.get('/api/concerts/', {'date_debut': '2023-01-01'},headers={'permission': 'web_user'})
        view = ConcertViewSet.as_view({'get': 'list'})
        response = view(request)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data['results']), 3)
        self.assertEqual(response.data['results'][0]['intitule'], 'Test Concert')

    def test_get_concert_filter_lieu(self):
        request = self.factory.get('/api/concerts/', {'lieu': 'Test Lieu'},headers={'permission': 'web_user'})
        view = ConcertViewSet.as_view({'get': 'list'})
        response = view(request)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data['results']), 1)
        self.assertEqual(response.data['results'][0]['intitule'], 'Test Concert')

    def test_get_concert_search(self):
        request = self.factory.get('/api/concerts/', {'q': 'Test Lieu'},headers={'permission': 'web_user'})
        view = ConcertViewSet.as_view({'get': 'list'})
        response = view(request)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data['results']), 3)
        self.assertEqual(response.data['results'][0]['intitule'], 'Test Concert')

    