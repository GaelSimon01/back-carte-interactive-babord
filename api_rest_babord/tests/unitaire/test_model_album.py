from django.test import TestCase
from api_rest_babord.models import Album, Groupe
from datetime import date

class AlbumModelTest(TestCase):

    def setUp(self):
        self.groupe = Groupe.objects.create(
            libelle="Test Groupe",
            description="Description du groupe de test",
            nb_homme=5,
            nb_femme=3,
            date_creation="2023-01-01"
        )
        self.album = Album.objects.create(
            libelle="Test Album",
            description="Description de l'album de test",
            date_sortie=date.today(),
            lieu="Test Lieu",
            groupe=self.groupe
        )

    def test_album_creation(self):
        self.assertEqual(self.album.libelle, "Test Album")
        self.assertEqual(self.album.description, "Description de l'album de test")
        self.assertEqual(self.album.date_sortie, date.today())
        self.assertEqual(self.album.lieu, "Test Lieu")
        self.assertEqual(self.album.groupe, self.groupe)

    def test_album_str(self):
        self.assertEqual(str(self.album), self.album.libelle)