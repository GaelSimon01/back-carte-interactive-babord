from django.test import TestCase, RequestFactory
from api_rest_babord.models import Info
from api_rest_babord.views.api_views import InfoViewSet
from rest_framework import status

class InfoIntegrationTest(TestCase):

    def setUp(self):
        self.factory = RequestFactory()
        self.info = Info.objects.create(
            titre="Test Info",
            description="Description de l'info de test",
            nom_image="test_image.jpg",
            type_info="ACTU"
        )

    def test_get_info_list(self):
        request = self.factory.get('/api/infos/',headers={'permission': 'web_user'})
        view = InfoViewSet.as_view({'get': 'list'})
        response = view(request)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data['results']), 1)
        self.assertEqual(response.data['results'][0]['titre'], "Test Info")

    def test_get_info_detail(self):
        request = self.factory.get('/api/infos/' + str(self.info.id) + '/',headers={'permission': 'web_user'})
        view = InfoViewSet.as_view({'get': 'retrieve'})
        response = view(request, pk=self.info.id)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['titre'], "Test Info")

    def test_create_info(self):
        data = {
            'titre': 'New Info',
            'description': 'Description de la nouvelle info',
            'nom_image': 'new_image.jpg',
            'type_info': 'ACTU'
        }
        request = self.factory.post('/api/infos/', data, format='json',headers={'permission': 'web_user'})
        view = InfoViewSet.as_view({'post': 'create'})
        response = view(request)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Info.objects.count(), 2)
        self.assertEqual(Info.objects.get(id=response.data['id']).titre, 'New Info')

    def test_update_info(self):
        data = {
            'titre': 'Updated Info',
            'description': 'Description de l\'info mise à jour',
            'nom_image': 'updated_image.jpg',
            'type_info': 'ACTU'
        }
        request = self.factory.put('/api/infos/' + str(self.info.id) + '/', data, format='json',headers={'permission': 'web_user'}, content_type='application/json')
        view = InfoViewSet.as_view({'put': 'update'})
        response = view(request, pk=self.info.id)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(Info.objects.get(id=self.info.id).titre, 'Updated Info')
        self.assertEqual(Info.objects.get(id=self.info.id).nom_image, 'updated_image.jpg')

    def test_delete_info(self):
        request = self.factory.delete('/api/infos/' + str(self.info.id) + '/',headers={'permission': 'web_user'})
        view = InfoViewSet.as_view({'delete': 'destroy'})
        response = view(request, pk=self.info.id)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Info.objects.count(), 0)

    def test_get_info_filter_titre(self):
        request = self.factory.get('/api/infos/', {'titre': 'Test Info'},headers={'permission': 'web_user'})
        view = InfoViewSet.as_view({'get': 'list'})
        response = view(request)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data['results']), 1)

    def test_get_info_filter_type_info(self):
        request = self.factory.get('/api/infos/', {'type_info': 'ACTU'},headers={'permission': 'web_user'})
        view = InfoViewSet.as_view({'get': 'list'})
        response = view(request)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data['results']), 1)
        self.assertEqual(response.data['results'][0]['titre'], 'Test Info')