import unittest

from src.core.entities import Player, Board, Coordinate
from src.core.enums import Symbol


class PlayerTest(unittest.TestCase):

    def test_make_move_should_assign_board_field(self):
        board = Board()
        player = Player("1", "John Doe")
        player.use_symbol(Symbol.Nought)
        player.make_move(board, Coordinate(1, 1))

        self.assertEqual(Symbol.Nought, board.fields[0].symbol)
