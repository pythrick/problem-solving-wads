from dataclasses import field, dataclass
from typing import List, Match

from problem_solving_wads.playing_cards.player import Player


@dataclass
class Game:
    players: List[Player]

    matches: List[Match] = field(default_factory=list)

    GOAL_POINTS = 3

    @property
    def winner(self):
        return next((player for player in self.players if player.score >= self.GOAL_POINTS), None)
