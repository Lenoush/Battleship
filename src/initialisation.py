from matrice import plot_grid, plot_flotte_grid, create_grid
from bateau import input_ajout_bateau, nouveau_bateau
from utils import random_orientation, random_position

NOMS = ["Transporteur" , "Cuirassé" , "Croisseur", "Sous-marin", "Destructeur" ]

#Fonction qui defini la flotte du joueur en fonction de ces choix. 
def init_joueur():
    flotteJoueur = []
    plot_grid(create_grid())
    for i in range (len(NOMS)) :
        input_ajout_bateau(flotteJoueur, NOMS[i])
        plot_flotte_grid(create_grid(),flotteJoueur)
        while len(flotteJoueur) != i+1 :
            input_ajout_bateau(flotteJoueur, NOMS[i])
            plot_flotte_grid(create_grid(),flotteJoueur)
    return(flotteJoueur)

#Fonction qui defini la flotte de L'IA en fonction de ces choix. 
import random
def init_ia() :
    flotteORDI = []
    for i in range (len(NOMS)) :
        nouveau_bateau(flotteORDI,NOMS[i],random_position(),random_orientation())
        while len(flotteORDI) != i+1 :
            nouveau_bateau(flotteORDI,NOMS[i],random_position(),random_orientation())
    return(flotteORDI)
