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
