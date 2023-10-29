import tkinter as tk
import random

def initializeDeck() -> list:
    """Initialize a shuffled UNO deck."""
    deck = []
    values = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, "SKIP", "DRAW TWO"]
    colors = ["RED", "GREEN", "YELLOW", "BLUE"]
    for color in colors:
        for value in values:
            card = f"{color} {value}"
            deck.append(card)
    random.shuffle(deck)
    return deck

def displayPlayerHand(hand) -> list:
    """Print the player's cards."""
    print("YOUR HAND: ")
    track = 0
    for card in hand:
        track += 1
        print(f"{track}. {card}")

def draw(cards, deck) -> list:
    """Draw card function."""
    drawn = []
    for card in range(cards):
        drawn.append(deck.pop(0))
    return drawn

def play_turn(playerDeck, bottom, deckColor, deckValue):
    player_input = player_input_entry.get()  # Get the input from the Entry widget
    if not player_input:
        result_label.config(text="Please enter a card number.")
        return False

    playerInput = int(player_input)
    
    if playerInput <= 0 or playerInput > len(playerDeck):
        result_label.config(text="Invalid input. Please enter a valid card number.")
        return False

    selected_card = playerDeck[playerInput - 1]
    handColor, handValue = selected_card.split(" ", 1)

    if deckColor == handColor or deckValue == handValue:
        bottom.append(playerDeck.pop(playerInput - 1))
        result_label.config(text=f"Played: {selected_card}")
        return True
    else:
        result_label.config(text="Invalid move. Please select a card with a matching color or value.")
        return False


def update_ui():
    # Update the UI elements
    player_input_entry.delete(0, tk.END)  # Clear the entry field
    displayPlayerHand(playerDeck)
    top_card_label.config(text=f"TOP CARD: {bottom[-1]}")
    deck_color, deck_value = bottom[-1].split(" ", 1)
    if play_turn(playerDeck, bottom, deck_color, deck_value):
        displayPlayerHand(playerDeck)
    if len(playerDeck) == 0:
        result_label.config(text="You win!")

# Create the main application window
root = tk.Tk()
root.title("UNO Game")

# Set the background color
root.configure(bg="lightblue")

# Initialize the UNO deck and create player's hand
deck = initializeDeck()
playerDeck = draw(7, deck)
AIDeck = draw(7, deck)
bottom = [deck.pop(0)]

# Create and configure UI elements
title_label = tk.Label(root, text="UNO Game", font=("Arial", 18), bg="lightblue")
title_label.pack()

top_card_label = tk.Label(root, text=f"TOP CARD: {bottom[-1]}", font=("Arial", 12), bg="lightblue")
top_card_label.pack()

player_input_entry = tk.Entry(root, width=5)
player_input_entry.pack()

play_button = tk.Button(root, text="Play", command=update_ui)
play_button.pack()

result_label = tk.Label(root, text="", font=("Arial", 12), bg="lightblue")
result_label.pack()

update_ui()  # Initialize the UI

root.mainloop()
