from django.test import TestCase
from api_rest_babord.models import Groupe

class GroupeModelTest(TestCase):

    def setUp(self):
        self.groupe = Groupe.objects.create(
            libelle="Test Groupe",
            description="Description du groupe de test",
            nb_homme=5,
            nb_femme=3,
            producteur="Test Producteur",
            lien_producteur="http://test.com",
            departement="00000",
        )

    def test_groupe_creation(self):
        self.assertEqual(self.groupe.libelle, "Test Groupe")
        self.assertEqual(self.groupe.description, "Description du groupe de test")
        self.assertEqual(self.groupe.nb_homme, 5)
        self.assertEqual(self.groupe.nb_femme, 3)
        self.assertEqual(self.groupe.producteur, "Test Producteur")
        self.assertEqual(self.groupe.lien_producteur, "http://test.com")
        self.assertEqual(self.groupe.departement, "00000")

    def test_groupe_str(self):
        self.assertEqual(str(self.groupe), self.groupe.libelle)

    def test_groupe_update(self):
        self.groupe.libelle = "Updated Groupe"
        self.groupe.description = "Description du groupe mis à jour"
        self.groupe.nb_homme = 4
        self.groupe.nb_femme = 6
        self.groupe.producteur = "New Producteur"
        self.groupe.lien_producteur = "http://new.com"
        self.groupe.departement = "22222"
        self.groupe.save()
        self.assertEqual(self.groupe.libelle, "Updated Groupe")
        self.assertEqual(self.groupe.description, "Description du groupe mis à jour")
        self.assertEqual(self.groupe.nb_homme, 4)
        self.assertEqual(self.groupe.nb_femme, 6)
        self.assertEqual(self.groupe.producteur, "New Producteur")
        self.assertEqual(self.groupe.lien_producteur, "http://new.com")
        self.assertEqual(self.groupe.departement, "22222")

    def test_groupe_delete(self):
        self.groupe.delete()
        self.assertEqual(Groupe.objects.count(), 0)

    