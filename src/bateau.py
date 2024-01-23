from utils import id_taille_Nom, pos_from_string

TAILLES = [5,4,3,3,2]

#Verifie si la position pos est deja dans la flotte.
def presence_bateau(pos,flotte):
    for i in range (len(flotte)):
        for j in (flotte[i]["pos"]) :
            if pos == j :
                return True #Il y a deja un bateau sur cette case
    return False #La case est libre

#Fonction qui indique l'indice du bateau,dont la position fait partie, dans la liste flotte 
def id_bateau_at_pos (pos,flotte) :
    for i in range (len(flotte)):
        for j in (flotte[i]["pos"]) :
            if pos == j :
                return i
            
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

