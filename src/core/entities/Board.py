from itertools import groupby

from src.core.enums import Symbol
from src.core.exceptions import FieldAlreadyFilledException

from .Coordinate import Coordinate
from .Field import Field


class Board:

    def __init__(self):
        self.fields = []

    def assign_field(self, symbol: Symbol, coordinate: Coordinate):
        existing_coordinate = list(filter(lambda x: x.coordinate.column == coordinate.column and
                                                    x.coordinate.row == coordinate.row,
                                          self.fields))

        if len(existing_coordinate) > 0:
            raise FieldAlreadyFilledException

        self.fields.append(Field(symbol, coordinate))

    def get_winner(self):
        winner = self._get_winner_at(lambda x: x.coordinate.row)

        if winner is Symbol.Empty:
            winner = self._get_winner_at(lambda x: x.coordinate.column)

        if winner is Symbol.Empty:
            winner = self._get_winner_at_diagonal()

        return winner

    def _get_winner_at(self, axis):
        fields = sorted(self.fields, key=axis)
        lines = groupby(fields, axis)

        for line, group in lines:
            winner = self._get_winner_at_line(list(group))
            if winner is not Symbol.Empty:
                return winner

        return Symbol.Empty

    def _get_winner_at_diagonal(self):
        primary_diagonal = list(filter(lambda x: x.coordinate.column == x.coordinate.row, self.fields))
        secondary_diagonal = list(filter(lambda x: x.coordinate.column + x.coordinate.row == Coordinate.maximum, self.fields))

        winner = self._get_winner_at_line(primary_diagonal)

        if winner is Symbol.Empty:
            winner = self._get_winner_at_line(secondary_diagonal)

        return winner

    @staticmethod
    def _get_winner_at_line(line: list):
        symbols = {
            Symbol.Empty: 0,
            Symbol.Nought: 0,
            Symbol.Cross: 0
        }

        for field in line:
            symbols[field.symbol] += 1
            if symbols[field.symbol] == Coordinate.length:
                return field.symbol

        return Symbol.Empty

    def to_dict(self):
        fields = []

        for field in self.fields:
            fields.append(field.to_dict())

        return {
            "fields": fields,
            "size": Coordinate.length
        }
