# 🔼 Higher-Lower Followers Game (Python CLI)

This is a simple and fun command-line game where you guess who has more followers on social media. Inspired by the classic "Higher or Lower" concept, the game challenges your intuition and memory across multiple rounds.

---

## 🎮 How to Play

- You'll be shown two famous individuals (A and B).
- Each round, you'll guess who has **more followers**.
- If you guess correctly, you continue playing.  
  The previous winner becomes the new challenger (A) for the next round.
- If you're wrong — game over!

---

## 🧠 Features

- Clean and modular Python code structure
- Randomized, non-repeating choices using a shrinking data pool
- Failsafe user input handling (only accepts 'A' or 'B')
- Debug mode to show follower counts for testing
- Auto-looping: replay the game as many times as you like

---

## 🧪 Sample Output

```text
Compare A: Cristiano Ronaldo, a footballer, from Portugal.
vs
Compare B: Ariana Grande, a singer and actress, from USA.

Who has more followers? Type 'A' or 'B': a
Nailed it!👍 Current score: 1

Compare A: Ariana Grande, a singer and actress, from USA.
vs
Compare B: Elon Musk, a CEO, from USA.

Who has more followers? Type 'A' or 'B':
````

---

## 🚀 Getting Started

### Requirements

* Python 3.6+

### Run the Game

```bash
python main.py
```

> Make sure `main.py` has access to:
>
> * `art.py` → stores ASCII art like logos and vs signs
> * `game_data.py` → stores the list of people with follower counts

---

## 📁 Project Structure

```
├── main.py           # Main game logic
├── art.py            # ASCII art graphics
├── game_data.py      # Data source of people and follower counts
└── README.md         # This file
```

---

## 🛠 Developer Notes

* To enable **debug mode**, set `DEBUG_MODE = True` in `main.py`.
* This reveals follower counts for both A and B, and shows how many choices remain.

---

## ✍️ Author

Created by [Sid](https://github.com/siwasitc).
Feel free to fork, contribute, or play around with the game!

---

## 🧠 Future Improvements (Ideas)

* Add scoring leaderboard
* Create a GUI version using `tkinter` or `streamlit`
* Pull live follower data from Instagram or X API
* Add difficulty modes (easy, medium, hard)
