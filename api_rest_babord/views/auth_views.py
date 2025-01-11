from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from api_rest_babord.models import UtilisateurMobile
from api_rest_babord.serializers import UtilisateurMobileSerializer
import bcrypt

class MobileUserLoginView(APIView):
    """
    Vue pour l'authentification des utilisateurs mobiles
    """
    authentication_classes = []
    permission_classes = []

    def post(self, request):
        mail = request.data.get('mail')
        password = request.data.get('password')

        try:
            user = UtilisateurMobile.objects.get(mail=mail)
        except UtilisateurMobile.DoesNotExist:
            return Response({"error": "Utilisateur non trouvé","type":"unknow_email"}, status=status.HTTP_404_NOT_FOUND)

        if bcrypt.checkpw(password.encode('utf-8'), user.password.encode('utf-8')):
            serializer = UtilisateurMobileSerializer(user)
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            return Response({"error": "Mot de passe incorrect", "type":"bad_password"}, status=status.HTTP_400_BAD_REQUEST)
        
    def get_queryset(self):
        return []