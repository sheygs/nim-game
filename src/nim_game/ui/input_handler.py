from config.constants import MIN_STICKS, MAX_STICKS, MIN_LIMIT, MAX_LIMIT, PLAYER_TYPES
from .display import show_message


def get_player_type(player_num: int) -> str:
    """Get player type selection from user.

    Args:
        player_num: Player number (1 or 2)

    Returns:
        Player type string
    """
    try:
        choice = int(input(f'Select a game type for player {player_num}:\n'
                          '1. Human\n'
                          '2. Computer\n'
                          '3. Smart Computer.\n'
                          'Type a number between 1-3 inclusive\n'))

        if choice in PLAYER_TYPES:
            return PLAYER_TYPES[choice]
        else:
            raise ValueError('Invalid user choice. Please try again')

    except ValueError as error:
        show_message(f'error: {error}')
        return get_player_type(player_num)


def get_total_sticks() -> int:
    """Get total number of sticks from user.

    Returns:
        Number of sticks for the game
    """
    while True:
        try:
            sticks = int(input(f'Enter the total number of sticks between {MIN_STICKS} and {MAX_STICKS} inclusive: \n'))

            if sticks < MIN_STICKS or sticks > MAX_STICKS:
                raise ValueError('number of sticks is not within the range. Please try again')

            return sticks
        except ValueError as error:
            show_message(f'error: {error}')


def get_game_limit() -> int:
    """Get maximum sticks per turn from user.

    Returns:
        Maximum number of sticks that can be taken per turn
    """
    while True:
        try:
            limit = int(input(f'Enter the maximum number of sticks players can take from the heap at a time (between {MIN_LIMIT}-{MAX_LIMIT} inclusive):\n'))

            if MIN_LIMIT <= limit <= MAX_LIMIT:
                return limit

            show_message(f'limit must be between {MIN_LIMIT}-{MAX_LIMIT} inclusive')
        except ValueError:
            show_message('Invalid data type for "limit"')


def get_play_again_choice() -> bool:
    """Get user choice for playing again.

    Returns:
        True if user wants to play again, False otherwise
    """
    response = input('Do you want to play again? type (yes or no):\n')
    response = response.strip().lower()
    return response in ["y", "yes"]