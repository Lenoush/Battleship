import time
from random import randint, choice
import re
from typing import Tuple, List
from enum import Enum

N = 10
GRID_SIZE = 10
HIDE_DURATION_SHORT = 1
HIDE_DURATION_LONG = 1
CLEAR_LINES = 100


class ShipName(Enum):
    CARRIER = "Carrier"
    BATTLESHIP = "Battleship"
    CRUISER = "Cruiser"
    SUBMARINE = "Submarine"
    DESTROYER = "Destroyer"


NAMES = [ship.value for ship in ShipName]


def string_from_pos(pos: Tuple[int, int]) -> Tuple[str, int]:
    """
    Converts a "number/number" position to a "letter/number" position.

    Args:
        pos (Tuple[int, int]): A position in the format (row, column), where both are integers.

    Returns:
        Tuple[str, int]: The position in the format (letter, number).
    """
    return chr(pos[0] + 97), pos[1]


def random_position() -> Tuple[int, int]:
    """
    Generates a random position within the grid.

    Returns:
        Tuple[int, int]: A random position (row, column) where both are integers within the grid size.
    """
    return randint(0, GRID_SIZE - 1), randint(0, GRID_SIZE - 1)


def random_orientation() -> str:
    """
    Randomly chooses an orientation for the AI's ship placement.

    Returns:
        str: Either "v" for vertical or "h" for horizontal orientation.
    """
    orientations = ["v", "h"]
    return choice(orientations)


def pos_from_string(pos: str) -> Tuple[int, int]:
    """
    Converts a "letter/number" position to a "number/number" position.

    Args:
        pos (str): A position in the format (letter, number), where letter is in 'a-j' and number is in '0-9'.

    Returns:
        Tuple[int, int]: The position as (row, column).

    Raises:
        ValueError: If the input string is not in the correct format.
    """
    if re.match("^[a-j]$", pos[0]) and re.match("^[0-9]$", pos[1]):
        return ord(pos[0]) - 97, int(pos[1])
    raise ValueError(f"Invalid position string: {pos}")


def id_size_from_name(name: str) -> int:
    """
    Returns the index of the ship's size based on its name.

    Args:
        name (str): The name of the ship.

    Returns:
        int: The index corresponding to the ship's size.

    Raises:
        ValueError: If the ship name is not found in NAMES.
    """
    try:
        return NAMES.index(name)
    except ValueError:
        raise ValueError(f"Invalid ship name: {name}")


def clear_screen(lines: int = CLEAR_LINES) -> None:
    """
    Clears the screen by printing a number of empty lines.

    Args:
        lines (int): The number of lines to print. Default is 100.
    """
    for _ in range(lines):
        print(" ")


def short_hide() -> None:
    """
    Pauses the game for 5 seconds, allowing the player to review the board.
    """
    print("\x1b[1;30mYou have 5 seconds to review the game.")
    time.sleep(HIDE_DURATION_SHORT)
    clear_screen()


def long_hide() -> None:
    """
    Pauses the game for a total of 12 seconds, 7 seconds for one player to review the board,
    and 5 seconds for the players to switch.
    """
    print("\x1b[1;30mYou have 7 seconds to review your board.")
    time.sleep(HIDE_DURATION_LONG)
    clear_screen()
    print("Please pass the computer to your opponent, you have 5 seconds.")
    time.sleep(HIDE_DURATION_SHORT)
    clear_screen()


def check_game_end(
    name: str, grid: List[List[int]], fleet: List[str], turn_count: int
) -> bool:
    """
    Checks if a player has won the game. This function should be called at each turn.

    Args:
        name (str): The name of the player.
        grid (List[List[int]]): The game grid.
        fleet (List[str]): The player's fleet, which is a list of remaining ships.
        turn_count (int): The current turn number.

    Returns:
        bool: True if the player has won, otherwise False.
    """
    if len(fleet) == 0:
        print(f"\x1b[4;31m{name} won in {turn_count} turns")
        exit()
    return False
