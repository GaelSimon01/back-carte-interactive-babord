from django.test import TestCase, RequestFactory
from api_rest_babord.models import UtilisateurMobile, Groupe
from api_rest_babord.views.api_views import UtilisateurMobileViewSet
from api_rest_babord.views.auth_views import MobileUserLoginView
from rest_framework import status
import bcrypt

class UtilisateurMobileTest(TestCase):

    def setUp(self):
        self.factory = RequestFactory()
        password = bcrypt.hashpw("12345".encode('utf-8'), bcrypt.gensalt()).decode('utf-8')
        self.utilisateur = UtilisateurMobile.objects.create(
            password=password,
            nom='Test',
            prenom='Test',
            mail='test@gmail.com',
            ville = "Test ville",
            code_postal = "12345",
        )
        self.groupe = Groupe.objects.create(
            libelle="Test Groupe",
            description="Description du groupe de test",
            nb_homme=5,
            nb_femme=3,
            producteur="Test Producteur",
            lien_producteur="http://test.com",
            departement="00000",
        )
    
    def test_auth_mobile_user(self):
        request = self.factory.post('/api/mobile-login/', 
                                    {'mail': 'test@gmail.com',
                                     'password': '12345'
                                     })
        view = MobileUserLoginView.as_view()
        response = view(request)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['mail'], self.utilisateur.mail)

    def test_auth_mobile_user_wrong_password(self):
        request = self.factory.post('/api/mobile-login/', 
                                    {'mail': 'test@gmail.com',
                                     'password':'wrong_password'
                                     })
        view = MobileUserLoginView.as_view()
        response = view(request)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(response.data['type'], "bad_password")

    def test_auth_mobile_user_wrong_mail(self):
        request = self.factory.post('/api/mobile-login/', 
                                    {'mail': 'wrong@gmail.com',
                                     'password':'12345'
                                     })
        view = MobileUserLoginView.as_view()
        response = view(request)
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)
        self.assertEqual(response.data['type'], "unknow_email")

    def test_create_user(self):
        request = self.factory.post('/api/utilisateur-mobile/', 
                                    {'nom': 'Test2',
                                     'prenom':'Test2',
                                     'mail':'test2@gmail.com',
                                     'ville':'Test2 ville',
                                     'code_postal':'54321',
                                     'password':'abcdef',
                                     'suivre_groupe': []
                                     },
                                     headers={'permission': 'create_mobile_user'})
        view = UtilisateurMobileViewSet.as_view({'post':'create'})
        response = view(request)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.data['mail'], 'test2@gmail.com')
        self.assertEqual(response.data['ville'], 'Test2 ville')
        self.assertEqual(response.data['code_postal'], '54321')
        self.assertEqual(response.data['nom'], 'Test2')
        self.assertEqual(response.data['prenom'], 'Test2')
    

