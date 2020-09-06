from core.exceptions import CoordinateOutOfTheBoardException


class Coordinate:

    maximum = 2
    lenght = 3

    def __init__(self, y_axis: int, x_axis: int):
        if self._is_invalid_axis(x_axis) or self._is_invalid_axis(y_axis):
            raise CoordinateOutOfTheBoardException(x_axis, y_axis)

        self.y_axis = y_axis
        self.x_axis = x_axis

    @staticmethod
    def _is_invalid_axis(axis: int):
        return axis < 0 or axis >= 3
