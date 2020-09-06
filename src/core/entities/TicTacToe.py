from core.exceptions import PlayerMovedOutOfItsTurnException

from .Board import Board
from .Coordinate import Coordinate
from .Player import Player


class TicTacToe:

    def __init__(self, id: int, player1: Player, player2: Player):
        self.id = id
        self.player1 = player1
        self.player2 = player2
        self.board = Board()
        self.player_turn = player1

    def make_move(self, player_id: int, coordinate: Coordinate):
        player = self.player_turn

        if player.id != player_id:
            raise PlayerMovedOutOfItsTurnException()

        player.make_move(self.board, coordinate)

        winner = self.board.get_winner() == player.symbol

        if not winner:
            self.change_players()

        return winner

    def change_players(self):
        self.player_turn = list(filter(lambda x: x.id != self.player_turn.id, [self.player1, self.player2]))[0]

    def restart(self):
        self.change_players()
        self.board = Board()