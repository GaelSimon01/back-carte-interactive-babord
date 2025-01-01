from django.test import TestCase
from api_rest_babord.models import Info

class InfoModelTest(TestCase):

    def setUp(self):
        self.info = Info.objects.create(
            titre="Test Info",
            description="Description de l'info de test",
            nom_image="test_image.jpg",
            type_info="ACTU"
        )

    def test_info_creation(self):
        self.assertEqual(self.info.titre, "Test Info")
        self.assertEqual(self.info.description, "Description de l'info de test")
        self.assertEqual(self.info.nom_image, "test_image.jpg")
        self.assertEqual(self.info.type_info, "ACTU")

    def test_info_str(self):
        self.assertEqual(str(self.info), self.info.titre)