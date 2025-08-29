from enum import Enum
import random

class Choice(Enum):
    ROCK = 'rock'
    PAPER = 'paper'
    SCISSORS = 'scissors'

    def __str__(self) -> str:
        return self.value

    @staticmethod
    def beats(a: 'Choice', b: 'Choice') -> bool:
        """Return True if choice a beats choice b."""
        return (
            (a == Choice.ROCK and b == Choice.SCISSORS) or
            (a == Choice.PAPER and b == Choice.ROCK) or
            (a == Choice.SCISSORS and b == Choice.PAPER)
        )

    @classmethod
    def random_permutation(cls):
        """Return a random permutation of all choices."""
        choices = list(cls)
        random.shuffle(choices)
        return choices

    @classmethod
    def from_input(cls, value: str) -> 'Choice':
        value = value.strip().lower()
        for choice in cls:
            if choice.value.startswith(value):
                return choice
        raise ValueError(f"Invalid choice: {value}")
