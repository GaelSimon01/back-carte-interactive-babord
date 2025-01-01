from django.test import TestCase, RequestFactory
from api_rest_babord.models import Info
from api_rest_babord.views import InfoViewSet
from rest_framework.test import force_authenticate
from django.contrib.auth.models import User
from rest_framework import status

class InfoIntegrationTest(TestCase):

    def setUp(self):
        self.factory = RequestFactory()
        self.user = User.objects.create_user(username='testuser', password='12345')
        self.info = Info.objects.create(
            titre="Test Info",
            description="Description de l'info de test",
            nom_image="test_image.jpg",
            type_info="ACTU"
        )

    def test_get_info_list(self):
        request = self.factory.get('/api/infos/')
        force_authenticate(request, user=self.user)
        view = InfoViewSet.as_view({'get': 'list'})
        response = view(request)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)
        self.assertEqual(response.data[0]['titre'], "Test Info")

    def test_create_info(self):
        data = {
            'titre': 'New Info',
            'description': 'Description de la nouvelle info',
            'nom_image': 'new_image.jpg',
            'type_info': 'ACTU'
        }
        request = self.factory.post('/api/infos/', data, format='json')
        force_authenticate(request, user=self.user)
        view = InfoViewSet.as_view({'post': 'create'})
        response = view(request)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Info.objects.count(), 2)
        self.assertEqual(Info.objects.get(id=response.data['id']).titre, 'New Info')