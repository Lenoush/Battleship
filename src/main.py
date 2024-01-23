from jeux import joueur_vs_ia, deux_joueurs

def Choix() :
    NbDeJoueur = input("Voulez-Vous jouer contre l'ordi (mettre '1') ou contre un autre joueur (mettre '2') ? ")
    while (NbDeJoueur != '1') and (NbDeJoueur != '2') :
        NbDeJoueur = input("Voulez-Vous jouer contre l'ordi ou contre un autre joueur ? Merci de repondre par ordi ou joueur : ")
    if (NbDeJoueur == '1') :
        print("Vous avez choisie de joueur contre une IA.")
        return joueur_vs_ia()
    elif (NbDeJoueur == '2') :
        print("Vous avez choisie de joueur contre un autre joueur.")
        return deux_joueurs()
    
Choix()
