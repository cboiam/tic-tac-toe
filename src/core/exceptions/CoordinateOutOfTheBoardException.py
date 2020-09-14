class CoordinateOutOfTheBoardException(Exception):

    def __init__(self, row, column):
        self.message = f"The coordinates ({row}, {column}) are outside of the board!"
