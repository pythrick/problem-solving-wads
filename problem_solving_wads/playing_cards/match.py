from random import shuffle
from typing import List

from problem_solving_wads.playing_cards.card import Card
from problem_solving_wads.playing_cards.enums import Rank
from problem_solving_wads.playing_cards.player import Player
from problem_solving_wads.playing_cards.truco_deck import TrucoDeck


class Match:
    def __init__(self, players: List[Player]):
        self.players = players
        self.deck = TrucoDeck()
        self.rounds = []
        shuffle(self.deck)

    turn_up: Card

    def deal_cards(self):
        for player in self.players:
            player.hand = self.deck.deal(3)
        self.turn_up = self.deck.draw()

    @property
    def trump_rank(self) -> Rank:
        ranks = list(TrucoDeck.ORDERED_RANKS.keys())
        len_ranks = len(ranks)
        turn_up_index = ranks.index(self.turn_up.rank.name)
        if turn_up_index + 1 >= len_ranks:
            return Rank[ranks[0]]
        return Rank[ranks[turn_up_index + 1]]

    @property
    def player_1_wins(self):
        return sum(1 for r in self.rounds if r.winner and r.winner == self.players[0])

    @property
    def player_2_wins(self):
        return sum(1 for r in self.rounds if r.winner and r.winner == self.players[1])

    @property
    def best_of_three(self):
        return len(self.rounds) == 3 or (self.player_1_wins >= 2 or self.player_2_wins >= 2)

    @property
    def winner(self):
        if self.player_1_wins > self.player_2_wins:
            return self.players[0]
        if self.player_2_wins > self.player_1_wins:
            return self.players[1]
