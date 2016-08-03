# portfolio
My portfolio website


## TODO

- captcha google pour l'envoi du formulaire
- completer l'exécution du formulaire sécurisée
- resume
- remplir bdd education
- vérifier la compatibilité des différents navigateurs
- compléter mon profil google+, facebook, github
- compléter le readme

- BONUS: jolie page 404
- BONUS: multi langage
- BONUS: generation automatique des données depuis le pdf/latex du cv
- BONUS: code konami -> photos de vacances en mozaique avec un morceau de la mozaique qui permet de retourner sur le site

## Version

1.0

## Installation prerequisities

* Un système Unix

* Une base de données MySQL à laquelle se connecter

* La bibliothèque `libmysqlclient-dev`, obtenable classiquement avec `sudo apt-get install libmysqlclient-dev`

* Python avec le gestionnaire de modules python `pip` : `sudo apt-get install python-pip`

  Si besoin, une procédure d'installation plus détaillée de pip peut être trouvée ici : http://pip.readthedocs.org/en/stable/installing/

* Le gestionnaire d'environnement virtuel pour python `virtualenv`. Installé par défaut avec les dernières verions de python, mais disponible, s'il n'est pas déjà installé, via votre gestionnaire de paquet préféré, sous le nom `python-virtualenv`, ou via `pip`.

  `sudo apt-get install python-virtualenv`

  ou `sudo pip install virtualenv`

## Installation

Placez vous dans un nouveau dossier dédié au portfolio. Nous l'appellerons `project_portfolio` dans la suite.

Décompressez l'archive du projet dans un sous-dossier `portfolio` ou clonez le dépôt du projet (privé pour l'instant) : `git clone https://github.com/Mascarpone/portfolio.git`

Afin de ne pas installer les modules requis directement sur vôtre système, et de ne pas dépendre de la configuration actuelle de celui-ci, nous allons créer un environnement virtuel avec `virtualenv`. Pour cela, utilisez la commande suivante : `virtualenv venv`

Nous disposons donc maintenant d'un environnement situé dans le dossier `venv`. Pour le lancer, utilisez la commande : `. venv/bin/activate` (ne pas oublier le point seul au début)

Pour vous assurer de la bonne activation de l'environnement virtuel, vérifiez que l'invite de commande a bien été modifiée et commence maintenant par `(venv)`. Par exemple `(venv)utilisateur@machine:~/project_portfolio`

Nous pouvons maintenant installer toutes les dépendances dans l'environnement virtuel : `pip install -r portfolio/requirements.txt` (il est possible que les droits d'administrateur soient requis pour cela)

Puis lancer le serveur : `python portfolio/app.py` (Utilisez Ctrl+C pour le quitter)

Le site portfolio est maintenant disponible à l'adresse http://localhost:8000

Pour quitter l'environnement virtuel, Utilisez la commande `deactivate`


## Un peu de lecture

http://flask.pocoo.org/docs/0.10/quickstart/

http://jinja.pocoo.org/docs/dev/templates/

http://www.cheat-sheets.org/saved-copy/git-cheat-sheet.pdf