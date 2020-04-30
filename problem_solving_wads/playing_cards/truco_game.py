import time

from problem_solving_wads.playing_cards.game import Game
from problem_solving_wads.playing_cards.match import Match
from problem_solving_wads.playing_cards.play import Play
from problem_solving_wads.playing_cards.player import Player
from problem_solving_wads.playing_cards.round import Round


def start_game():
    player_a_name = input("What's your name? ")
    player_a = Player(player_a_name)
    player_b_name = input("What's your opponent's name? ")
    player_b = Player(player_b_name)
    time.sleep(0.2)

    game = Game([player_a, player_b])

    while not game.winner:
        print("Starting a new match...\n")
        match = Match(game.players)
        time.sleep(0.2)
        print("Dealing...\n")
        match.deal_cards()
        time.sleep(0.2)
        for player in match.players:
            print(f"{player.name}'s hand: {player.hand}")
        time.sleep(0.2)
        print(f"\nTurn-up: {match.turn_up}\n")

        print("Starting match, best of three...\n")

        while not match.best_of_three:
            plays = []
            for player in match.players:
                options = ", ".join(f"[{i}] {card}" for i, card in enumerate(player.hand))
                selection = int(input(f"{player}, play a card, options {options}: \n"))
                play = Play(
                    card=player.hand.pop(selection),
                    player=player,
                    trump_rank=match.trump_rank
                )
                print(f"{play.player} played the card: {play.card}\n")
                plays.append(play)
                time.sleep(0.2)
            r = Round(plays)
            round_winner = r.winner
            if round_winner:
                print(f"Round winner: {r.winner}. \n")
            else:
                print("The result of this round was a draw.\n")
            match.rounds.append(r)

        time.sleep(0.2)

        print(f"Player {match.winner} scored.\n\n")
        match.winner.score += 1

        time.sleep(0.3)
        for player in match.players:
            print(f"Player {player} current score: {player.score}\n")

        print("-" * 50)
        game.matches.append(match)


if __name__ == '__main__':
    start_game()


# TODO:
# 1 - Play against tha machine
# 2 - Truco negotiation
# 3 - Unit tests
