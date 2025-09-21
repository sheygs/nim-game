from src.nim_game.core.game_controller import setup_game, play_game
from src.nim_game.ui.display import show_message
from src.nim_game.ui.input_handler import get_play_again_choice


def main():
    """Main entry point for the Nim game."""
    while True:
        sticks, player_one, player_two, limit = setup_game()

        show_message(f'game state: {(sticks, player_one, player_two, limit)}')

        play_game(sticks, player_one, player_two, limit)

        if not get_play_again_choice():
            show_message('See you next time. 👋')
            break


if __name__ == "__main__":
    main()