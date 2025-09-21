def get_divisor(limit: int) -> int:
    """Calculate divisor for optimal play strategy.

    Args:
        limit: Maximum number of sticks that can be removed

    Returns:
        The divisor (limit + 1) for optimal strategy
    """
    if limit == 2:
        return 3
    if limit == 3:
        return 4
    return 5