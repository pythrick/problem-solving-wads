from dataclasses import field, dataclass
from typing import List, Optional

from problem_solving_wads.playing_cards.play import Play
from problem_solving_wads.playing_cards.player import Player


@dataclass
class Round:
    plays: List[Play] = field(default_factory=list)

    @property
    def winner(self) -> Optional[Player]:
        if self.plays[0].points > self.plays[1].points:
            return self.plays[0].player
        if self.plays[1].points > self.plays[0].points:
            return self.plays[1].player
