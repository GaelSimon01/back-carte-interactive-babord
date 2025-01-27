# Utiliser une image officielle Python comme base
FROM python:3.10-slim

# Définir le répertoire de travail à l'intérieur du conteneur
WORKDIR /work

# Copier les fichiers requirements
COPY requirements.txt /work

# Installer les dépendances
RUN pip install --no-cache-dir -r requirements.txt

# Copier le code du projet Django
COPY . /work/

# Exposer le port que Django utilisera
EXPOSE 8000

# Commande pour migrer la base de données et 
CMD ["bash", "-c", "python manage.py migrate && python manage.py collectstatic --noinput && python manage.py runserver 0.0.0.0:8000"]



