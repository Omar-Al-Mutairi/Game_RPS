from __future__ import annotations

from dataclasses import dataclass
from typing import List

from .choices import Choice


def _prompt_choice(index: int, used: List[Choice]) -> Choice:
    """Prompt the user for a choice ensuring no duplicates."""
    while True:
        user_input = input(f"Select move #{index+1} (rock/paper/scissors): ")
        try:
            choice = Choice.from_input(user_input)
        except ValueError as e:
            print(e)
            continue
        if choice in used:
            print("You already used that option. Choose another.")
            continue
        return choice

@dataclass
class Player:
    name: str

    def choose_moves(self) -> List[Choice]:
        raise NotImplementedError

@dataclass
class HumanPlayer(Player):
    def choose_moves(self) -> List[Choice]:
        moves: List[Choice] = []
        for i in range(3):
            moves.append(_prompt_choice(i, moves))
        return moves

@dataclass
class ComputerPlayer(Player):
    def choose_moves(self) -> List[Choice]:
        return Choice.random_permutation()
