from django.test import TestCase
from api_rest_babord.models import Groupe

class GroupeModelTest(TestCase):

    def setUp(self):
        self.groupe = Groupe.objects.create(
            libelle="Test Groupe",
            description="Description du groupe de test",
            nb_homme=5,
            nb_femme=3,
            date_creation="2023-01-01"
        )

    def test_groupe_creation(self):
        self.assertEqual(self.groupe.libelle, "Test Groupe")
        self.assertEqual(self.groupe.description, "Description du groupe de test")
        self.assertEqual(self.groupe.nb_homme, 5)
        self.assertEqual(self.groupe.nb_femme, 3)
        self.assertEqual(str(self.groupe.date_creation), "2023-01-01")

    def test_groupe_str(self):
        self.assertEqual(str(self.groupe), self.groupe.libelle)

    