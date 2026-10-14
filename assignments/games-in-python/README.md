
# 📘 Assignment: Hangman Game

## 🎯 Objective

Build a command-line Hangman game using strings, loops, conditionals, random selection, and user input. The player wins by revealing a randomly selected word before using all available incorrect guesses.

## 📝 Tasks

### 🛠️ Set Up the Game

#### Description
Select a secret word from the provided `words` list and initialize the game state before asking the player to guess.

#### Requirements
Completed program should:

- Select exactly one secret word at random from the provided `words` list.
- Initialize and update a collection of the letters guessed by the player.
- Set the maximum number of incorrect guesses to six and track the number remaining.
- Display each unrevealed letter as an underscore, with one space between positions.


### 🛠️ Run the Guessing Loop

#### Description
Repeatedly prompt the player to guess a letter, update and display the game state, and stop when the word is guessed or no incorrect guesses remain.

#### Requirements
Completed program should:

- Prompt for and accept one letter from the player on each turn.
- Reveal every position of a correctly guessed letter in the secret word.
- Reduce the number of remaining incorrect guesses when the guessed letter is not in the secret word.
- Continue until all letters in the secret word are revealed or all six incorrect guesses are used.
- Display a win message when the player reveals the word.
- When the player uses all six incorrect guesses, display a lose message and reveal the secret word.

For example, after guessing `p` and `o` in the word `python`, display:

```text
p _ _ _ o _
```
