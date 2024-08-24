from enum import Enum
from typing import List
from matrice import plot_grid, plot_flotte_grid, create_grid
from bateau import input_ajout_bateau, nouveau_bateau
from utils import random_orientation, random_position

class ShipName(Enum):
    CARRIER = "Carrier"
    BATTLESHIP = "Battleship"
    CRUISER = "Cruiser"
    SUBMARINE = "Submarine"
    DESTROYER = "Destroyer"

NAMES = [ship.value for ship in ShipName]

def init_joueur() -> List[dict]:
    """
    Initializes the player's fleet based on their input choices.

    The function displays an empty grid first, then prompts the player to place ships one by one.
    The grid updates after each ship is placed.

    Returns:
        List[dict]: A list of dictionaries where each dictionary represents a ship with its properties (e.g., name, position).
    """
    player_fleet = []
    grid = create_grid()

    plot_grid(grid)
    for i in range(len(NAMES)):
        input_ajout_bateau(player_fleet, NAMES[i])
        plot_flotte_grid(grid, player_fleet)

        while len(player_fleet) != i + 1:
            input_ajout_bateau(player_fleet, NAMES[i])
            plot_flotte_grid(grid, player_fleet)

    return player_fleet

def init_ia() -> List[dict]:
    """
    Initializes the AI's fleet with random positions and orientations.

    The function automatically generates ships for the AI by placing them on the grid randomly.
    It ensures that each ship is placed correctly before moving on to the next.

    Returns:
        List[dict]: A list of dictionaries where each dictionary represents a ship with its properties (e.g., name, position).
    """
    ai_fleet = []
    
    for i in range(len(NAMES)):
        while len(ai_fleet) != i + 1:
            nouveau_bateau(ai_fleet, NAMES[i], random_position(), random_orientation())

    return ai_fleet
