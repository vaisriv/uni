# Vai Srivastava - 0106

from time import sleep
import random
import numpy as np


def main() -> int:
    """
    Main function to run the card game.

    Sets up the deck and handles the game loop where the player and dealer take turns drawing cards.
    The goal is to reach a score as close as possible to 31 without exceeding it.

    Returns
    -------
    int
        Returns 0 upon exiting the game.
    """
    # Create a deck with values 0 to 'F', repeated 4 times to simulate a full deck
    deck = np.array([0, "Ace", 2, 3, 4, 5, 6, 7, 8, 9, "A", "B", "C", "D", "E", "F"])
    fulldeck = np.repeat(deck, 4)

    clear()  # Clear the screen
    again = 1
    while again:
        newgame = input("Start a new game? (y/n)\n> ")
        if "n" in newgame:
            print("Goodbye!")
            again = 0
            return 0

        # Deal initial hands
        p_hand = random.choices(
            population=fulldeck, k=2
        )  # Player's hand starts with 2 cards
        d_hand = [random.choice(fulldeck)]  # Dealer's hand starts with 1 card
        p_score = calc_score(p_hand)
        d_score = calc_score(d_hand)

        # Show initial hands
        print(hand_text(name="Your", hand=p_hand))
        print(f"Your hand sums to: {p_score}")
        print(hand_text(name="Dealer's", hand=d_hand))
        print(f"Dealer's hand sums to {d_score}")
        sleep(1)

        # Player's turn
        p_more = 1
        while p_more:
            user_more = input("Do you want another card? (y/n)\n> ")
            sleep(1)

            if "n" in user_more:
                p_more = 0

            if p_more:
                # Player draws a new card
                new_card = random.choice(fulldeck)
                p_hand.append(new_card)  # Add the new card to player's hand
                p_score = calc_score(p_hand)

                print(f"You just drew {str(new_card)}")
                print(f"Your hand sums to: {p_score}")

                # Check for winning or busting conditions
                if p_score == 31:
                    p_more = 0
                    game_end(state=1)  # Player wins
                if p_score > 31:
                    p_more = 0
                    game_end(state=4)  # Player busts

        # Dealer's turn if player hasn't already won or busted
        if p_score < 31:
            d_more = 1
            while d_more:
                sleep(1)
                # Dealer draws a new card
                new_card = random.choice(fulldeck)
                d_hand.append(new_card)
                d_score = calc_score(d_hand)

                print(f"Dealer just drew {str(new_card)}")
                print(f"Dealer's hand sums to: {d_score}")

                # Check for dealer bust
                if d_score > 31:
                    d_more = 0
                    game_end(state=1)  # Player wins (dealer busts)

                # Dealer stops drawing if score is over 28
                if d_score > 28:
                    # Compare scores to determine the winner
                    if d_score < p_score:
                        state = 1  # Player wins
                    elif d_score > p_score:
                        state = 2  # Dealer wins
                    else:
                        state = 3  # Tie game

                    d_more = 0
                    game_end(state=state)

    return 0


def calc_score(hand: list) -> int:
    """
    Calculates the total score of a hand based on the card values.

    Parameters
    ----------
    hand : list
        List of cards in the hand.

    Returns
    -------
    int
        The total score of the hand.
    """
    score = 0

    # Assign scores to each card in the hand
    for card in hand:
        cardscore = 0
        match card:
            case 0:
                cardscore = 0
            case "Ace":
                cardscore = 1
            case 2:
                cardscore = 2
            case 3:
                cardscore = 3
            case 4:
                cardscore = 4
            case 5:
                cardscore = 5
            case 6:
                cardscore = 6
            case 7:
                cardscore = 7
            case 8:
                cardscore = 8
            case 9:
                cardscore = 9
            case "A":
                cardscore = 10
            case "B":
                cardscore = 11
            case "C":
                cardscore = 12
            case "D":
                cardscore = 13
            case "E":
                cardscore = 14
            case "F":
                cardscore = 15
        score += cardscore

    return score


def hand_text(name: str, hand: list) -> str:
    """
    Creates a string representation of a hand.

    Parameters
    ----------
    name : str
        The name to be used (e.g., "Your", "Dealer's").
    hand : list
        The list of cards in the hand.

    Returns
    -------
    str
        A formatted string representing the hand.
    """
    hand_str = " and ".join(map(str, hand))
    return f"{name} cards are {hand_str}"


def game_end(state: int) -> None:
    """
    Prints the game result based on the state.

    Parameters
    ----------
    state : int
        The state of the game:
        1 - Player wins
        2 - Dealer wins
        3 - Tie game
        4 - Player busts

    Returns
    -------
    None
    """
    sleep(1)
    match state:
        case 1:
            print("You win!")
        case 2:
            print("Dealer wins!")
        case 3:
            print("No winner.")
        case 4:
            print("Bust. Better luck next time.")


def clear() -> None:
    """
    Clears the console screen.

    Returns
    -------
    None
    """
    print("\033c\033[3J", end="")
    return None


if __name__ == "__main__":
    main()
