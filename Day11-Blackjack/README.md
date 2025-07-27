---

# 🃏 Blackjack Game in Python

This is a simple command-line Blackjack game written in Python. It simulates a single-player round against the dealer using standard Blackjack rules.

## 🎯 Features

- Play against the dealer with standard rules
- Automatic score calculation with Ace adjustment
- Automatic reshuffling when cards run low
- Supports multiple decks to simulate house advantage (default: 8)
- Detects Blackjack and Bust conditions
- Dealer logic: draws until 17 or more

## 🧠 Game Logic Highlights

- **Deck Creation**: You can specify how many decks are used. All cards are shuffled at the start.
- **Score Calculation**: Aces are counted as 11 unless total score exceeds 21, in which case they revert to 1.
- **Turns**:
  - Player can hit or pass.
  - Dealer hits until score reaches 17 or higher.
- **End Conditions**: Game declares winner based on final scores with Blackjack and bust detection.

## 🧩 Function Descriptions

### `create_decks(num_of_decks)`
Creates a shuffled deck and a dictionary that maps card ranks to their values in Blackjack.

### `calculate_score(cards)`
Calculates total score of a hand, adjusting Aces from 11 to 1 if needed.

### `player_turn(player, dealer)`
Handles user interaction during the player's turn. Prompts to hit or stand, and checks for bust or Blackjack.

### `dealer_turn(dealer, play_score)`
Handles the dealer's turn based on game rules (draw until 17).

### `compare_score(dealer, deal_score, player, play_score)`
Compares the player’s and dealer’s final scores and prints the result.

### `play_game()`
Runs a full round of Blackjack, dealing cards, handling turns, and evaluating the winner.

## 🔄 How to Play

1. Clone the repository:
   ```bash
   git clone https://github.com/your-username/blackjack-python.git
   ```
2. Run the game:
   ```bash
   python blackjack.py
   ```
3. Follow the prompts to draw cards or pass. Try to beat the dealer without going over 21!

## 📦 Dependencies

Only standard Python libraries are used:
- `random`
- `art` for ASCII logo

## 📌 To-Do / Future Improvements

- Add betting system with chips or currency
- Track win/loss statistics
- Add suits (♠️ ♥️ ♦️ ♣️)
- Support for multiple players
- Visual interface with GUI or web frontend
- Handle reshuffle dynamically during gameplay

## 🧑‍💻 Author

Created and developed as a learning project in Python by [**Siwasit** ](https://github.com/siwasitc).
Happy coding! 🧠⚙️

---
