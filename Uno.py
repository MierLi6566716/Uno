from enum import Enum
import random

class Color(Enum):
    RED = 1
    GREEN = 2
    BLUE = 3
    YELLOW = 4

class Card:
    def __init__(self, color: Color, value: int):
        self.color = color
        self.value = value

    def getColor(self):
        return self.color

    def getValue(self):
        return self.value

def main() -> None:
    "Entry point of the program and game loop"
    win: bool = False
    total: int = 112
    wild: int = 4
    player: bool = True
    deck: list[Card] = InitializeDeck()
    playerDeck: list[Card] = Randomize(deck)
    oppDeck: list[Card] = Randomize(deck)
    pile: list[Card] = [Draw(deck)]

    while (win == False):
        if player == True:
            DisplayGameState(playerDeck, oppDeck, pile)
            playerDeck, pile, win = PlayerTurn(playerDeck, pile, win)
        else:
            oppDeck, pile, win = OppTurn(oppDeck, pile, win)
        player = not player

def InitializeDeck() -> list[Card]:
    "Initialize the Uno deck with standard cards"
    deck: list[Card] = []
    colors = [Color.RED, Color.GREEN, Color.BLUE, Color.YELLOW]
    for color in colors:
        for value in range(10):
            if value != 0:
                deck.append(Card(color, value))
                deck.append(Card(color, value))
    return deck

def OppTurn(oppDeck: list[Card], pile: list[Card], win: bool) -> tuple:
    "(Opponent) Tries to play a card matching either the color or value of the pile, if not, draw from the deck."
    # Assign the color of the top of the deck
    color = pile[-1].getColor()
    for i, card in enumerate(oppDeck):
        # Check if the either the color or value of the card matches any card it has.
        if card.getColor() == color or card.getValue() == pile[-1].getValue():
            pile.append(oppDeck.pop(i))
            if len(oppDeck) == 0:
                win = True
            return oppDeck, pile, win
    # Draw from the deck if no hands.
    oppDeck.append(Draw(deck))
    return oppDeck, pile, win

def PlayerTurn(playerDeck: list[Card], pile: list[Card], win: bool) -> tuple:
    "(Player) Displays cards and lets player choose to play or draw."
    color = pile[-1].getColor()
    # Assign to valid_cards the cards of which its color or value matches that of the deck
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

def Randomize(deck: list[Card]) -> list[Card]:
    "Randomizing the initial decks"
    random.shuffle(deck)
    return deck

def Draw(deck: list[Card]) -> Card:
    "Drawing a card from the deck"
    return deck.pop(0)

def DisplayGameState(playerDeck: list[Card], oppDeck: list[Card], pile: list[Card]) -> None:
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
