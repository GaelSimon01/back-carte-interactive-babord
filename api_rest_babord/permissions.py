from rest_framework.permissions import BasePermission
from api_rest_babord.models import UtilisateurMobile



class WebUserPermission(BasePermission):
    """
    Permission pour les utilisateurs web
    """

    def has_permission(self, request, view):
        print(request.headers)
        return request.headers['permission'] == "web_user" # temporaire pour les tests
    

class MobileUserPermission(BasePermission):
    """
    Permission pour les utilisateurs mobiles
    """

    def has_permission(self, request, view):
        # Vérifie si l'utilisateur est un utilisateur mobile
        return UtilisateurMobile.objects.filter(mail=request.user.email).exists()