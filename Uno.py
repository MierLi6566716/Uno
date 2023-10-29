from enum import Enum
import random

class Color(Enum):
    RED = 1
    GREEN = 2
    BLUE = 3
    YELLOW = 4

class Card:
    def __init__(self, color: Color, value: str):
        self.color = color
        self.value = value

    def getColor(self):
        return self.color

    def getValue(self):
        return self.value

    def __str__(self):
        return f"{self.color.name} {self.value}"

def main() -> None:
    """Entry point of the program and game loop"""
    win: bool = False
    player: bool = True
    deck: list[Card] = InitializeDeck()
    playerDeck: list[Card] = [Draw(deck) for _ in range(7)]
    oppDeck: list[Card] = [Draw(deck) for _ in range(7)]
    pile: list[Card] = [Draw(deck)]

    while not win:
        if player:
            DisplayGameState(playerDeck, pile)

            # Validate the player's choice
            choice = int(input("Choose a card to play (0 to draw): "))
            while choice < 0 or choice > len(playerDeck):
                choice = int(input("Invalid choice. Please choose again: "))

            # Draw a card if the player chooses to
            if choice == 0:
                card = Draw(deck)
            else:
                card = playerDeck.pop(choice - 1)

            # Play the card
            pile.append(card)

            # Check if the player has won
            if len(playerDeck) == 0:
                win = True
        else:
            oppDeck, pile, win = OppTurn(oppDeck, pile, win)

        player = not player


def InitializeDeck() -> list[Card]:
    """Initialize the Uno deck with standard cards"""
    deck: list[Card] = []
    colors = [Color.RED, Color.GREEN, Color.BLUE, Color.YELLOW]
    values = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "Skip", "Reverse", "Draw Two"]

    for color in colors:
        for value in values:
            deck.append(Card(color, value))

    for _ in range(4):
        deck.append(Card(Color.RED, "Wild"))
        deck.append(Card(Color.RED, "Wild Draw Four"))

    random.shuffle(deck)
    return deck


def OppTurn(oppDeck: list[Card], pile: list[Card], win: bool) -> tuple:
    """(Opponent) Tries to play a card matching either the color or value of the pile, if not, draw from the deck"""
    global deck

    color = pile[-1].getColor()

    # Find a valid card to play
    for card in oppDeck:
        if card.getColor() == color or card.getValue() == pile[-1].getValue() or card.getColor() == Color.RED:
            break

    # Draw a card if there are no valid cards to play
    else:
        card = Draw(deck)

    # Play the card
    pile.append(card)

    # Check if the opponent has won
    if len(oppDeck) == 0:
        win = True

    return oppDeck, pile, win



def PlayerTurn(playerDeck: list[Card], pile: list[Card], win: bool) -> tuple:
    "(Player) Displays cards and lets the player choose to play or draw"
    global deck
    color = pile[-1].getColor()
    valid_cards = [card for card in playerDeck if card.getColor() == color or card.getValue() == pile[-1].getValue()]
    
    if len(valid_cards) > 0:
        DisplayPlayerHand(playerDeck)
        choice = int(input("Choose a card to play (0 to draw): "))
        if choice == 0:
            card = Draw(deck)
        else:
            card = valid_cards[choice - 1]
            playerDeck.remove(card)
        pile.append(card)
        if len(playerDeck) == 0:
            win = True
    else:
        print("No valid cards to play. Drawing a card.")
        pile.append(Draw(deck))
    
    return playerDeck, pile, win

def Draw(deck: list[Card]) -> Card:
    "Drawing a card from the deck"
    return deck.pop(0)

def DisplayGameState(playerDeck: list[Card], pile: list[Card]) -> None:
    "Display the current game state"
    print("Current top card: " + str(pile[-1]))
    print("Your Hand:")
    DisplayPlayerHand(playerDeck)

def DisplayPlayerHand(playerDeck: list[Card]) -> None:
    "Display the player's hand"
    for i, card in enumerate(playerDeck):
        print(f"{i + 1}: {card}")

if __name__ == "__main__":
    main()