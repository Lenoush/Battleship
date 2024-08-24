from enum import Enum
from typing import List, Tuple, Dict, Union
from utils import id_size_from_name, pos_from_string
from re import search

TAILLES_SHIP = [5, 4, 3, 3, 2]

def presence_bateau(pos: Tuple[int, int], flotte: List[Dict[str, Union[str, int, List[Tuple[int, int]]]]]) -> bool:
    """
    Checks if the position `pos` is already occupied by a ship in the fleet.

    Args:
        pos (Tuple[int, int]): The position to check.
        flotte (List[Dict[str, Union[str, int, List[Tuple[int, int]]]]]): The fleet list.

    Returns:
        bool: True if the position is occupied, False otherwise.
    """
    for ship in flotte:
        if pos in ship["pos"]:
            return True
    return False

def id_bateau_at_pos(pos: Tuple[int, int], flotte: List[Dict[str, Union[str, int, List[Tuple[int, int]]]]]) -> int:
    """
    Returns the index of the ship in the fleet that occupies the given position.

    Args:
        pos (Tuple[int, int]): The position to check.
        flotte (List[Dict[str, Union[str, int, List[Tuple[int, int]]]]]): The fleet list.

    Returns:
        int: The index of the ship in the fleet, or -1 if no ship occupies the position.
    """
    for i, ship in enumerate(flotte):
        if pos in ship["pos"]:
            return i
    return -1

def nouveau_bateau(flotte: List[Dict[str, Union[str, int, List[Tuple[int, int]]]]], nom: str, pos: Tuple[int, int], orientation: str) -> Union[str, None]:
    """
    Adds a new ship to the fleet with the specified name, position, and orientation.

    Args:
        flotte (List[Dict[str, Union[str, int, List[Tuple[int, int]]]]]): The fleet list.
        nom (str): The name of the ship.
        pos (Tuple[int, int]): The initial position of the ship.
        orientation (str): The orientation of the ship ('h' for horizontal, 'v' for vertical).

    Returns:
        Union[str, None]: An error message if the ship can't be placed, None otherwise.
    """
    ship = {
        'nom': nom,
        'taille': TAILLES_SHIP[id_size_from_name(nom)],
        'cases touchées': 0,
        'pos': [pos],
        'orientation': orientation
    }
    
    for i in range(1, ship['taille']):
        if orientation.lower() == "h":
            if not (0 <= pos[1] + i < 10):
                return "The ship cannot be placed here as it is out of bounds. Please choose another position."
            ship['pos'].append((pos[0], pos[1] + i))
        elif orientation.lower() == "v":
            if not (0 <= pos[0] + i < 10):
                return "The ship cannot be placed here as it is out of bounds. Please choose another position."
            ship['pos'].append((pos[0] + i, pos[1]))
    
    if not presence_bateau_totale(pos, orientation, flotte, nom):
        flotte.append(ship)
    else:
        return "The ship overlaps with another ship. Please choose a different position."

def presence_bateau_totale(pos: Tuple[int, int], orientation: str, flotte: List[Dict[str, Union[str, int, List[Tuple[int, int]]]]], nom: str) -> bool:
    """
    Checks if the entire area where the new ship would be placed is free of other ships.

    Args:
        pos (Tuple[int, int]): The initial position of the ship.
        orientation (str): The orientation of the ship ('h' for horizontal, 'v' for vertical).
        flotte (List[Dict[str, Union[str, int, List[Tuple[int, int]]]]]): The fleet list.
        nom (str): The name of the ship.

    Returns:
        bool: True if there is an overlap with another ship, False otherwise.
    """
    ship_size = TAILLES_SHIP[id_size_from_name(nom)]
    
    for i in range(ship_size):
        if orientation.lower() == 'h':
            if presence_bateau((pos[0], pos[1] + i), flotte):
                return True
        elif orientation.lower() == 'v':
            if presence_bateau((pos[0] + i, pos[1]), flotte):
                return True
    return False

def input_ajout_bateau(flotte: List[Dict[str, Union[str, int, List[Tuple[int, int]]]]], nom: str) -> Union[str, None]:
    """
    Adds a ship to the player's fleet based on user input.

    Args:
        flotte (List[Dict[str, Union[str, int, List[Tuple[int, int]]]]]): The fleet list.
        nom (str): The name of the ship.

    Returns:
        Union[str, None]: An error message if the ship cannot be added, None otherwise.
    """
    ship_size = TAILLES_SHIP[id_size_from_name(nom)]
    
    while True:
        pos = input(f"Enter a position (e.g., 'a0') to place the {nom} (size {ship_size}): ")
        if search(r"\b[a-j]{1}[0-9]{1}\b", pos):
            pos_finale = pos_from_string(pos)
            if not presence_bateau(pos_finale, flotte):
                break
            else:
                print(f"The position {pos} is already occupied. Please choose another.")
        else:
            print(f"Invalid format. Please enter a valid position (e.g., 'a0').")
    
    while True:
        orientation = input("Enter an orientation (h for horizontal, v for vertical): ")
        if search(r"\b[hvHV]\b", orientation):
            break
        else:
            print("Invalid orientation. Please enter 'h' or 'v'.")
    
    if not presence_bateau_totale(pos_finale, orientation, flotte, nom):
        return nouveau_bateau(flotte, nom, pos_finale, orientation)
    else:
        print(f"The {nom} of size {ship_size} cannot be placed at {pos} with orientation {orientation} as it overlaps with another ship.")
        return None
