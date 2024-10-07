# create_superuser.py
import os
from django.contrib.auth import get_user_model
from django.db.utils import IntegrityError
import os
import django

# Définissez le module de paramètres
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'babord_project.settings')

# Configurez Django
django.setup()



User = get_user_model()

USERNAME = os.getenv("DJANGO_SUPERUSER_USERNAME")
EMAIL = os.getenv("DJANGO_SUPERUSER_EMAIL")
PASSWORD = os.getenv("DJANGO_SUPERUSER_PASSWORD")

try:
    User.objects.create_superuser(USERNAME, EMAIL, PASSWORD)
    print(f"Superuser {USERNAME} created successfully.")
except IntegrityError:
    print(f"Superuser {USERNAME} already exists.")
