from django.test import TestCase
from api_rest_babord.models import Concert, Groupe
from datetime import date

class ConcertModelTest(TestCase):

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

    def test_concert_creation(self):
        self.assertEqual(self.concert.intitule, "Test Concert")
        self.assertEqual(str(self.concert.date_debut), "2023-01-01")
        self.assertEqual(self.concert.lieu, "Test Lieu")
        self.assertEqual(self.concert.groupe, self.groupe)

    def test_concert_str(self):
        self.assertEqual(str(self.concert), self.concert.intitule)

    def test_concert_update(self):
        self.concert.intitule = "Updated Concert"
        self.concert.date_debut = "2023-01-01"
        self.concert.lieu = "New Lieu"
        self.concert.save()
        self.assertEqual(self.concert.intitule, "Updated Concert")
        self.assertEqual(str(self.concert.date_debut), "2023-01-01")
        self.assertEqual(self.concert.lieu, "New Lieu")

    def test_concert_delete(self):
        self.concert.delete()
        self.assertEqual(Concert.objects.count(), 0)