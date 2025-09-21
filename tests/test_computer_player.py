import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from src.nim_game.players.computer_player import nim, nim_best


def test_nim():
    """Test the basic computer player."""
    move = nim(10, 3)
    assert 1 <= move <= 3

    move = nim(2, 3)
    assert 1 <= move <= 2
    print("✅ Basic computer player tests passed!")


def test_nim_best():
    """Test the optimal computer player."""
    # Test losing position (multiple of divisor)
    move = nim_best(12, 3)  # 12 % 4 = 0, losing position
    assert 1 <= move <= 3

    # Test winning position
    move = nim_best(13, 3)  # 13 % 4 = 1, should return 1
    assert move == 1

    move = nim_best(14, 3)  # 14 % 4 = 2, should return 2
    assert move == 2
    print("✅ Optimal computer player tests passed!")


if __name__ == "__main__":
    test_nim()
    test_nim_best()