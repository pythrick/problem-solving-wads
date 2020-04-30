from dataclasses import dataclass, field
from typing import List

from problem_solving_wads.playing_cards.card import Card


@dataclass
class Player:
    name: str
    score: int = 0
    hand: List[Card] = field(default_factory=list)

    def __str__(self):
        return self.name

    def __repr__(self):
        return str(self)

    def __eq__(self, other):
        return self.name == other.name
