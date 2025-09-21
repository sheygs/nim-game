from config.constants import PLAYER_LABELS
from ..players.computer_player import nim, nim_best
from ..players.human_player import nim_human
from ..ui.display import show_message
from ..ui.input_handler import get_player_type, get_total_sticks, get_game_limit


def setup_game():
    """Set up game parameters.

    Returns:
        Tuple containing sticks, player_one, player_two, limit
    """
    show_message()
    player_one = get_player_type(1)
    player_two = get_player_type(2)
    limit = get_game_limit()
    sticks = get_total_sticks()

    return sticks, player_one, player_two, limit


def play_game(*args) -> None:
    """Main game loop.

    Args:
        *args: Game parameters (sticks, player_one, player_two, limit)
    """
    sticks, player_one, player_two, limit = args

    show_message(f'Total sticks in the heap: {sticks}')

    move_mapper = {
        "human": nim_human,
        "computer": nim,
        "smart": nim_best
    }

    players = [
        move_mapper[player_one],
        move_mapper[player_two]
    ]

    player_labels = [
        PLAYER_LABELS[player_one],
        PLAYER_LABELS[player_two]
    ]

    current_player = 0

    while sticks > 0:
        move = players[current_player](sticks, limit)
        sticks -= move

        show_message(f'{player_labels[current_player]} player {current_player + 1} removed {move} sticks')
        show_message(f'total sticks left: {sticks}')

        if sticks == 0:
            show_message(f'Game over! {player_labels[current_player]} player {current_player + 1} wins 🚀🎉')
            break

        current_player = 1 if current_player == 0 else 0