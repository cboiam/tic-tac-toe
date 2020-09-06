from core.enums import Symbol

from .Board import Board
from .Coordinate import Coordinate


class Player:

    def __init__(self, id: int, name: str, symbol: Symbol):
        self.id = id
        self.name = name
        self.symbol = symbol

    def make_move(self, board: Board, coordinate: Coordinate):
        board.assign_field(self.symbol, coordinate)