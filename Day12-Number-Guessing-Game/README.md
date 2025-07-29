# 🎯 Number Guessing Game

A fun and interactive number guessing game built in Python. Challenge yourself to guess a number between 1 and 100 with limited attempts — based on the difficulty level you choose!

---

## 📦 Features

- ✅ Three difficulty levels: `easy`, `normal`, and `hard`
- 🔁 Replayable gameplay loop with customizable attempts
- 🧪 Optional debug mode to reveal the target number
- 🛡️ Input validation for clean and user-friendly experience
- 🎉 Engaging console feedback for player progress

---

## 🧠 How It Works

1. The game randomly generates a number between `1-100`.
2. You select a difficulty level which determines your allowed number of guesses.
3. You guess the number with guidance whether each attempt is `TOO HIGH` or `TOO LOW`.
4. Win by guessing correctly within the allowed attempts. Or lose with style! 😉

---

## 🛠️ Technologies Used

- Python 3.10+
- `random` module for number generation
- Optional ASCII art with `logo` import
- Console-based input/output only

---

## ⚙️ Installation & Usage

```bash
# Clone this repo
git clone https://github.com/YOUR_USERNAME/number-guessing-game.git
cd number-guessing-game

# Run the game
python main.py
