from dataclasses import dataclass
from typing import List, Tuple

from .choices import Choice


def evaluate_subround(player_choice: Choice, computer_choice: Choice) -> int:
    """Return 1 if player wins, -1 if computer wins, 0 for tie."""
    if player_choice == computer_choice:
        return 0
    if Choice.beats(player_choice, computer_choice):
        return 1
    return -1

@dataclass
class RoundResult:
    player_moves: List[Choice]
    computer_moves: List[Choice]
    score: int

    def winner(self) -> str:
        if self.score > 0:
            return 'player'
        if self.score < 0:
            return 'computer'
        return 'tie'


def play_round(player_moves: List[Choice], computer_moves: List[Choice]) -> RoundResult:
    score = 0
    for p_move, c_move in zip(player_moves, computer_moves):
        score += evaluate_subround(p_move, c_move)
    return RoundResult(player_moves, computer_moves, score)
