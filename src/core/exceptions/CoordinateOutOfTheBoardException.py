class CoordinateOutOfTheBoardException(Exception):

    def __init__(self, x_axis, y_axis):
        self.message = f"The coordinates ({x_axis}, {y_axis}) are outside of the board!"
