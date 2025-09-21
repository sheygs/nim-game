import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from src.nim_game.core.game_logic import get_divisor


def test_get_divisor():
    """Test the get_divisor function."""
    assert get_divisor(2) == 3
    assert get_divisor(3) == 4
    assert get_divisor(4) == 5
    print("✅ All game logic tests passed!")


if __name__ == "__main__":
    test_get_divisor()