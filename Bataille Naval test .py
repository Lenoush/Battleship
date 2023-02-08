# Lena OUDJMAN et Salma BASRIR
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
#AMELIORATION POSSIBLE :
    ##Faire en sorte que le soncond tour offert à l'ordi apres un 'touché' ne declenche pas la detruction du bateau
    #mais juste qu'il touche au hasard une case qui touche celle 'touché'
    ##Faire des Niveaux de l'ordi : - Facile : Ordi touche que au hasard aprés avoir touché une case
                                    #- Moyen : Ordi touche au hasard seulement les cases 'prés' de celle touché
                                    #- Difficile : Comme maintenant 


# create_grid() = Matrice vide
# plot_grid(M) = ""
# tir(M,pos,flotte) = Matrice
# random_position() = position (Chiffre/Chiffre)
# random_orientation() = orientation (h/v)
# pos_from_string(S) = position (Chiffre/Chiffre)
# nouveau_bateau(flotte,nom,pos,orientation) = ""
# presence_bateau(pos,flotte) = Boolean
# plot_flotte_grid(M,flotte) = Plot_grid(M) en fonction de flotte
# input_ajout_bateau(flotte,nom) = nouveau_bateau(flotte,nom,posFinale,orientation)
# id_bateau_at_pos (pos,flotte) = i indice du bateau de la position pos dans flotte
# init_joueur() = flotte du joueur 
# init_ia() = flotte de l'ordi
# tour_ia_random(M,flotte) = tir(M,pos,flotte)
# tour_joueur (nom,M,flotte) = tir(M,pos,flotte)
# tour_ia_better_random(M, flotte) = tour_ia_random(M,flotte)
# test_fin_partie(Nom, M, flotte, nb_tour) = (Nom," a gagné en  ",nb_tour," tours")

# Creation Matrice Vide ( avec seulemnt des points )
def create_grid() :
    matrice = []
    for i in range(N) :
        l =  []
        for j in range(N) :
            l.append(VIDE)
        matrice.append(l)
    return(matrice)

# Transforme une Matrice lambda en grille a Jouer 
def plot_grid(M) :
    PetiteListe = []
    L = [COLONNES] #Les chiffres de la Grille     #L est une liste de liste
    VarIncrementé = 1
    for i in LIGNES : #i prend la valeur des lettres entre a et j
        PetiteListe = [i] + M[LIGNES.index(i)] 
        L.append(PetiteListe)
    for i in L :
        for j in i :
            if VarIncrementé % 11 == 0 :
                VarIncrementé = VarIncrementé +1
                print ( j , end=" \n")
            else :
                VarIncrementé = VarIncrementé +1
                print ( j , end =" ")
    return ""

# Fonction permettant de tirer a la postion pos dans la matrice M, elle retourne la matrice.
def tir (M,pos,flotte,nom) :
    indice = id_bateau_at_pos(pos,flotte)
    pos2 = string_from_pos(pos)
    
    if M[pos[0]][pos[1]] != VIDE :
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



# Transformation d'une position "chiffre/chiffre" en position "lettre/chiffre"
def string_from_pos(S) :
    return(chr(S[0]+97),int(S[1]))



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

#Verifie si la position pos est deja dans la flotte.
def presence_bateau(pos,flotte):
    for i in range (len(flotte)):
        for j in (flotte[i]["pos"]) :
            if pos == j :
                return True #Il y a deja un bateau sur cette case
    return False #La case est libre
                
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

#Fonction qui indique l'indice du bateau,dont la position fait partie, dans la liste flotte 
def id_bateau_at_pos (pos,flotte) :
    for i in range (len(flotte)):
        for j in (flotte[i]["pos"]) :
            if pos == j :
                return i
            
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
