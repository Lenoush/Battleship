from initialisation import init_ia, init_joueur
from matrice import plot_flotte_grid, plot_grid, create_grid
from attaque import tour_joueur, tour_ia_random, tour_ia_better_random
from utils import PetitHide, check_fin_partie, hide

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
    while (check_fin_partie('Ordi', J, FlotteJoueur, nb_tour) == False) :
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
        if (check_fin_partie(NomJoueur, M, FlotteIA, nb_tour) == False) :
            print("\x1b[0mAu tour de l'IA d'attaquer.")
            J = tour_ia_better_random(J,FlotteJoueur) 
            PetitHide()


        
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
    while (check_fin_partie(NomJoueur2, MatriceJ1, FlotteJoueur1, nb_tour) == False) :
        nb_tour = nb_tour +1
        print("\x1b[0;31mVotre flotte ",NomJoueur1, " : ")
        plot_flotte_grid(create_grid(),FlotteJoueur1)
        print ("Nb de bateaux encore debout : %d" %(len(FlotteJoueur1)))
        print ("Nb de bateaux coulés : %d" %(5-len(FlotteJoueur1)))
        for i in range(5) : print (" ")
        print (NomJoueur1, " Merci de jouer. Il vous reste %d bateaux à detruire." %(len(FlotteJoueur2)))
        plot_grid(MatriceJ2)
        MatriceJ2 = tour_joueur(MatriceJ2,FlotteJoueur2)
        if (check_fin_partie(NomJoueur1, MatriceJ2, FlotteJoueur2, nb_tour) == False) :
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
