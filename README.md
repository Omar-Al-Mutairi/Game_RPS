# Multi-Dimensional Rock-Paper-Scissors

This repository contains a small terminal-based game implemented in Python. The game expands the classic Rock–Paper–Scissors by requiring the player to submit **three unique moves** per round. The computer does the same using a random permutation. Whoever wins at least two of the three sub-rounds wins the overall round.

## Software Architecture

The code is organized as a small package under `rpsgame/`:

- `choices.py` – defines the `Choice` enumeration for rock, paper and scissors along with helper utilities.
- `player.py` – contains `Player` base class and two implementations: `HumanPlayer` and `ComputerPlayer`.
- `round.py` – logic for evaluating individual sub-rounds and aggregating their results.
- `game.py` – orchestration of the game loop, keeping score and user interaction.
- `main.py` – entry point that wires the pieces together.

This modular structure keeps responsibilities separated and makes the code easy to extend or test.

## Model Design

- **Choice** – enumeration representing rock, paper or scissors. Includes a method `beats` to check which choice defeats another and a `random_permutation` method for the computer player.
- **Player** – abstract interface with a `choose_moves` method. `HumanPlayer` prompts the user to select three distinct moves, while `ComputerPlayer` simply generates a random permutation of the three choices.
- **RoundResult** – dataclass capturing the moves from both sides and the overall score (positive if the player won more sub-rounds, negative if the computer won).
- **Game** – tracks cumulative scores and runs the main loop.

## Game Flow

1. On starting the game, the player is prompted three times to choose rock, paper or scissors. Duplicate choices are rejected, ensuring all three moves are used in some order.
2. The computer generates its own unique sequence of moves.
3. Each pair of moves is evaluated. Win/loss/tie for sub-rounds is displayed.
4. Winning at least two sub-rounds awards the round to that side. Scores are tracked.
5. The player can continue playing multiple rounds until they choose to stop. Final tallies are printed at the end.

## Quality of Life Features

- **Input Validation** – Typing just the first letter of a choice (e.g. `r`, `p`, `s`) is accepted. Invalid or duplicate entries are re-prompted.
- **Replayability** – After each round, the user can decide whether to play again.
- **Clear Output** – Each round shows the matchup of moves and announces the winner before displaying the running score at game end.

## Running the Game

Ensure you have Python 3.8 or later installed. Run the game from the repository root:

```bash
python main.py
```

Enjoy!
