# Middleware
Ce projet implémente un middleware qui permet d'assurer une communication sécurisée et tracée entre les différentes applications clientes et la base de données métier.

Le middleware est composé de différents composants logiciels à savoir :

1. Une Blockchain (fait maison) qui permet de tracer toutes les transactions effectuées.
2. HL7 Parser : utilisé par la blockchain pour traduire les messages hl7 en objet.
3. Les microservices (ou `api`) qui represente les services métiers.

##installer le Git:
https://git-scm.com/download/win

##installer visual studio code:
https://code.visualstudio.com/docs?dv=win

## Pré-requis
1. Installer [Python 3.6+](https://www.python.org/downloads/).
2. Installer [pipenv](https://github.com/kennethreitz/pipenv). 
```
$ pip install pipenv 
```
3. Installer les requirements  
```
$ pipenv install 
``` 
    
## Blockchain
Ajouter plus de contenu (se baser sur le projet de base)
py -m main.application

## Parseur HL7
Le seul parseur compatible avec python 3
https://python-hl7.readthedocs.io/en/latest/

##Base de données mysql
installer  https://dev.mysql.com/downloads/file/?id=480823
installer flask : 
pip install Flask
pip install requests
pip install hl7


## Microservices/API

### 1. Resource Patient
```
GET /patients
```
Retourne tous les patients
```
GET /patients/pid
```
Recherche le patient avec son PID (patient identifier)

Création d'un nouveau patient

### 2. Resource Observation
```
POST /observations
```
**Exemple:**
```
POST /observations
```

Retourne tous les patients


# Démarrer les applications

## Démarrer l'API
```
py -m main.application
```

toto 

liens importants: 

https://github.com/schoolofcode-me/rest-api-sections

