# Camploy

Un projet Django pour la plateforme Camploy.

## Installation

1. Clonez le repository :
```bash
git clone <url-du-repository>
cd camploy
```

2. Créez un environnement virtuel :
```bash
python -m venv venv
```

3. Activez l'environnement virtuel :
```bash
# Sur Windows
venv\Scripts\activate

# Sur macOS/Linux
source venv/bin/activate
```

4. Installez les dépendances :
```bash
pip install -r requirements.txt
```

5. Effectuez les migrations :
```bash
python manage.py migrate
```

6. Créez un superutilisateur :
```bash
python manage.py createsuperuser
```

7. Lancez le serveur de développement :
```bash
python manage.py runserver
```

Le site sera accessible à l'adresse : http://127.0.0.1:8000/

## Structure du projet

```
camploy/
├── camploy/          # Configuration du projet Django
│   ├── __init__.py
│   ├── settings.py   # Paramètres du projet
│   ├── urls.py       # URLs principales
│   ├── wsgi.py       # Configuration WSGI
│   └── asgi.py       # Configuration ASGI
├── manage.py         # Script de gestion Django
├── requirements.txt  # Dépendances Python
├── .gitignore       # Fichiers à ignorer par Git
└── README.md        # Ce fichier
```

## Développement

Pour ajouter de nouvelles applications Django :
```bash
python manage.py startapp nom_de_l_app
```

## Technologies utilisées

- Django 4.2+
- Python 3.8+
- PostgreSQL (en production)
- SQLite (en développement)
