from core.enums import Symbol

from .Coordinate import Coordinate


class Field:

    def __init__(self, symbol: Symbol, coordinate: Coordinate):
        self.symbol = symbol
        self.coordinate = coordinate
