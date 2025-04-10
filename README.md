## Anthony Montoya
# Musics

Ce projet est un exemple d’application Python permettant de voir diverses
informations sur des données liées à la musique.

La base de données viennent du dépôt
https://github.com/lerocha/chinook-database

Il comprend 4 manières d’accéder aux données :

- une interface web dans `musics/api.py`.
- une interface en ligne de commande dans `musics/__main__.py`,
- une bibliothèque pour afficher des résultats dans le terminal dans `musics/cli.py`,
- une bibliothèque bas-niveau pour accéder à la base de données dans `musics/db.py`,

Cette application est écrite à des fins éducatives, et ne suit pas toutes les
bonnes pratiques du développement d’applications en Python.

**Au-delà de Python, le but de cette évaluation est de vous familiariser avec
les multiples facettes du développement : lecture et compréhension de
code, découverte d’outils, lecture de documentation, qualité
logicielle, intégration continue…**

Le sujet d’évaluation, comprenant des opérations à réaliser et des questions,
est inclus en bas de ce document.

Si vous avez des réponses à donner ou des remarques à faire, une section est
dédiée à cela en bas de ce document : écrivez ce que vous souhaitez, commitez
et pushez ce document README.md. N’écrivez pas de texte ailleurs que dans cette
section !

**Ce devoir est à rendre pour le 10 avril à 12h15. L’évaluation est individuelle.**

Les rendus après cette date ne seront pas évalués. Pour des raisons d’équité,
aucune excuse concernant un oubli de commit ou de push ne sera tolérée.

Les devoirs dont le contenu est trop proche, dont l’historique Git est douteux,
ou dont le code est si stupide qu’il ne peut pas avoir été écrit par un humain,
seront notés comme tous les autres et leur note sera divisée par 2.


## Comment l’installer

1. [Importez](https://github.com/new/import) le dépôt en privé.

2. Partagez votre dépôt en lecture avec moi.

   Sur la page de votre fork GitHub, dans l’onglet « Settings », la section
   « Collaborators and teams », vous avez un bouton « Add people ». Ajoutez
   l’utilisateur « grewn0uille » (Lucie Anglade).

3. Clonez votre fork.

   `git clone git@github.com:YourNickName/musics.git`

4. Allez dans votre dépôt cloné.

   `cd musics`

5. Créez un environnement virtuel appelé `venv`.

   `python -m venv venv`

6. Activez votre environnement virtuel.

7. Installez les dépendances du projet.

   `pip install -e .`


## Comment l’utiliser

Pour utiliser l’application ou lancer les tests, veillez bien à être à la
racine du dépôt que vous avez cloné et à activer l’environnement virtuel.

### Pour utiliser l’API web

`fastapi dev musics`

Vous avez alors accès à l’adresse `http://127.0.0.1:8000` et aux différentes
routes de l’application.

Une documentation automatique, avec une interface de test, est disponible à
l’adresse `http://127.0.0.1:8000/docs`.

Vous pouvez arrêter le serveur avec `Ctrl+C`.

### Pour utiliser la CLI

`python -m musics --help`

Différentes commandes s’offrent à vous. Pour afficher le top 5 des artistes,
vous pouvez par exemple lancer :

`python -m musics artists --top=5`

### Pour utiliser la bibliothèque

`python`

Dans l’interpréteur Python :

```python
>>> from musics import cli
>>> help(cli)
```

Différentes fonctions sont disponibles. Pour afficher le top 5 des artistes,
vous pouvez par exemple lancer :

```python
>>> cli.top_artists(top=5)
```

Pour quitter l’interpréteur, utilisez `exit()`.

### Pour utiliser les fonctions bas-niveau de la base de données

`python`

Dans l’interpréteur Python :

```python
>>> from musics import db
>>> help(db)
```

Différentes fonctions sont possibles. Pour récupérer une liste de tous les
artistes et afficher les informations du premier, vous pouvez par exemple
lancer :

```python
>>> artists = db.get_artists()
>>> dict(artists[0])
{'ArtistId': 1, 'Name': 'AC/DC'}
```

Vous pouvez également lancer des requêtes SQL de cette manière :

```python
>>> cursor = db.get_connection().cursor()
>>> artists = cursor.execute('SELECT ArtistId, Name FROM Artists LIMIT 5').fetchall()
>>> dict(artists[0])
{'ArtistId': 1, 'Name': 'AC/DC'}
```

Le schéma de la base de données est dans `database/model.sql`.

Pour quitter l’interpréteur, utilisez `exit()`.

### Pour lancer les tests

Quelques tests basiques sont disponibles dans le dossier `tests`.

Pour lancer les tests, lancez `python -m pytest`


## Sujet

Le but de cette évaluation est de tester, corriger et améliorer cette
application.

**Vérifiez d’avoir bien tout commité et pushé à la fin de votre travail, en
vérifiant les fichiers sur GitHub.**

**Faites au moins un commit par question, dans la mesure du possible.**

**Si vous n’arrivez pas à faire une question, ne perdez pas trop de temps,
passez à la suivante.**

Privilégiez l’intelligence à la quantité. Je préfère par exemple avoir
quelques tests pertinents que des centaines de tests répétitifs.
Utilisez ce que vous avez vu en cours, et la documentation des outils
vus en cours.

Ne me faites pas installer d’autres outils que les dépendances actuelles du
projet ou les bibliothèques que je vous demande d’installer pour cette
évaluation.

**Ajoutez votre nom et prénom tout en haut de ce README.**

### Testez l’application

Votre première mission est de tester l’application. Vous devrez au final avoir
100% de couverture pour `musics/db.py`.

Lors de l’écriture de vos tests, vous devrez trouver un bug (au moins)
caché dans ce fichier. Pour ce bug, faites un commit comprenant à la
fois la correction du bug et un test de non-régression.

Les fonctions des modules Python sont faites pour être utilisées avec les bons
types de paramètres, et ne gèrent volontairement pas les appels avec des types
différents : ce ne sont donc pas des bugs. Par contre, les API web et en ligne
de commande doivent rejeter proprement les types inattendus : si l’application
lève une exception, on peut considérer cela comme un bug.

1. Installez la bibliothèque `pytest-cov`. Ajoutez cette bibliothèque
   aux dépendances `pyproject.toml`. Cette dépendance ne doit être
   installée que si l’on veut lancer les tests.

2. Configurez pytest pour avoir la couverture uniquement sur les dossiers
   `musics` et `tests`. Enregistrez cette configuration dans
   `pyproject.toml`.

3. Configurez pytest pour afficher le détail des lignes qui ne sont pas
   couvertes dans le terminal. Enregistrez cette configuration dans
   `pyproject.toml`.

4. Écrivez des tests pour `db.py`, dans le fichier `test_db.py`. Inspirez-vous
   du test déjà écrit.

5. Un bug est caché dans le fichier, faites un test de non-régression dédié et
   commitez-le avec la correction.
   
### Trouvez et corrigez d’autres bugs

Dans cette application, il n’y avait pas qu’un seul bug.

Votre deuxième mission est de trouver les autres bugs. Il y a un bug
(au moins) caché dans chacun des fichiers du dossier musics (à part
__init__.py). Pour chacun de ces bugs, faites un commit comprenant à
la fois la correction du bug et un test de non-régression.

6. Dans le fichier `cli.py`, à quoi sert le paramètre « file » ?

7. Dans le fichier `__main__.py`, à quoi sert le commentaire « pragma:
   no cover » ?

8. Admettons que vous ayez une couverture de 100% sur l’ensemble de
   l’application. Serait-ce suffisant pour que l’ensemble du code
   fonctionne parfaitement ? Quels autres types de tests pourraient
   être idéalement réalisés ? (Ne les écrivez pas, décrivez-les
   simplement.)

9. Pour tester l’ensemble de l’application, dans quel ordre
    réaliseriez-vous les tests et pourquoi ? À quoi cela sert-il de
    regrouper une correction de bug et un test de non-régression dans
    un commit commun, ne comprenant que cela ?

### Ajoutez une fonctionnalité en TDD

Ajoutez une fonctionnalité de votre en suivant la méthode TDD (Test Driven Development). Vous
pouvez créer un système de recherche d’artistes par leur nom : rechercher « of »
trouvera par exemple « System Of A Down » et « The Office ».

À chaque fois, écrivez un test qui ne passe pas, commitez-le, puis ajoutez le
code nécessaire pour faire passer ce test dans un autre commit.

Écrivez d’abord la fonction nécessaire dans `db.py`. Répétez les opérations
dans `api.py`, `cli.py` et `__main__.py`.

Veillez bien sûr à garder une couverture de tests de 100% sur `db.py` !

### Configurez GitHub Actions sur votre dépôt

Activez GitHub Actions sur votre dépôt et configurez-le pour lancer les tests
sur plusieurs versions de Python, sur plusieurs plateformes, avec des choix
pertinents et justifiés. N’utilisez pas d’outils tiers, en particulier `tox`.

### Vérifiez la qualité du code

Mettez en place un outil de vérification de la qualité du code : installez,
configurez et utilisez `ruff`. Mettez en place dans votre dépôt Git des
méthodes pour s’assurer que le code suit toujours ces bonnes pratiques.

## Réponses et remarques

Si vous avez des réponses à écrire, des remarques à faire sur votre travail,
ajoutez-les à la fin de ce fichier. **N’hésitez pas à expliquer vos réussites,
vos doutes, vos erreurs, afin que je puisse mieux comprendre votre projet et en
tenir compte lors de mon évaluation.**
