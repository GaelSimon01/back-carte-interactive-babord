# Projets Babord

Ce document a pour but de décrire comment installer et lancer le projet Babord aussi bien en local que sur un serveu (via docker).

Cette API est une API REST permettant de récupérer les informations des artistes et des événements du label Babord.
Elle à été réaliser avec Django et Django Rest Framework dont voici les documentations : https://docs.djangoproject.com/fr/5.1/ et https://www.django-rest-framework.org/

## Installation en local

Pour installer le projet, il faut cloner le projet et installer les dépendances.

```bash
git clone
cd babord_project
pip install -r requirements.txt
```

De plus il faut installer la dépendance suivante pour la base de données  ( Attention a ne pas l'inculre dans le requirements.txt car elle ferait planter le docker lors du build):

```bash
pip install psycopg2
```

### Configuration de la base de données

Dans le settings.py, il faut modifier les informations de la base de données pour qu'elles correspondent à votre base de données utiliser pour le dévellopement.

```py
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql', # moteur de BDD ( postgresql )
        'NAME': "", # nom de la base de données
        'USER': "", # utilisateur
        'PASSWORD': "", # mot de passe
        'HOST': "localhost", # adresse de la base de données
        'PORT': "5432", # port de la base de données (5432 car postgres)
    }
}
```

### Lancement du serveur

Pour lancer le serveur, il faut exécuter la commande suivante :

```bash
./manage.py runserver
```

### Création de la base de données

Pour créer la base de données, il faut exécuter la commande suivante :

```bash
./manage.py makemigrations <nom_app> # nom_app n'est pas obligatoire
./manage.py migrate
```

## Installation avec docker

Pour installer le projet avec docker, il faut cloner le projet et lancer la commande suivante :

```bash
docker-compose up --build
```
L'API est lancer automatiquement sur le port 8000 a l'adresse suivante : http://localhost:8000/api


## Commande pour effectuer les tests

### test unitaire
aucune installation n'est necessaire pour effectuer les test unitaire 

Pour lancer les test unitaire  : 
```bash
./manage.py test api_rest_babord.tests.unitaire
```
### test d'intégration
aucune installation n'est necessaire pour effectuer les test d'intégration
Pour lancer les test d'intégration  : 
```bash
./manage.py test api_rest_babord.tests.integration
```

### lancer un coverage
il faut installer le package coverage pour effectuer les test de couverture de code

```bash
pip install coverage
```

Pour lancer le coverage de l'api : 
```bash
coverage run --source='api_rest_babord' manage.py test
```

Pour afficher le coverage : 
```bash
coverage report
```

### test de performance
il faut installer le package hey pour effectuer les test de performance

#### installation de hey

installation avec go : 
```bash
go get -u github.com/rakyll/hey
```

installation avec brew : 
```bash
brew install hey
```

installation avec apt : 
```bash
sudo apt-get install hey
```

Pour effectuer les test de performance ( 1000 requetes avec 100 connections simultanées ) : 
```bash
hey -n 1000 -c 100 http://127.0.0.1:8000/api
```

## Commande pour effectuer le pylint

Pour lancer le pylint : 
```bash
pylint --load-plugins=pylint_django --django-settings-module=babord_project.settings api_rest_babord
```


## Explication supplémentaire sur le projet

### Description du projet

Le projet Bâbord est le regroupement de solutions pour le label babord : 
 - Un site web ( wordpress ) permettant au artistes labeliser babord de renseigner une description de leur groupe et de renseigner leur prochain evenement( concert, sortie d'album et festival )
 - une API permettant de récupérer les informations des artistes et des evenements
 - une application mobile permettant de consulter les informations des artistes et des evenements ( avce notamment un carte interactive pour les evenements )

### Description de l'API

un swagger est mit a disposition à cette adresse : http://localhost:8000/api/swagger/  ( lancer le serveur pour y accéder )
Cependant le but de l'API et de représenter les données des artistes et des evenements de la base de données.

### Utilisateur mobile
En cours de developpement pour le token JWT

Pour qu'un utilisateur mobile puisse accéder à l'API, il doit s'authentifier avec un token JWT. Pour cela, il doit envoyer une requête POST à l'adresse suivante : http://localhost:8000/api/mobile-login avec les informations suivantes :

```json
{
    "mail": "mail@mail.mail",
    "password": "password"
}
```

Et retourne une instance de l'utilisateur avec un token JWT ( voir le fichier auth_views.py pour plus d'informations )

## Améliorations possibles

Un certain nombre d'amélioration sont possible notamment : 
- les token JWT ( en cours de developpement )
- passage en MongoDB ( analyse pousser necessaire )
- ajout utilisateur web ( pour les artistes ) mais a voir avce babord car pas de besoin pour le moment
- modification du web pour une page par utilisateur ( pour les artistes )
- optimisation des requetes
- ajout d l'admin django pour la gestion des données ( pour l'instant ancun besoin )

## Contacter les développeurs

Pour contacter les développeurs, vous pouvez envoyer un mail à l'adresse suivante : 

aide.dev.api.babord@gmail.com


## Fonctionnalite en cours d'implémentation 

Comme expliquer dans la partie amélioration possible, certaines fonctionnalités sont en cours d'implémentation :
 - les JWT, je rencontre un probleme sur le fait qu'il est necessaire d'utiliser les user de django pour les jwt cependant je ne l'ai utilise pas du tout dans le projet, je cherche donc un moyen de contourner regler ce probleme 
