---

# 🃏 Blackjack Game in Python

This is a simple command-line Blackjack game written in Python. It simulates a single-player round against the dealer using standard Blackjack rules. The project is designed for beginners and hobbyists interested in game logic, probability, and card-based gameplay.

## 🎯 Features

- Play against the dealer with standard rules
- Automatic score calculation with Ace adjustment
- Supports multiple decks to simulate house advantage
- Detects Blackjack and Bust conditions
- Handles reshuffling when deck size gets low

## 🧠 Game Logic Highlights

- **Deck Creation**: You can specify how many decks are used. All cards are shuffled at the start.
- **Score Calculation**: Aces are counted as 11 unless total score exceeds 21, in which case they revert to 1.
- **Turns**:
  - Player can hit or pass.
  - Dealer hits until score reaches 17 or higher.
- **End Conditions**: Game declares winner based on final scores with Blackjack and bust detection.

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
- Support for multiple players
- Visual interface with GUI or web frontend
- Handle reshuffle dynamically during gameplay

## 🧑‍💻 Author

Created by **Siwasit**  

---
