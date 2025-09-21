from ..ui.display import show_message


def nim_human(sticks: int, limit: int) -> int:
    """Human player that takes input from user.

    Args:
        sticks: Number of sticks in the heap
        limit: Maximum number of sticks that can be removed

    Returns:
        Number of sticks to remove based on user input
    """
    while True:
        try:
            move = int(input(f'Enter the number of sticks to remove between (1-{limit}) inclusive:\n'))

            if move > sticks:
                raise ValueError('number of sticks removed cannot exceed the total sticks')

            if move < 1 or move > limit:
                raise ValueError(f'Invalid number of sticks! Please enter the sticks to remove within the range (1-{limit})')

            return move
        except ValueError as error:
            show_message(f'error: {error}')