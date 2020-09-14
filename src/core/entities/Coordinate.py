from src.core.exceptions import CoordinateOutOfTheBoardException


class Coordinate:

    maximum = 2
    length = 3

    def __init__(self, row: int, column: int):
        if self._is_invalid_axis(column) or self._is_invalid_axis(row):
            raise CoordinateOutOfTheBoardException(row, column)

        self.row = row
        self.column = column

    @staticmethod
    def _is_invalid_axis(axis: int):
        return axis < 0 or axis >= 3

    def to_dict(self):
        return {
            "row": self.row,
            "column": self.column
        }
