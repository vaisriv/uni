import random
import numpy as np


class HexBlackjack:
    def __init__(self) -> None:
        self.players = {"player": Player("User"), "dealer": Player("Dealer")}
        self.fulldeck = np.repeat(
            np.array([0, "Ace", 2, 3, 4, 5, 6, 7, 8, 9, "A", "B", "C", "D", "E", "F"]),
            4,
        )

    def gameloop(self) -> None:
        return None

    def drawscreen(self) -> None:
        clear()
        return None


class Player:
    def __init__(self, name) -> None:
        self.name = name
        self.score = 0
        self.hand = []

    def getScore(self) -> int:
        return self.score


def main() -> None:
    return None


def clear() -> None:
    """
    clears the console screen using ANSI escape codes.

    Returns
    -------
    None
    """

    # clear screen using ANSI escape codes
    print("\033c\033[3J", end="")
    return None


if __name__ == "__main__":
    main()
