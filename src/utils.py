
import time 

N = 10
NOMS = ["Transporteur" , "Cuirassé" , "Croisseur", "Sous-marin", "Destructeur" ]

# Transformation d'une position "chiffre/chiffre" en position "lettre/chiffre"
def string_from_pos(S) :
    return(chr(S[0]+97),int(S[1]))

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

#Fonction qui renvoie l'indice de la taille. 
def id_taille_Nom(nom) :
    for i in range (len(NOMS)) :
        if NOMS[i] == nom :
            return i

#Fonction qui attend 5 second avant de passer a la suite du code
def PetitHide():
    print("\x1b[1;30mVous avez 5 secondes pour examiner le jeu.")
    time.sleep(5)
    for i in range(5) :
        print (" ")

#Fonction qui attend 5 puis 7 seconde pour passer au prochain adversaire 
def hide():
    print("\x1b[1;30mVous avez 7 secondes pour examiner votre jeu.")
    time.sleep(7)
    for i in range(100) :
        print (" ")
    print("Veuillez donner l'ordinateur à votre adversaire, vous avez 5 secondes.")
    time.sleep(5)
    for i in range(100) :
        print (" ")

#Fonction qui test si un jour a gagne la partie ( fonction qui se verifie a CHAQUE tour)
def check_fin_partie(Nom, M, flotte, nb_tour):
    if (len(flotte))==0:
        print ("\x1b[4;31m",Nom," à gagné en ",nb_tour," tours")
        exit()
        return True
    else : return False
