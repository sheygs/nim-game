import random
from ..core.game_logic import get_divisor


def nim(sticks: int, limit: int) -> int:
    """Computer player that makes random legal moves.

    Args:
        sticks: Number of sticks in the heap
        limit: Maximum number of sticks that can be removed

    Returns:
        Number of sticks to remove
    """
    max_move = min(limit, sticks)
    return random.randint(1, max_move)


def nim_best(sticks: int, limit: int) -> int:
    """Smart computer player that uses optimal strategy.

    Args:
        sticks: Number of sticks in the heap
        limit: Maximum number of sticks that can be removed

    Returns:
        Number of sticks to remove using optimal strategy
    """
    divisor = get_divisor(limit)
    remainder = sticks % divisor

    # If in losing position, play random legal move
    # Otherwise play optimal move
    return nim(sticks, limit) if remainder == 0 else remainder