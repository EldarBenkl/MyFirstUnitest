import unittest
from rectangle import area


class RectangleTestCase(unittest.TestCase):

    def test_zero_mul(self):
        res = area(10, 0)
        self.assertEqual(res, 0)

    def test_square_mul(self):
        res = area(10, 10)
        self.assertEqual(res, 100)

    def test_float_mul(self):
        res = area(0.5, 0.5)
        self.assertAlmostEqual(res, 0.25)

    def test_rectangle_mul(self):
        res = area(4, 7)
        self.assertEqual(res, 28)

    def test_large_numbers(self):
        res = area(100000, 200000)
        self.assertEqual(res, 20000000000)

    def test_negative_values(self):
        with self.assertRaises(ValueError):
            area(-5, 10)

    def test_invalid_types(self):
        with self.assertRaises(TypeError):
            area("10", "5")
