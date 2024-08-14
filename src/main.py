from jeux import joueur_vs_ia, deux_joueurs

CHOICE_PROMPT = "Do you want to play against the computer (enter '1') or against another player (enter '2')? "
INVALID_CHOICE_MESSAGE = "Invalid input. Please respond with '1' or '2'."

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

def start_game(mode: str) -> None:
    """
    Starts the game based on the selected mode.

    Args:
        mode (str): '1' to play against the AI, '2' to play against another player.

    """
    if mode == '1':
        print("You chose to play against an AI.")
        joueur_vs_ia()
    elif mode == '2':
        print("You chose to play against another player.")
        deux_joueurs()

def main() -> None:
    """
    Main function to select and start the game mode.

    """
    mode = ask_for_game_mode()
    start_game(mode)

if __name__ == "__main__":
    main()
