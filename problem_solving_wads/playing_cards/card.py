from dataclasses import dataclass

from problem_solving_wads.playing_cards.enums import Rank, Suit


@dataclass
class Card:
    rank: Rank
    suit: Suit

    def __str__(self):
        return f"{self.rank.value} {self.suit.value}"

    def __repr__(self):
        return str(self)
