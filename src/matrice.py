
N = 10
COLONNES = [" "] + [str(i) for i in range (N)]
VIDE = "."
BATEAU = "#"

# Creation Matrice Vide ( avec seulement des points )
def create_grid() :
    matrice = []
    for i in range(N) :
        l =  []
        for j in range(N) :
            l.append(VIDE)
        matrice.append(l)
    return(matrice)

# Transforme une Matrice lambda en grille a Jouer 
def plot_grid(matrice) :
    PetiteList = []
    LIGNES = list(map(chr,range(97,107)))
    GrandeList = [COLONNES] 
    VarIncrementé = 1

    for i in LIGNES :
        PetiteList = [i] + matrice[LIGNES.index(i)] 
        GrandeList.append(PetiteList)
    for i in GrandeList :
        for j in i :
            if VarIncrementé % 11 == 0 :
                VarIncrementé = VarIncrementé +1
                print ( j , end=" \n")
            else :
                VarIncrementé = VarIncrementé +1
                print ( j , end =" ")
    return ""

#Transforme une Matrice lambda en grille a Jouer Decouverte en fonction de la flotte du joueur
def plot_flotte_grid(M,flotte):
    for i in range (len(flotte)):
        for pos in (flotte[i]["pos"]) :
            M[pos[0]][pos[1]] = BATEAU
    return (plot_grid(M))
