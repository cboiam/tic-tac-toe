import unittest

from src.core.entities import Board, Coordinate
from src.core.enums import Symbol
from src.core.exceptions import FieldAlreadyFilledException


class BoardTest(unittest.TestCase):

    def test_assign_field_should_be_successfully(self):
        board = Board()
        board.assign_field(Symbol.Nought, Coordinate(1, 1))

        self.assertEqual(Symbol.Nought, board.fields[0].symbol)

    def test_assign_field_should_raise_exception_when_field_not_empty(self):
        board = Board()
        board.assign_field(Symbol.Nought, Coordinate(1, 1))

        with self.assertRaises(FieldAlreadyFilledException) as context:
            board.assign_field(Symbol.Nought, Coordinate(1, 1))
            self.assertEqual("Field must be empty to receive a value!", context.exception.message)

    def test_get_winner_returns_empty_when_board_created(self):
        self.assertEqual(Symbol.Empty, Board().get_winner())

    def test_get_winner_returns_empty_when_one_symbol(self):
        board = Board()
        board.assign_field(Symbol.Nought, Coordinate(0, 0))

        self.assertEqual(Symbol.Empty, board.get_winner())

    def test_get_winner_returns_nought_when_row_filled(self):
        board = Board()
        board.assign_field(Symbol.Nought, Coordinate(0, 0))
        board.assign_field(Symbol.Nought, Coordinate(0, 1))
        board.assign_field(Symbol.Nought, Coordinate(0, 2))

        self.assertEqual(Symbol.Nought, board.get_winner())

    def test_get_winner_returns_cross_when_row_filled(self):
        board = Board()
        board.assign_field(Symbol.Cross, Coordinate(0, 0))
        board.assign_field(Symbol.Nought, Coordinate(1, 0))
        board.assign_field(Symbol.Cross, Coordinate(0, 1))
        board.assign_field(Symbol.Nought, Coordinate(1, 1))
        board.assign_field(Symbol.Cross, Coordinate(0, 2))

        self.assertEqual(Symbol.Cross, board.get_winner())

    def test_get_winner_returns_nought_when_column_filled(self):
        board = Board()
        board.assign_field(Symbol.Nought, Coordinate(0, 0))
        board.assign_field(Symbol.Nought, Coordinate(1, 0))
        board.assign_field(Symbol.Nought, Coordinate(2, 0))

        self.assertEqual(Symbol.Nought, board.get_winner())

    def test_get_winner_returns_cross_when_column_filled(self):
        board = Board()
        board.assign_field(Symbol.Cross, Coordinate(0, 0))
        board.assign_field(Symbol.Cross, Coordinate(1, 0))
        board.assign_field(Symbol.Cross, Coordinate(2, 0))

        self.assertEqual(Symbol.Cross, board.get_winner())

    def test_get_winner_returns_nought_when_primary_diagonal_filled(self):
        board = Board()
        board.assign_field(Symbol.Nought, Coordinate(0, 0))
        board.assign_field(Symbol.Nought, Coordinate(1, 1))
        board.assign_field(Symbol.Nought, Coordinate(2, 2))

        self.assertEqual(Symbol.Nought, board.get_winner())

    def test_get_winner_returns_cross_when_primary_diagonal_filled(self):
        board = Board()
        board.assign_field(Symbol.Cross, Coordinate(0, 0))
        board.assign_field(Symbol.Cross, Coordinate(1, 1))
        board.assign_field(Symbol.Cross, Coordinate(2, 2))

        self.assertEqual(Symbol.Cross, board.get_winner())

    def test_get_winner_returns_nought_when_secondary_diagonal_filled(self):
        board = Board()
        board.assign_field(Symbol.Nought, Coordinate(0, 2))
        board.assign_field(Symbol.Nought, Coordinate(1, 1))
        board.assign_field(Symbol.Nought, Coordinate(2, 0))

        self.assertEqual(Symbol.Nought, board.get_winner())

    def test_get_winner_returns_cross_when_secondary_diagonal_filled(self):
        board = Board()
        board.assign_field(Symbol.Cross, Coordinate(0, 2))
        board.assign_field(Symbol.Cross, Coordinate(1, 1))
        board.assign_field(Symbol.Cross, Coordinate(2, 0))

        self.assertEqual(Symbol.Cross, board.get_winner())
