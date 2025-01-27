from django.test import TestCase, RequestFactory
from api_rest_babord.models import Album, Groupe
from api_rest_babord.views.api_views import AlbumViewSet
from django.contrib.auth.models import User
from rest_framework import status
from datetime import date

class AlbumIntegrationTest(TestCase):

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
        self.groupe1 = Groupe.objects.create(
            libelle="groupe1",
            description="Description du groupe de test 1",
            nb_homme=5,
            nb_femme=3,
            producteur="Test Producteur 1",
            lien_producteur="http://test1.com",
            departement="11111",
        )
        self.album = Album.objects.create(
            libelle="Test Album",
            description="Description de l'album de test",
            date_sortie=date.today(),
            lieu="Test Lieu",
            groupe=self.groupe
        )
        self.album1 = Album.objects.create(
            libelle="album1",
            description="Description de l'album de test 1",
            date_sortie=date.today(),
            lieu="Test Lieu 1",
            groupe=self.groupe
        )
        self.album2 = Album.objects.create(
            libelle="album2",
            description="Description de l'album de test 2",
            date_sortie=date.today(),
            lieu="Test Lieu 2",
            groupe=self.groupe1
        )

    def test_get_album_list(self):
        request = self.factory.get('/api/albums/',headers={'permission': 'web_user'})
        view = AlbumViewSet.as_view({'get': 'list'})
        response = view(request)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 3)
        self.assertEqual(response.data[0]['libelle'], "Test Album")

    def test_create_album(self):
        data = {
            'libelle': 'New Album',
            'description': 'Description du nouvel album',
            'date_sortie': '2023-02-01',
            'lieu': 'New Lieu',
            'groupe': self.groupe.id
        }
        request = self.factory.post('/api/albums/', data, format='json', headers={'permission': 'web_user'})
        view = AlbumViewSet.as_view({'post': 'create'})
        response = view(request)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Album.objects.count(), 4)
        self.assertEqual(Album.objects.get(id=response.data['id']).libelle, 'New Album')

    def test_update_album(self):
        data = {
            'libelle': 'Updated Album',
            'description': 'Description de l\'album mis à jour',
            'date_sortie': '2023-02-01',
            'lieu': 'New Lieu',
            'groupe': self.groupe.id
        }
        request = self.factory.put(f'/api/albums/{self.album.id}/', data, format='json', headers={'permission': 'web_user'}, content_type='application/json')
        view = AlbumViewSet.as_view({'put': 'update'})
        response = view(request, pk=self.album.id)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(Album.objects.get(id=self.album.id).libelle, 'Updated Album')

    def test_delete_album(self):
        request = self.factory.delete(f'/api/albums/{self.album.id}/', headers={'permission': 'web_user'})
        view = AlbumViewSet.as_view({'delete': 'destroy'})
        response = view(request, pk=self.album.id)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Album.objects.count(), 2)

    def test_get_album_filter_libelle(self):
        request = self.factory.get('/api/albums/', {'libelle': 'Test Album'}, headers={'permission': 'web_user'})
        view = AlbumViewSet.as_view({'get': 'list'})
        response = view(request)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)
        self.assertEqual(response.data[0]['libelle'], 'Test Album')

    def test_get_album_filter_groupe(self):
        request = self.factory.get('/api/albums/', {'groupe__libelle': 'Test Groupe'}, headers={'permission': 'web_user'})
        view = AlbumViewSet.as_view({'get': 'list'})
        response = view(request)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 2)
        self.assertEqual(response.data[0]['libelle'], 'Test Album')

    def test_get_album_filter_date_sortie(self):
        request = self.factory.get('/api/albums/', {'date_sortie': date.today()}, headers={'permission': 'web_user'})
        view = AlbumViewSet.as_view({'get': 'list'})
        response = view(request)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 3)
        self.assertEqual(response.data[0]['libelle'], 'Test Album')

    def test_get_album_filter_lieu(self):
        request = self.factory.get('/api/albums/', {'lieu': 'Test Lieu'}, headers={'permission': 'web_user'})
        view = AlbumViewSet.as_view({'get': 'list'})
        response = view(request)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)
        self.assertEqual(response.data[0]['lieu'], 'Test Lieu')