from src.core.enums import Symbol

from .Coordinate import Coordinate


class Field:

    def __init__(self, symbol: Symbol, coordinate: Coordinate):
        self.symbol = symbol
        self.coordinate = coordinate

    def to_dict(self):
        return {
            "symbol": {
                "name": self.symbol.name,
                "value": self.symbol.value
            },
            "coordinate": self.coordinate.to_dict()
        }