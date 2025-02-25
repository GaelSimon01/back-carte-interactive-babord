from django.test import TestCase
from api_rest_babord.models import Festival, Concert, Groupe
from datetime import date

class FestivalModelTest(TestCase):

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
        self.concert = Concert.objects.create(
            intitule="Test Concert",
            date_debut="2023-01-01",
            lieu="Test Lieu",
            groupe=self.groupe
        )
        self.festival = Festival.objects.create(
            date_debut="2023-01-01",
            lieu="Test Lieu",
            description="Description du festival de test"
        )
        self.festival.concerts.add(self.concert)

    def test_festival_creation(self):
        self.assertEqual(str(self.festival.date_debut), "2023-01-01")
        self.assertEqual(self.festival.lieu, "Test Lieu")
        self.assertEqual(self.festival.description, "Description du festival de test")
        self.assertIn(self.concert, self.festival.concerts.all())

    def test_festival_str(self):
        expected_str = f"{self.festival.date_debut} {self.festival.lieu} ({str(len(self.festival.concerts.all()))})"
        self.assertEqual(str(self.festival), expected_str)

    def test_festival_update(self):
        self.festival.date_debut = "2023-02-01"
        self.festival.lieu = "New Lieu"
        self.festival.save()
        self.assertEqual(str(self.festival.date_debut), "2023-02-01")
        self.assertEqual(self.festival.lieu, "New Lieu")

    def test_festival_delete(self):
        self.festival.delete()
        self.assertEqual(Festival.objects.count(), 0)