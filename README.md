# NomadSocial-backend

installation du projet:

installer python (j'ai la version 3.10, je ne sais pas si ca marchera avec toutes les version, à voir)

Creez un dossier dans lequel vous mettrez le projet et installez-y l'environnement virtuel via la commande : python3.10 -m venv env (si vous avez la version 3.10 de python sinon utilisez votre version)

Activez ensuite l'environnement virtuelle avec la commande: source env\bin\activate

Pour installer toutes le bibliothéques essentiels executez la commande : pip install -r requirements.txt

Ensuite executez les commandes :

python manage.py makemigrations

python manage.py migrate

Ces commandes sont à executer à chaque fois qu'il y a des modifications dans le projet qui pourraient affecter la base de données

Enfin pour lancer le serveur, executer la commande:

python manage.py runserver



UTILISATION DU PROJET AVEC SQLITE3 :

Activer la machine virtuelle avec la commande: source env\bin\activate (il faut se placer dans le dossier ou se trouve le dossier env)
Il devrait y avoir écrit "(env)" dans le terminal devant le chemin courant si la machine virtuelle a été lancée

Ensuite executez les commandes :

python manage.py makemigrations

python manage.py migrate

Ces commandes sont à executer à chaque fois qu'il y a des modifications dans le projet qui pourraient affecter la base de données

Enfin pour lancer le serveur, executer la commande:

python manage.py runserver
