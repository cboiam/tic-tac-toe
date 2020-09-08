import unittest

from src.core.entities import Coordinate
from src.core.exceptions import CoordinateOutOfTheBoardException


class CoordinateTest(unittest.TestCase):

    def test_create_coordinate_should_succeed_with_both_axis_with_0(self):
        coordinate = Coordinate(0, 0)

        self.assertEqual(0, coordinate.x_axis)
        self.assertEqual(0, coordinate.y_axis)

    def test_create_coordinate_should_succeed_with_both_axis_with_2(self):
        coordinate = Coordinate(2, 2)

        self.assertEqual(2, coordinate.x_axis)
        self.assertEqual(2, coordinate.y_axis)

    def test_create_coordinate_should_raise_exception_when_x_axis_lower_then_0(self):
        with self.assertRaises(CoordinateOutOfTheBoardException) as context:
            Coordinate(-1, 2)
            self.assertEqual("The coordinates (-1, 2) are outside of the board!", context.exception.message)

    def test_create_coordinate_should_raise_exception_when_x_axis_greater_then_2(self):
        with self.assertRaises(CoordinateOutOfTheBoardException) as context:
            Coordinate(3, 2)
            self.assertEqual("The coordinates (3, 2) are outside of the board!", context.exception.message)

    def test_create_coordinate_should_raise_exception_when_y_axis_lower_then_0(self):
        with self.assertRaises(CoordinateOutOfTheBoardException) as context:
            Coordinate(2, -1)
            self.assertEqual("The coordinates (2, -1) are outside of the board!", context.exception.message)

    def test_create_coordinate_should_raise_exception_when_y_axis_greater_then_2(self):
        with self.assertRaises(CoordinateOutOfTheBoardException) as context:
            Coordinate(2, 3)
            self.assertEqual("The coordinates (2, 3) are outside of the board!", context.exception.message)


if __name__ == '__main__':
    unittest.main()
