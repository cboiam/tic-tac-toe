from src.core.enums import Symbol

from .Board import Board
from .Coordinate import Coordinate


class Player:

    def __init__(self, sid: str, name: str):
        self.sid = sid
        self.name = name
        self.symbol = Symbol.Empty

    def use_symbol(self, symbol: Symbol):
        self.symbol = symbol

    def make_move(self, board: Board, coordinate: Coordinate):
        board.assign_field(self.symbol, coordinate)
