from jeux import player_vs_ai, two_players

CHOICE_PROMPT = "Do you want to play against the computer (enter '1') or against another player (enter '2')? "
DIFFICULTY_PROMPT = "Wich level do you want ? 'd' for difficulty, 'e' for easy : "
INVALID_CHOICE_MESSAGE = "Invalid input. Retry."

def ask_for_game_mode() -> str:
    """
    Asks the user to choose a game mode: against the computer or against another player.
    
    Returns:
        str: '1' to play against the computer, '2' to play against another player.
    """
    choice = input(CHOICE_PROMPT)
    while choice not in {'1', '2'}:
        print(INVALID_CHOICE_MESSAGE)
        choice = input(CHOICE_PROMPT)
    return choice

def ask_for_game_difficulty() -> str:
    """
    Asks the user to choose a game difficulty: only against the computer.
    
    Returns:
        boolean : 'True' for difficulty, 'False' for easy.
    """
    choice = input(DIFFICULTY_PROMPT)
    while choice not in {'d', 'e'}:
        print(INVALID_CHOICE_MESSAGE)
        choice = input(DIFFICULTY_PROMPT)
    if choice == "d" :
        print("You choose the difficult level.")
    else : print("You choose the easy level.")
    return choice

def start_game(mode: str) -> None:
    """
    Starts the game based on the selected mode.

    Args:
        mode (str): '1' to play against the AI, '2' to play against another player.

    """
    if mode == '1':
        print("You chose to play against an AI.")
        level:str = ask_for_game_difficulty()
        player_vs_ai(level)
    elif mode == '2':
        print("You chose to play against another player.")
        two_players()

def main() -> None:
    """
    Main function to select and start the game mode.

    """
    mode = ask_for_game_mode()
    start_game(mode)

if __name__ == "__main__":
    main()
