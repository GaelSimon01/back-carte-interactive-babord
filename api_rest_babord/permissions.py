from rest_framework.permissions import BasePermission
from api_rest_babord.models import UtilisateurMobile



class WebUserPermission(BasePermission):
    """
    Permission pour les utilisateurs web
    """

    def has_permission(self, request, view):
        if("permission" in request.headers):
            # Vérifie si l'utilisateur est un utilisateur web
            return request.headers['permission'] == "web_user" # temporaire pour les tests
        else:
            return False
    
class NewMobileUserPermission(BasePermission):
    """
    Permission pour les utilisateurs mobiles
    """

    def has_permission(self, request, view):
        if("permission" in request.headers):
        # Vérifie si l'utilisateur est un utilisateur mobile
            return request.headers['permission'] == "create_mobile_user"
        else:
            return False
    

class MobileUserPermission(BasePermission):
    """
    Permission pour les utilisateurs mobiles
    """

    def has_permission(self, request, view):
        if("permission" in request.headers):
        # Vérifie si l'utilisateur est un utilisateur mobile
            return request.headers['permission'] == "mobile_user" and UtilisateurMobile.objects.filter(mail=request.user.email).exists()
        else:
            return False