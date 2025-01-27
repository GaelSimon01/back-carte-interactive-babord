from django.test import TestCase, RequestFactory
from api_rest_babord.models import Groupe
from api_rest_babord.views.api_views import GroupeViewSet
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
        self.groupe2 = Groupe.objects.create(
            libelle="groupe2",
            description="Description du groupe de test 2",
            nb_homme=5,
            nb_femme=3,
            producteur="Test Producteur 2",
            lien_producteur="http://test2.com",
            departement="22222",
        )


    def test_get_groupe_list(self):
        request = self.factory.get('/api/groupes/',headers={'permission': 'web_user'})
        view = GroupeViewSet.as_view({'get': 'list'})
        response = view(request)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data['results']), 3)
        self.assertEqual(response.data['results'][0]['libelle'], "Test Groupe")
    
    def test_get_groupe_detail(self):
        request = self.factory.get('/api/groupes/' + str(self.groupe.id) + '/',headers={'permission': 'web_user'})
        view = GroupeViewSet.as_view({'get': 'retrieve'})
        response = view(request, pk=self.groupe.id)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['libelle'], "Test Groupe")

    def test_create_groupe(self):
        data = {
            'libelle': 'New Groupe',
            'description': 'Description du nouveau groupe',
            'nb_homme': 4,
            'nb_femme': 6,
            'producteur': 'New Producteur',
            'lien_producteur': 'http://new.com',
            'departement': '22222'
        }
        request = self.factory.post('/api/groupes/', data, format='json',headers={'permission': 'web_user'})
        view = GroupeViewSet.as_view({'post': 'create'})
        response = view(request)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Groupe.objects.count(), 4)
        self.assertEqual(Groupe.objects.get(id=response.data['id']).libelle, 'New Groupe')

    def test_update_groupe(self):
        data = {
            'libelle': 'Updated Groupe',
            'description': 'Description du groupe mis à jour',
            'nb_homme': 4,
            'nb_femme': 6,
            'producteur': 'Updated Producteur',
            'lien_producteur': 'http://updated.com',
            'departement': '11111'
        }
        request = self.factory.put('/api/groupes/' + str(self.groupe.id) + '/', data, format='json',headers={'permission': 'web_user'}, content_type='application/json')
        view = GroupeViewSet.as_view({'put': 'update'})
        response = view(request, pk=self.groupe.id)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(Groupe.objects.get(id=self.groupe.id).libelle, 'Updated Groupe')
        self.assertEqual(Groupe.objects.get(id=self.groupe.id).producteur, 'Updated Producteur')
        self.assertEqual(Groupe.objects.get(id=self.groupe.id).departement, '11111')
        self.assertEqual(Groupe.objects.get(id=self.groupe.id).lien_producteur, 'http://updated.com')
        self.assertEqual(Groupe.objects.get(id=self.groupe.id).description, 'Description du groupe mis à jour')
        self.assertEqual(Groupe.objects.get(id=self.groupe.id).nb_homme, 4)
        self.assertEqual(Groupe.objects.get(id=self.groupe.id).nb_femme, 6)

    def test_delete_groupe(self):
        request = self.factory.delete('/api/groupes/' + str(self.groupe.id) + '/',headers={'permission': 'web_user'})
        view = GroupeViewSet.as_view({'delete': 'destroy'})
        response = view(request, pk=self.groupe.id)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Groupe.objects.count(), 2)

    def test_get_groupe_filter_libelle(self):
        request = self.factory.get('/api/groupes/', {'libelle': 'groupe1'},headers={'permission': 'web_user'})
        view = GroupeViewSet.as_view({'get': 'list'})
        response = view(request)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data['results']), 1)
        self.assertEqual(response.data['results'][0]['libelle'], 'groupe1')

    def test_get_groupe_filter_departement(self):
        request = self.factory.get('/api/groupes/', {'departement': '11111'},headers={'permission': 'web_user'})
        view = GroupeViewSet.as_view({'get': 'list'})
        response = view(request)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data['results']), 1)
        self.assertEqual(response.data['results'][0]['departement'], '11111')

    def test_get_groupe_filter_producteur(self):
        request = self.factory.get('/api/groupes/', {'producteur': 'Test Producteur 1'},headers={'permission': 'web_user'})
        view = GroupeViewSet.as_view({'get': 'list'})
        response = view(request)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data['results']), 1)
        self.assertEqual(response.data['results'][0]['producteur'], 'Test Producteur 1')