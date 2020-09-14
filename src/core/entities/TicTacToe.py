from src.core.exceptions import PlayerMovedOutOfItsTurnException

from .Board import Board
from .Coordinate import Coordinate
from .Player import Player
from src.core.enums import Symbol


class TicTacToe:

    def __init__(self, player1: Player, player2: Player):
        self.player1 = player1
        self.player1.use_symbol(Symbol.Cross)

        self.player2 = player2
        self.player2.use_symbol(Symbol.Nought)

        self.board = Board()
        self.player_turn = player1

    def make_move(self, player_id: str, coordinate: Coordinate):
        player = self.player_turn

        if player.sid != player_id:
            raise PlayerMovedOutOfItsTurnException()

        player.make_move(self.board, coordinate)

        winner = self.board.get_winner() == player.symbol

        if not winner:
            self.change_turn()

        return winner

    def change_turn(self):
        self.player_turn = list(filter(lambda x: x.sid != self.player_turn.sid, [self.player1, self.player2]))[0]

    def restart(self):
        self.change_turn()
        self.board = Board()

    def to_dict(self):
        return {
            "players": [
                self.player1.to_dict(),
                self.player2.to_dict()
            ],
            "board": self.board.to_dict(),
            "turn": self.player_turn.sid
        }
