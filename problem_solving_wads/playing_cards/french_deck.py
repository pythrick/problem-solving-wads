from problem_solving_wads.playing_cards.card import Card
from problem_solving_wads.playing_cards.enums import Rank, Suit


class FrenchDeck:
    def __init__(self):
        self._cards = [Card(rank, suit) for suit in Suit for rank in Rank]

    def __len__(self):
        return len(self._cards)

    def __getitem__(self, position: int):
        return self._cards[position]

    def __setitem__(self, key, value: Card):
        self._cards[key] = value

    def pop(self):
        return self._cards.pop()
