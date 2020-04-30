from typing import List

from problem_solving_wads.playing_cards.card import Card
from problem_solving_wads.playing_cards.enums import Rank, Suit


class TrucoDeck:
    def __init__(self):
        ranks = list(Rank)
        self._cards = [Card(rank, suit) for suit in Suit for rank in ranks[:6] + ranks[10:]]

    def __len__(self):
        return len(self._cards)

    def __getitem__(self, position: int):
        return self._cards[position]

    def __setitem__(self, key, value: Card):
        self._cards[key] = value

    def deal(self, amount: int) -> List[Card]:
        return [self._cards.pop() for _ in range(amount)]

    def draw(self):
        return self._cards.pop()

    @classmethod
    def get_card_value(cls, card: Card, trump_rank: Rank):
        if card.rank == trump_rank:
            return cls.ORDERED_TRUMP_SUIT[card.suit.name]
        return cls.ORDERED_RANKS[card.rank.name]

    ORDERED_TRUMP_SUIT = {
        "SPADES": 11,
        "DIAMONDS": 12,
        "HEARTS": 13,
        "CLUBS": 14,
    }

    ORDERED_RANKS = {
        "FOUR": 1,
        "FIVE": 2,
        "SIX": 3,
        "SEVEN": 4,
        "QUEEN": 5,
        "JACK": 6,
        "KING": 7,
        "ACE": 8,
        "TWO": 9,
        "THREE": 10,
    }
