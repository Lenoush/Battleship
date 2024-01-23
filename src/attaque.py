from matrice import plot_grid
from utils import string_from_pos,random_position, pos_from_string
from bateau import id_bateau_at_pos, presence_bateau
from re import search

EAU = "O"
TOUCHE = "X"
VIDE = "."
DETRUIT = "@"


#Fonction qui trouve une position vide et l'attaque 
def tour_ia_random(M,flotte):
    pos = random_position()
    while M[pos[0]][pos[1]] != VIDE :
        pos = random_position()
    return tir(M,pos,flotte,'IA')

#Fonction qui demande une position vide et l'attaque 
def tour_joueur(M,flotte) :
    pos = input("Donnez une position pour tirer: " )
    while search(r"\b[a-j]{1}[0-9]{1}\b",pos) == None:
        pos = input("Donnez une autre position pour tirer, de forme 'a0', celle d'avant n'ets pas conforme : " )
    pos = pos_from_string(pos)
    while M[pos[0]][pos[1]] != VIDE :
        pos = input("Donnez une autre position,celle-ci à deja etait attaqué : ")
        while search(r"\b[a-j]{1}[0-9]{1}\b",pos) == None:
            pos = input("Donnez une autre position pour tirer, de forme 'a0', celle d'avant n'ets pas conforme : ")
        pos = pos_from_string(pos)
    return tir(M,pos,flotte,'Joueur')

#Fonction qui attaque les cases entourant les cases touchees de la flotte si il y'en a. 
def tour_ia_better_random(M, flotte):
    for i in range(len(flotte)):
        if flotte[i]["cases touchées"]!= 0:
            for e in flotte[i]["pos"] :
                if M[e[0]][e[1]] != TOUCHE:
                    return tir(M,e,flotte,'IA')
    return tour_ia_random(M,flotte)

# Fonction permettant de tirer a la postion pos dans la matrice M, elle retourne la matrice.
def tir (M,pos,flotte,nom) :
    indice = id_bateau_at_pos(pos,flotte)
    pos2 = string_from_pos(pos)
    
    if M[pos[0]][pos[1]] != "." :
        print ("FALSE : Cette case ",pos2," a deja ete attaqué" )
    else :
        print ("TRUE : Cette case" ,pos2, "n'a pas encore ete attaqué" )
        if presence_bateau(pos,flotte) == False : #Si la case est libre, le tir est manqué.
            M[pos[0]][pos[1]] = EAU
            print ("MANQUE, Dommage")
            plot_grid(M)
        elif presence_bateau(pos,flotte) == True : #Si la case n'est pas libre, le tir est Reussi.
            M[pos[0]][pos[1]] = TOUCHE
            print ("TOUCHE, Bravo")
            flotte[indice]["cases touchées"] = flotte[indice]["cases touchées"] + 1 
            if (flotte[indice]["taille"]) == (flotte[indice]["cases touchées"]) : #Si True , Tous le bateau a été detruit
                print ("TOUCHÉ-COULÉ : FELICITATION VOUS AVEZ COULÉ LE BATEAU" ,flotte[indice]["nom"])
                for i in flotte[indice]["pos"] :
                    M[i[0]][i[1]] = DETRUIT #Toutes les positions du bateau en Question passe de TOUCHE à DETRUIT
                plot_grid(M)
                flotte.pop(indice) #On enleve le bateau detriut de la liste des bateaux OK
            else : #Si le tir est Reussi mais que le bateau n'est pas detruit alors l'IA ou le Joueur qui a tiré peux rejouer
                if nom == 'IA' : tour_ia_better_random(M, flotte)
                elif nom == 'Joueur' :
                    plot_grid(M)
                    tour_joueur(M,flotte)
    return M 