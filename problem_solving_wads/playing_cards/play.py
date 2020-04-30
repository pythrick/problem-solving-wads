from dataclasses import dataclass

from problem_solving_wads.playing_cards.card import Card
from problem_solving_wads.playing_cards.enums import Rank
from problem_solving_wads.playing_cards.player import Player
from problem_solving_wads.playing_cards.truco_deck import TrucoDeck


@dataclass
class Play:
    player: Player
    card: Card
    trump_rank: Rank

    @property
    def points(self):
        return TrucoDeck.get_card_value(self.card, self.trump_rank)

    def __gt__(self, other):
        return self.points > other.points

    def __lt__(self, other):
        return self.points < other.points

    def __eq__(self, other):
        return self.points == other.points
