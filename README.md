# Battleship Game

Bienvenue sur le projet Battleship, une reproduction du célèbre jeu de stratégie où vous pouvez affronter un ami ou jouer contre l'ordinateur. Le but est simple : placez stratégiquement vos navires sur une grille et tentez de couler la flotte de votre adversaire avant qu'il ne coule la vôtre !

Ce projet a été développé dans le cadre de mes études à l'Université Panthéon Sorbonne. Il est entièrement écrit en Python et vous permet de jouer à Battleship dans un environnement convivial.

# Caractéristiques
Jouez contre un autre joueur ou contre l'ordinateur.
Deux niveaux de difficulté disponibles (un troisième est en cours de développement).  

# Installation

Clonez le dépôt :
```
git clone https://github.com/Lenoush/Battleship.git && cd Battleship
```

Installez les dépendances :
```
pip install -r requirements.txt
```

Exécutez le jeu :
```
python src/main.py
```

# Fonctionnalités
- Création de la grille : create_grid() génère une matrice vide pour le jeu.
- Tirs : Les joueurs peuvent tirer sur les cases de l'adversaire avec tir(M, pos, flotte).
- Positions aléatoires : random_position() et random_orientation() aident à positionner les navires de manière aléatoire.
- Gestion des navires : Fonctionnalités pour ajouter et vérifier la présence de navires dans la flotte.

# Améliorations possibles
- Gérer le second tour de l'ordinateur après un 'touché' pour qu'il touche au hasard une case adjacente plutôt que de détruire le bateau.
  
Introduire différents niveaux de difficulté pour l'IA :  
Facile : L'ordinateur tire au hasard après avoir touché une case.  
Moyen : L'ordinateur tire au hasard uniquement sur les cases adjacentes à la case touchée.  
Difficile : Comportement actuel.    

# Fonctions principales
Voici une brève explication des principales fonctions du jeu :

create_grid() : Crée une matrice vide.  
plot_grid(M) : Affiche la grille.  
tir(M, pos, flotte) : Met à jour la matrice après un tir.  
random_position() : Renvoie une position aléatoire (Chiffre/Chiffre).  
random_orientation() : Renvoie une orientation (h/v).  
nouveau_bateau(flotte, nom, pos, orientation) : Ajoute un nouveau bateau à la flotte.  
presence_bateau(pos, flotte) : Vérifie la présence d'un bateau à une position donnée.  
init_joueur() : Initialise la flotte du joueur.  
init_ia() : Initialise la flotte de l'IA.  

# Auteurs
Ce projet a été développé par Lena OUDJMAN. Merci d'avoir consulté ce dépôt, et amusez-vous bien à jouer à Battleship !
