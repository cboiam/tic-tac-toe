import unittest

from src.core.entities import *
from src.core.enums import Symbol
from src.core.exceptions import PlayerMovedOutOfItsTurnException


class TicTacToeTest(unittest.TestCase):

    def test_instantiate_assign_symbol_to_players(self):
        player1 = Player("1", "John")
        player2 = Player("2", "Doe")

        tic_tac_toe = TicTacToe(player1, player2)

        self.assertEqual(tic_tac_toe.player1.symbol, Symbol.Cross)
        self.assertEqual(tic_tac_toe.player2.symbol, Symbol.Nought)

    def test_make_move_returns_no_winner_when_new_board(self):
        player1 = Player("1", "John")
        player2 = Player("2", "Doe")

        tic_tac_toe = TicTacToe(player1, player2)

        won = tic_tac_toe.make_move("1", Coordinate(1, 1))

        self.assertFalse(won)

    def test_make_move_returns_winner(self):
        player1 = Player("1", "John")
        player2 = Player("2", "Doe")

        tic_tac_toe = TicTacToe(player1, player2)

        tic_tac_toe.make_move("1", Coordinate(0, 0))
        tic_tac_toe.make_move("2", Coordinate(0, 1))
        tic_tac_toe.make_move("1", Coordinate(1, 1))
        tic_tac_toe.make_move("2", Coordinate(0, 2))
        won = tic_tac_toe.make_move("1", Coordinate(2, 2))

        self.assertTrue(won)

    def test_make_move_raise_exception_when_player_moves_2_times(self):
        player1 = Player("1", "John")
        player2 = Player("2", "Doe")

        tic_tac_toe = TicTacToe(player1, player2)

        tic_tac_toe.make_move("1", Coordinate(0, 0))

        with self.assertRaises(PlayerMovedOutOfItsTurnException) as context:
            tic_tac_toe.make_move("1", Coordinate(0, 0))
            self.assertEqual("You can't move in other players turn!", context.exception.message)

    def test_change_turn_should_change_player_turn_to_player2(self):
        player1 = Player("1", "John")
        player2 = Player("2", "Doe")

        tic_tac_toe = TicTacToe(player1, player2)
        tic_tac_toe.change_turn()

        self.assertEqual("2", tic_tac_toe.player_turn.sid)

    def test_restart_should_change_turn(self):
        player1 = Player("1", "John")
        player2 = Player("2", "Doe")

        tic_tac_toe = TicTacToe(player1, player2)
        tic_tac_toe.restart()

        self.assertEqual("2", tic_tac_toe.player_turn.sid)

    def test_restart_should_reset_board(self):
        player1 = Player("1", "John")
        player2 = Player("2", "Doe")

        tic_tac_toe = TicTacToe(player1, player2)
        tic_tac_toe.make_move("1", Coordinate(0, 0))

        board = tic_tac_toe.board

        tic_tac_toe.restart()

        self.assertNotEqual(board, tic_tac_toe.board)
        self.assertEqual([], tic_tac_toe.board.fields)
