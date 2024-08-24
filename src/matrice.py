from typing import List

N = 10
COLUMNS = [" "] + [str(i) for i in range(N)]
EMPTY = "."
SHIP = "#"

def create_grid() -> List[List[str]]:
    """
    Creates an empty grid filled with dots.
    
    Returns:
        List[List[str]]: A 2D list representing the grid, filled with EMPTY.
    """
    return [[EMPTY for _ in range(N)] for _ in range(N)]

def plot_grid(matrix: List[List[str]]) -> None:
    """
    Displays the grid in a user-friendly format.
    
    Args:
        matrix (List[List[str]]): The grid to display.
    
    Returns:
        None
    """
    rows = list(map(chr, range(97, 107))) 
    header = COLUMNS
    print(" ".join(header))  

    for i, row in enumerate(rows):
        line = [row] + matrix[i]  
        print(" ".join(line))  


def plot_flotte_grid(matrix: List[List[str]], fleet: List[dict]) -> None:
    """
    Updates the grid to display the player's fleet.
    
    Args:
        matrix (List[List[str]]): The grid to update.
        fleet (List[dict]): A list of ships, each with a "pos" key containing their positions.
    
    Returns:
        None
    """
    for ship in fleet:
        for pos in ship["pos"]:
            matrix[pos[0]][pos[1]] = SHIP  
    plot_grid(matrix)  

