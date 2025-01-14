from django.test import TestCase
from api_rest_babord.models import UtilisateurMobile
from datetime import date
import bcrypt

class UtilisateurMobileModelTest(TestCase):

    def setUp(self):
        self.utilisateur_mobile = UtilisateurMobile.objects.create(
            nom="Test Nom",
            prenom="Test Prenom",
            mail="test@gmail.com",
            password=bcrypt.hashpw("12345".encode('utf-8'), bcrypt.gensalt()).decode('utf-8'),
            ville="Test Ville",
            code_postal="12345"
        )



    def test_Utilisateur_mobile_creation(self):
        self.assertEqual(self.utilisateur_mobile.nom, "Test Nom")
        self.assertEqual(self.utilisateur_mobile.prenom, "Test Prenom")
        self.assertEqual(self.utilisateur_mobile.mail, "test@gmail.com")
        self.assertEqual(self.utilisateur_mobile.ville, "Test Ville")
        self.assertEqual(self.utilisateur_mobile.code_postal, "12345")
        
    def test_Utilisateur_mobile_str(self):
        self.assertEqual(str(self.utilisateur_mobile), self.utilisateur_mobile.nom + " " + self.utilisateur_mobile.prenom + " "+ self.utilisateur_mobile.mail)

    def test_Utilisateur_mobile_update(self):
        self.utilisateur_mobile.nom = "Updated Nom"
        self.utilisateur_mobile.prenom = "Updated Prenom"
        self.utilisateur_mobile.mail = "TestUpdate@gmail.com"
        self.utilisateur_mobile.ville = "Updated Ville"
        self.utilisateur_mobile.code_postal = "54321"
        self.utilisateur_mobile.save()
        self.assertEqual(self.utilisateur_mobile.nom, "Updated Nom")
        self.assertEqual(self.utilisateur_mobile.prenom, "Updated Prenom")
        self.assertEqual(self.utilisateur_mobile.mail, "TestUpdate@gmail.com")
        self.assertEqual(self.utilisateur_mobile.ville, "Updated Ville")
        self.assertEqual(self.utilisateur_mobile.code_postal, "54321")
                         
    def test_Utilisateur_mobile_delete(self):
        self.utilisateur_mobile.delete()
        self.assertEqual(UtilisateurMobile.objects.count(), 0)