
# 📘 Assignment: Hangman Game

## 🎯 Objective

Build a command-line Hangman game that uses strings, loops, conditionals, random selection, and user input. The player should reveal a randomly selected word by guessing its letters before running out of incorrect guesses.

## 📝 Tasks

### 🛠️ Set Up the Game

#### Description
Choose a secret word from the provided word list and initialize the variables needed to track the game.

#### Requirements
Completed program should:

- Select one word at random from the provided `words` list.
- Track the letters guessed by the player.
- Set and track a maximum of six incorrect guesses.
- Display each unrevealed letter as an underscore, with spaces between positions.

### 🛠️ Run the Guessing Loop

#### Description
Repeatedly ask the player for a letter, update the game state, and end the game when the word is guessed or no incorrect guesses remain.

#### Requirements
Completed program should:

- Accept a letter guess from the player during each turn.
- Reveal the positions of correctly guessed letters in the secret word.
- Reduce the remaining incorrect guesses when a guess is not in the secret word.
- Continue until the player guesses the full word or uses all six incorrect guesses.
- Display a win message when the word is guessed, or a lose message and the secret word when attempts run out.

Example progress display for the word `python` after guessing `p` and `o`:

```text
p _ _ _ o _
```
