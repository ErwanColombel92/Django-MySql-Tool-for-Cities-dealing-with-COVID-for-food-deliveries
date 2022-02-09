# Django-MySql-Tool-for-Cities-dealing-with-COVID-for-food-deliveries
This project aims to create a web platform that cities could use to organize food deliveries in a COVID or a crisis context. Is uses MySql and Django (Python).

La gestion des demandeurs s’établit en plusieurs parties. On trouve la gestion des comptes utilisateurs, la gestions des profils des utilisateur et la gestion des commandes. Ces différents points seront abordés dans les trois parties qui suivront.

Pour la base de la gestion des comptes utilisateurs, nous nous sommes servis de la classe User par défaut de Django. Cette classe permet de gérer les utilisateurs de l’application en définissant s’ils peuvent être admin ou non grâce à un simple booléen. Par défaut, lorsqu’un utilisateur s’inscrit, il renseigne nom, prénom, username, mot de passe et adresse mail. Ces informations sont directement sauvegardées dans la BDD dans la table auth_user.

La gestions du compte utilisateur seule ne suffit pas, pour pouvoir ajouter d’autres données intéressantes, nous avons créé un modèle Profil,permettant d’associer (grâce à un héritage) les données suivantes au compte utilisateur :
• adresse
• ville
• département (nous n’avons géré que l’ile de France et les arrondissements de Paris)
• photo de profil optionnelle
• 1 Restriction alimentaire au choix parmi : Sans Gluten, Sans Viande, Sans Fruits secs, Sans Lactose ou Aucune restriction

![profil](https://user-images.githubusercontent.com/59508102/153101784-b9ed4d42-8137-4463-916b-938f11605ce9.jpg)

Afin d’éviter que plusieurs commandes se fassent à partir d’un même foyer, nous avons également ajouté une gestion des foyers. Chaque personne peut posséder un compte sur le site, mais seul le Chef de Famille (géré par un booléen dans la BDD) aura accès à l’interface de commande. Par défaut, lorsqu’un utilisateur s’inscrit et entre une adresse, un nouveau foyer est automatiquement créé dans la BDD ( table foyer) s’il est le premier membre de sa famille à s’inscrire. Il sera donc par défaut le seul chef de famille de celle-ci. Si un second membre s’inscrit, en rentrant son adresse, Django interroge la BDD et le place automatiquement dans le foyer correspondant (même adresse et même ville). Pour modifier le statut Chef de Famille, l’utilisateur doit contacter les gestionnaires du site (nous !).

![foyers](https://user-images.githubusercontent.com/59508102/153101780-e4374ff4-adfa-4648-b5f3-7141c139ce2d.jpg)

L’interface de commandes débute avec un choix de filtre afin de choisir quels articles nous souhaitons commander. Les articles affichés tiennent compte des restrictions alimentaires choisies dans la page de profil.


![panier](https://user-images.githubusercontent.com/59508102/153101781-0e5e77a5-91ea-4a90-b6b2-067c559ffee2.jpg)

Cette section d’interface collectivité n’est visible à l’écran que si l’on est connecté en mode super user (utilisateur du mode admin). Ceci permet d’éviter qu’un utilisateur lambda du site puisse arriver sur cette page. Le bouton d’accès à cette page n’est pas le seul à être masqué : même si un utilisateur tentait d’accéder à cette page sans être administrateur, il serait redirigé vers l’interface de connexion. Ceci a été rendu possible grâce à l’utilisation d’un lambda expression prenant en entrée un utilisateur connecté et vérifiant s’il est super utilisateur.

![maps](https://user-images.githubusercontent.com/59508102/153101783-d37a3a63-93f0-4012-a71b-e20af8cb5a1c.jpg)

