# Projets Babord

## Installation

Pour installer le projet, il faut cloner le projet et installer les dépendances.

```bash
git clone
cd babord_project
pip install -r requirements.txt
```

## Lancement du serveur

Pour lancer le serveur, il faut exécuter la commande suivante :

```bash
./manage.py runserver
```

## Création de la base de données

Pour créer la base de données, il faut exécuter la commande suivante :

```bash
./manage.py migrate
```


## commande test

Pour lancer les test unitaire  : 
```bash
./manage.py test api_rest_babord.tests.unitaire
```

Pour lancer les test d'intégration  : 
```bash
./manage.py test api_rest_babord.tests.integration
```

## commande pylint

Pour lancer le pylint : 
```bash
pylint --load-plugins=pylint_django --django-settings-module=babord_project.settings api_rest_babord
```
Pour 
