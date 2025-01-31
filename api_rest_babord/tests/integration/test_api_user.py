from django.test import TestCase, RequestFactory
from api_rest_babord.models import UtilisateurMobile, Groupe
from api_rest_babord.views.api_views import UtilisateurMobileViewSet
from api_rest_babord.views.auth_views import MobileUserLoginView
from rest_framework import status
import bcrypt
import json
class UtilisateurMobileTest(TestCase):

    def setUp(self):
        self.factory = RequestFactory()
        password = bcrypt.hashpw("12345".encode('utf-8'), bcrypt.gensalt()).decode('utf-8')
        self.utilisateur = UtilisateurMobile.objects.create(
            password=password,
            nom='Test',
            prenom='Test',
            mail='test@gmail.com',
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
        request = self.factory.post('/api/Utilisateur/', 
                                    {'nom': 'Test2',
                                     'prenom':'Test2',
                                     'mail':'test2@gmail.com',
                                     'code_postal':"28000",
                                     'password':'abcdef'
                                     },
                                     headers={'permission': 'create_mobile_user'})
        view = UtilisateurMobileViewSet.as_view({'post':'create'})
        response = view(request)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.data['mail'], 'test2@gmail.com')
        self.assertEqual(response.data['code_postal'], '28000')
        self.assertEqual(response.data['nom'], 'Test2')
        self.assertEqual(response.data['prenom'], 'Test2')

    def test_partial_update_user(self):
        data = {
                "nom": 'Test2',
                "prenom":'Test2',
                "suivre_groupe": [self.groupe.id]
        }
        request = self.factory.patch('/api/Utilisateur/' + str(self.utilisateur.id) + '/', 
                                    data = json.dumps(data),headers={"permission": 'mobile_user','content-type': 'application/json'})
        view = UtilisateurMobileViewSet.as_view({'patch':'partial_update'})
        response = view(request, pk=self.utilisateur.id)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['nom'], 'Test2')
        self.assertEqual(response.data['prenom'], 'Test2')
        self.assertEqual(response.data['suivre_groupe'][0], self.groupe.id)
    

