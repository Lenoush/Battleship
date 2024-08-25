from matrice import plot_grid
from utils import string_from_pos, random_position, pos_from_string
from bateau import id_bateau_at_pos, presence_bateau
from re import search
from typing import List, Dict, Tuple

# Constants for the different states of the grid
WATER = "O"
HIT = "X"
EMPTY = "."
DESTROYED = "@"

def ai_easy_turn(matrix: List[List[str]], fleet: List[Dict[str, any]], exception: bool = False) -> List[List[str]]:
    """
    Function allowing the AI to choose a random, unattacked position and fire at it.

    Args:
        matrix (List[List[str]]): The game grid.
        fleet (List[Dict[str, any]]): The enemy fleet.
        exception (bool): Indicates if the shot should be treated as a difficult shot.

    Returns:
        List[List[str]]: The updated grid after the shot.
    """
    pos = random_position()
    while matrix[pos[0]][pos[1]] != EMPTY:
        pos = random_position()

    if exception:
        return fire(matrix, pos, fleet, 'AI', level="d")
    else:
        return fire(matrix, pos, fleet, 'AI')

def ai_difficult_turn(matrix: List[List[str]], fleet: List[Dict[str, any]]) -> List[List[str]]:
    """
    Function allowing the AI to choose a position to attack. If a ship is partially hit,
    the AI continues to attack the surrounding  . Otherwise, it chooses a random position.

    Args:
        matrix (List[List[str]]): The game grid.
        fleet (List[Dict[str, any]]): The enemy fleet.

    Returns:
        List[List[str]]: The updated grid after the shot.
    """
    for ship in fleet:
        if ship["cases touchées"] != 0:
            for pos_num in ship["pos"]:
                if matrix[pos_num[0]][pos_num[1]] != HIT:
                    return fire(matrix, pos_num, fleet, 'AI', level="d")
    return ai_easy_turn(matrix, fleet, exception=True)

def player_turn(matrix: List[List[str]], fleet: List[Dict[str, any]]) -> List[List[str]]:
    """
    Function allowing the player to choose a position to attack. The position must be available and valid.

    Args:
        matrix (List[List[str]]): The game grid.
        fleet (List[Dict[str, any]]): The enemy fleet.

    Returns:
        List[List[str]]: The updated grid after the shot.
    """
    pos = input("Enter a position to fire: ")
    while search(r"\b[a-j]{1}[0-9]{1}\b", pos) is None:
        pos = input("Enter another position to fire, in the form 'a0', the previous one is not valid: ")
    
    pos = pos_from_string(pos)
    while matrix[pos[0]][pos[1]] != EMPTY:
        pos = input("Enter another position, this one has already been attacked: ")
        while search(r"\b[a-j]{1}[0-9]{1}\b", pos) is None:
            pos = input("Enter another position to fire, in the form 'a0', the previous one is not valid: ")
        pos = pos_from_string(pos)
    
    return fire(matrix, pos, fleet, 'Player')

def fire(matrix: List[List[str]], pos: Tuple[int, int], fleet: List[Dict[str, any]], name: str, level: str = "e") -> List[List[str]]:
    """
    Function allowing a shot to be fired at a specific position in the grid. The function handles cases
    where the shot hits a ship or not, and updates the grid and fleet accordingly.

    Args:
        matrix (List[List[str]]): The game grid.
        pos (Tuple[int, int]): The target position of the shot.
        fleet (List[Dict[str, any]]): The enemy fleet.
        name (str): The name of the shooter (AI or Player).
        level (str): The difficulty level of the shot (e for easy, d for difficult).

    Returns:
        List[List[str]]: The updated grid after the shot.
    """
    index = id_bateau_at_pos(pos, fleet)
    pos_str = string_from_pos(pos)

    if matrix[pos[0]][pos[1]] != EMPTY:
        print(f"This position {pos_str} has already been attacked")
    else:
        print(f"This position {pos_str} has not been attacked yet")
        if presence_bateau(pos, fleet):  # If the position is occupied, the shot is a hit.
            matrix[pos[0]][pos[1]] = HIT
            print("HIT, Well done")
            fleet[index]["cases touchées"] += 1
            if fleet[index]["taille"] == fleet[index]["cases touchées"]:  # The entire ship has been destroyed.
                print(f"HIT-SUNK: CONGRATULATIONS, YOU HAVE SUNK THE {fleet[index]['nom']}")
                for i in fleet[index]["pos"]:
                    matrix[i[0]][i[1]] = DESTROYED  # All positions of the ship are marked as DESTROYED.
                plot_grid(matrix)
                fleet.pop(index)  # Remove the destroyed ship from the fleet list.
            else:  # If the shot is a hit but the ship is not destroyed, take another turn.
                if name == 'AI':
                    if level == "e":
                        ai_easy_turn(matrix, fleet)
                    else:
                        ai_difficult_turn(matrix, fleet)
                elif name == 'Player':
                    plot_grid(matrix)
                    player_turn(matrix, fleet)
        else:  # If the position is empty, the shot is a miss.
            matrix[pos[0]][pos[1]] = WATER
            print("MISS, Too bad")
            plot_grid(matrix)
    
    return matrix
