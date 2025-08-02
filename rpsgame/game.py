from dataclasses import dataclass
from typing import Optional

from .player import HumanPlayer, ComputerPlayer
from .round import play_round, RoundResult
from .choices import Choice

@dataclass
class Game:
    player: HumanPlayer
    computer: ComputerPlayer
    player_score: int = 0
    computer_score: int = 0

    def play(self):
        print("Welcome to Multi-Dimensional Rock-Paper-Scissors!")
        while True:
            player_moves = self.player.choose_moves()
            computer_moves = self.computer.choose_moves()
            result = play_round(player_moves, computer_moves)
            self._display_round(result)
            self._update_score(result)
            if not self._prompt_continue():
                break
        self._display_final()

    def _display_round(self, result: RoundResult):
        print("\nRound results:")
        for i, (p, c) in enumerate(zip(result.player_moves, result.computer_moves), 1):
            sub = 'tie'
            if Choice.beats(p, c):
                sub = self.player.name
            elif Choice.beats(c, p):
                sub = self.computer.name
            print(f"  {i}: {p} vs {c} -> {sub}")
        winner = result.winner()
        if winner == 'tie':
            print("Round was a tie!")
        else:
            print(f"{winner.capitalize()} wins the round!")

    def _update_score(self, result: RoundResult):
        if result.score > 0:
            self.player_score += 1
        elif result.score < 0:
            self.computer_score += 1

    def _prompt_continue(self) -> bool:
        ans = input("Play another round? [Y/n]: ").strip().lower()
        return ans in ('', 'y', 'yes')

    def _display_final(self):
        print("\nFinal Score:")
        print(f"{self.player.name}: {self.player_score}")
        print(f"{self.computer.name}: {self.computer_score}")
        if self.player_score == self.computer_score:
            print("Overall result: Tie")
        elif self.player_score > self.computer_score:
            print("Overall result: Player wins!")
        else:
            print("Overall result: Computer wins!")
