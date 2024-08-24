from initialisation import init_ia, init_joueur
from matrice import plot_flotte_grid, plot_grid, create_grid
from attaque import player_turn, ai_easy_turn, ai_difficult_turn
from utils import short_hide, check_game_end, long_hide
from typing import List

#Fonction qui fait jouer un jouer x contre l'IA, chacun tire une fois l'un apres l'autre
def player_vs_ai(level: str) -> None:
    """
    Function that runs a game between a player and the AI. Each takes turns firing.

    Args:
        level (str): Difficulty level of the AI ('e' for easy, 'd' for difficult).
    """
    player_name = input("Enter Your Name: ")
    turn_number = 1

    print(f"\x1b[0;31m {player_name} begins initializing their fleet.")
    player_fleet = init_joueur()
    ai_fleet = init_ia()

    for _ in range(5): 
        print(" ")

    print(f"\x1b[1;30mThe game can begin. The AI has created its fleet. \x1b[0;31m {player_name} start attacking:")
    plot_grid(create_grid())

    player_grid = player_turn(create_grid(), ai_fleet)
    short_hide()

    print("\x1b[0mIt's the AI's turn to attack.")
    if level == "e":
        ai_grid = ai_easy_turn(create_grid(), player_fleet)
    else:
        ai_grid = ai_difficult_turn(create_grid(), player_fleet)

    short_hide()

    while not check_game_end('AI', ai_grid, player_fleet, turn_number):
        turn_number += 1
        print(f"\x1b[0;31mYour fleet {player_name}:")
        plot_flotte_grid(create_grid(), player_fleet)
        print(f"Number of ships still afloat: {len(player_fleet)}")
        print(f"Number of ships sunk: {5 - len(player_fleet)}")

        for _ in range(5): 
            print(" ")

        print(f"{player_name}, keep playing. You have {len(ai_fleet)} ships left to destroy.")
        plot_grid(player_grid)
        player_grid = player_turn(player_grid, ai_fleet)
        short_hide()

        if not check_game_end(player_name, player_grid, ai_fleet, turn_number):
            print("\x1b[0mIt's the AI's turn to attack.")
            if level == "e":
                ai_grid = ai_easy_turn(ai_grid, player_fleet)
            else:
                ai_grid = ai_difficult_turn(ai_grid, player_fleet)
            short_hide()

def two_players() -> None:
    """
    Function that runs a game between two players. Each takes turns firing.

    The game alternates between Player 1 and Player 2 until all ships are destroyed.
    """
    player1_name = input("Enter the name of the first player: ")
    player2_name = input("Enter the name of the second player: ")
    turn_number = 1

    for _ in range(5): 
        print(" ")

    print("\x1b[0;31m", player1_name, "begins initializing their fleet. During the game, the screen will be red during your turn.")
    player1_fleet = init_joueur()
    long_hide()

    print("\x1b[0;34mNow it's", player2_name, "'s turn to initialize their fleet. During the game, the screen will be blue during your turn.")
    player2_fleet = init_joueur()
    long_hide()

    print("\x1b[0;31mYour fleet", player1_name, ":")
    plot_flotte_grid(create_grid(), player1_fleet)

    for _ in range(5): 
        print(" ")

    print(player1_name, "can start playing.")
    plot_grid(create_grid())
    grid_p2 = player_turn(create_grid(), player2_fleet)
    long_hide()

    print("\x1b[0;34mYour fleet", player2_name, ":")
    plot_flotte_grid(create_grid(), player2_fleet)

    for _ in range(5): 
        print(" ")

    print(f"Now it's {player2_name}'s turn to play.")
    plot_grid(create_grid())
    grid_p1 = player_turn(create_grid(), player1_fleet)
    long_hide()

    while not check_game_end(player2_name, grid_p1, player1_fleet, turn_number):
        turn_number += 1

        print(f"\x1b[0;31mYour fleet {player1_name}:")
        plot_flotte_grid(create_grid(), player1_fleet)
        print(f"Number of ships still afloat: {len(player1_fleet)}")
        print(f"Number of ships sunk: {5 - len(player1_fleet)}")

        for _ in range(5): 
            print(" ")

        print(f"{player1_name}, keep playing. You have {len(player2_fleet)} ships left to destroy.")
        plot_grid(grid_p2)
        grid_p2 = player_turn(grid_p2, player2_fleet)

        if not check_game_end(player1_name, grid_p2, player2_fleet, turn_number):
            long_hide()
            print(f"\x1b[0;34mYour fleet {player2_name}:")
            plot_flotte_grid(create_grid(), player2_fleet)
            print(f"Number of ships still afloat: {len(player2_fleet)}")
            print(f"Number of ships sunk: {5 - len(player2_fleet)}")

            for _ in range(5): 
                print(" ")

            print(f"{player2_name}, keep playing. You have {len(player1_fleet)} ships left to destroy.")
            plot_grid(grid_p1)
            grid_p1 = player_turn(grid_p1, player1_fleet)
            long_hide()