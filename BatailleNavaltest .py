# Lena OUDJMAN et Salma BASRIR

from src.matrice import create_grid, plot_grid

N = 10
LIGNES = list(map(chr,range(97,107)))
COLONNES = [" "] + [str(i) for i in range (N)]
VIDE = "."
EAU = "O"
TOUCHE = "X"
BATEAU = "#"
DETRUIT = "@"
NOMS = ["Transporteur" , "Cuirassé" , "Croisseur", "Sous-marin", "Destructeur" ]
TAILLES = [5,4,3,3,2]

DICT_LIGNES_INT = {LIGNES[i]:i for i in range(len(LIGNES))}




# Creation de position aleatoire Pour L'IA
from random import randint
def random_position() :
    return (randint(0,N-1), randint(0,N-1))

# Fonction en plus : Choisi aleatoirement une orientation Pour l'IA
from random import choice
def random_orientation() :
    orientation = ["v","h"] 
    return choice(orientation)

# Transformation d'une position "lettre/chiffre" en position "chiffre/chiffre"
import re
def pos_from_string(S) :
    if bool(re.match("^[a-j]$",S[0])) :
        if bool(re.match("^[0-9]$",S[1])) :
            return (ord(S[0])-97,int(S[1])) #On utlise ici le code ASCII des lettres Minuscules (ex: ASCII de 'a' = 97 donc 'a2' renvoie '02' )





#Creation d'une fonction qui ajoute un nouveau bateau à la flotte (liste des bateaux des joueurs)
def nouveau_bateau(flotte,nom,pos,orientation):
    d={}
    d['nom']=str(nom)
    indiceTaille = id_taille_Nom(nom)
    d['taille'] = TAILLES[indiceTaille] #La taille du bateau est prédefini par son nom. 
    d['cases touchées']=0
    d['pos']=[pos]
    for i in range(1,d['taille']):
        if orientation== "h" or orientation== "H":
            if (pos[1] + i) < 0 or (pos[1] + i) >9 :
                return ("Le bateau ne peut etre ici car hors grille, Merci de mettre un autre position")
            else :
                d['pos'].append((pos[0],pos[1]+i))
        elif orientation== "v" or orientation== "V" :
            if (pos[0]+ i) <0 or (pos[0]+ i) >9 :
                return("Le bateau ne peut etre ici car hors grille,  Merci de mettre un autre position")
            else :
                d['pos'].append((pos[0]+i,pos[1]))
    d['orientation']=orientation
    if presence_bateau_totale(pos,orientation,flotte,nom) == False : #On verifie que le bateau qu'on souhaite ajouter ne croise pas un autre bateau. 
        flotte.append(d)
    else : return ""


                
#Fonction en plus pour etre sur le bateau qu'on souhaite ajouter ne croise pas un autre bateau deja present dans la flotte.
def presence_bateau_totale(pos,orientation,flotte,nom):
    indiceTaille = id_taille_Nom(nom)
    if orientation == 'h' or orientation== "H":
        j=0
        while (j < TAILLES[indiceTaille]) and (presence_bateau(((pos[0],pos[1] + j)), flotte) == False) :#Tant que la case est libre
            j = j + 1
        if j == TAILLES[indiceTaille] : return False #Tous les cases sont libres
        else : return True #La case n'est pas libre
    elif orientation =='v' or orientation== "V":
        j=0
        while (j < TAILLES[indiceTaille]) and (presence_bateau(((pos[0] + j, pos[1])), flotte)) == False:
            j = j + 1
        if j == TAILLES[indiceTaille] : return False #Tous les cases sont libres
        else : return True #La case n'est pas libre

#Transforme une Matrice lambda en grille a Jouer Decouverte en fonction de la flotte du joueur
def plot_flotte_grid(M,flotte):
    for i in range (len(flotte)):
        for pos in (flotte[i]["pos"]) :
            M[pos[0]][pos[1]] = BATEAU
    return (plot_grid(M))

#Fonction qui permet de rajouter un bateau dans la liste flotte du joueur en fonction d'une posistion et d'une oriantation donnée. 
from re import *
def input_ajout_bateau(flotte,nom):
    indiceTaille = id_taille_Nom(nom)
    pos = input("Donnez une position, de forme 'a0', pour ajouter le bateau %s , de taille %d: " %(nom,TAILLES[indiceTaille]))
    while search(r"\b[a-j]{1}[0-9]{1}\b",pos) == None:
        pos = input("Donnez autre une position, de forme 'a0', pour ajouter le bateau %s , de taille %d, celle d'avant n'est pas conforme : " %(nom,TAILLES[indiceTaille]))
    posFinale = pos_from_string(pos)
    while presence_bateau(posFinale,flotte) == True:
        pos = input("Donnez une autre position, de forme 'a0', pour le bateau %s de taille %d ,celle-ci est deja prise : " %(nom,TAILLES[indiceTaille]))
        while search(r"\b[a-j]{1}[0-9]{1}\b",pos) == None:
            pos = input("Donnez autre une position, de forme 'a0', pour ajouter le bateau %s , de taille %d, celle d'avant n'ets pas conforme : " %(nom,TAILLES[indiceTaille]))
        posFinale = pos_from_string(pos)
    print ("Vous Voulez ajouter un bateau en cases " ,pos,)
    orientation = input("Donnez une orientation entre h et v : ")
    while search(r"\b[hvHV]\b", orientation) == None :
        orientation = input("Votre orientation est fausse, Merci de mettre h ou v : ")
    print("Vous voulez ajouter le bateau %s , de taille %d ,en position %s et en orientation %s. " %(nom,TAILLES[indiceTaille],pos,orientation))
    if presence_bateau_totale(posFinale,orientation,flotte,nom) == False :
        return nouveau_bateau(flotte,nom,posFinale,orientation)
    else : print ("Votre bateau %s de taille %s , d'orientation %s et de position principale %s ne peux etre mis car il croise un autre bateau de vous. Merci de recommencer" %(nom,TAILLES[indiceTaille],orientation,pos))


            
#Fonction en plus qui renvoie l'indice de la taille. 
def id_taille_Nom(nom) :
    for i in range (len(NOMS)) :
        if NOMS[i] == nom :
            return i
            
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

#Fonction qui test si un jour a gagne la partie ( fonction qui se verifie a CHAQUE tour)
def test_fin_partie(Nom, M, flotte, nb_tour):
    if (len(flotte))==0:
        print ("\x1b[4;31m",Nom," à gagné en ",nb_tour," tours")
        exit()
        return True
    else : return False

#Fonction qui fait jouer un jouer x contre l'IA, chacun tire une fois l'un apres l'autre
def joueur_vs_ia():
    NomJoueur = input("Donner Votre Nom : ")
    nb_tour = 1
    print("\x1b[0;31m",NomJoueur, "commence à initialiser sa flotte.")
    FlotteJoueur = init_joueur()
    FlotteIA = init_ia()
    for i in range(5) : print (" ")
    print("\x1b[1;30mLe jeu peux commencer. L'IA a creer sa flotte. \x1b[0;31m",NomJoueur," commencez à attaquer :")
    plot_grid(create_grid())
    M = tour_joueur(create_grid(),FlotteIA)
    PetitHide()
    print("\x1b[0mAu tour de l'IA d'attaquer.")
    J = tour_ia_random(create_grid(),FlotteJoueur)
    PetitHide()
    while (test_fin_partie('Ordi', J, FlotteJoueur, nb_tour) == False) :
        nb_tour = nb_tour +1
        print("\x1b[0;31mVotre flotte ",NomJoueur, " : ")
        plot_flotte_grid(create_grid(),FlotteJoueur)
        print ("Nb de bateaux encore debout : %d" %(len(FlotteJoueur)))
        print ("Nb de bateaux coulés : %d" %(5-len(FlotteJoueur)))
        for i in range(5) : print (" ")
        print (NomJoueur, " Merci de jouer. Il vous reste %d bateaux à detruire" %(len(FlotteIA)))
        plot_grid(M)
        M = tour_joueur(M,FlotteIA)
        PetitHide()
        if (test_fin_partie(NomJoueur, M, FlotteIA, nb_tour) == False) :
            print("\x1b[0mAu tour de l'IA d'attaquer.")
            J = tour_ia_better_random(J,FlotteJoueur) 
            PetitHide()

def PetitHide():
    print("\x1b[1;30mVous avez 5 secondes pour examiner le jeu.")
    time.sleep(5)
    for i in range(5) :
        print (" ")

def hide():
    print("\x1b[1;30mVous avez 7 secondes pour examiner votre jeu.")
    time.sleep(7)
    for i in range(100) :
        print (" ")
    print("Veuillez donner l'ordinateur à votre adversaire, vous avez 5 secondes.")
    time.sleep(5)
    for i in range(100) :
        print (" ")
        
import time 
def deux_joueurs() :
    NomJoueur1 = input("Donner Le Nom Du Premier Joueur : ")
    NomJoueur2 = input("Donner Le Nom Du Deuxième Joueur : ")
    nb_tour = 1
    for i in range(5) : print (" ")
    print("\x1b[0;31m",NomJoueur1, "commence à initialiser sa flotte. Sachez que pendant la partie, lors de Votre tour, le jeu jeu sera de couleur rouge.")
    FlotteJoueur1 = init_joueur()
    hide()
    print("\x1b[0;34mC'est maintenant à", NomJoueur2, " d'initialiser sa flotte. Sachez que pendant la partie, lors de Votre tour, le jeu jeu sera de couleur bleu.")
    FlotteJoueur2 = init_joueur()
    hide()
    print("\x1b[0;31mVotre flotte ",NomJoueur1," : ")
    plot_flotte_grid(create_grid(),FlotteJoueur1)
    for i in range(5) : print (" ")
    print (NomJoueur1, "peut commencer à jouer.")
    plot_grid(create_grid())
    MatriceJ2 = tour_joueur(create_grid(),FlotteJoueur2)
    hide()
    print("\x1b[0;34mVotre flotte ", NomJoueur2," : ")
    plot_flotte_grid(create_grid(),FlotteJoueur2)
    for i in range(5) : print (" ")
    print("C'est maintenant à", NomJoueur2, " de jouer.")
    plot_grid(create_grid())
    MatriceJ1 = tour_joueur(create_grid(),FlotteJoueur1)
    hide()
    while (test_fin_partie(NomJoueur2, MatriceJ1, FlotteJoueur1, nb_tour) == False) :
        nb_tour = nb_tour +1
        print("\x1b[0;31mVotre flotte ",NomJoueur1, " : ")
        plot_flotte_grid(create_grid(),FlotteJoueur1)
        print ("Nb de bateaux encore debout : %d" %(len(FlotteJoueur1)))
        print ("Nb de bateaux coulés : %d" %(5-len(FlotteJoueur1)))
        for i in range(5) : print (" ")
        print (NomJoueur1, " Merci de jouer. Il vous reste %d bateaux à detruire." %(len(FlotteJoueur2)))
        plot_grid(MatriceJ2)
        MatriceJ2 = tour_joueur(MatriceJ2,FlotteJoueur2)
        if (test_fin_partie(NomJoueur1, MatriceJ2, FlotteJoueur2, nb_tour) == False) :
            hide()
            print("\x1b[0;34mVotre flotte ",NomJoueur2," : ")
            plot_flotte_grid(create_grid(),FlotteJoueur2)
            print ("Nb de bateaux encore debout : %d" %(len(FlotteJoueur2)))
            print ("Nb de bateaux coulés : %d" %(5-len(FlotteJoueur2)))
            for i in range(5) : print (" ")
            print (NomJoueur2, "Merci de jouer. Il vous reste %d bateaux à detruire." %(len(FlotteJoueur1)))
            plot_grid(MatriceJ1)  
            MatriceJ1 = tour_joueur(MatriceJ1,FlotteJoueur1)
            hide()
            
