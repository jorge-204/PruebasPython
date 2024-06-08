import unittest
from unittest.mock import patch
import pytest

from app.calc import Calculator


def mocked_validation(*args, **kwargs):
    return True


@pytest.mark.unit
class TestCalculate(unittest.TestCase):
    def setUp(self):
        self.calc = Calculator()

    def test_add_method_returns_correct_result(self):
        self.assertEqual(4, self.calc.add(2, 2))
        self.assertEqual(0, self.calc.add(2, -2))
        self.assertEqual(0, self.calc.add(-2, 2))
        self.assertEqual(1, self.calc.add(1, 0))

    def test_substract_method_returns_correct_result(self):
        self.assertEqual(0, self.calc.substract(2, 2))
        self.assertEqual(1, self.calc.substract(3, 2))
        self.assertEqual(3, self.calc.substract(3, 0))

    def test_divide_method_returns_correct_result(self):
        self.assertEqual(1, self.calc.divide(2, 2))
        self.assertEqual(1.5, self.calc.divide(3, 2))
        self.assertAlmostEqual(0.75, self.calc.divide(3.0, 4.0))
        with self.assertRaises(TypeError):
            self.calc.divide(3, 0)

    def test_multiply_method_returns_correct_result(self):
        self.assertEqual(4, self.calc.multiply(2, 2))
        self.assertEqual(6, self.calc.multiply(3, 2))
        self.assertEqual(0, self.calc.multiply(3, 0))

    def test_power_method_returns_correct_result(self):
        self.assertEqual(4, self.calc.power(2, 2))
        self.assertEqual(9, self.calc.power(3, 2))
        self.assertEqual(1, self.calc.power(3, 0))
        self.assertEqual(9, self.calc.power(-3, 2))
        self.assertEqual(-8, self.calc.power(-2, 3))
        self.assertAlmostEqual(0.25, self.calc.power(2, -2))
        self.assertAlmostEqual(0.125, self.calc.power(2, -3))

    def test_square_root_method_returns_correct_result(self):
        self.assertEqual(2, self.calc.square_root(4))
        self.assertEqual(3, self.calc.square_root(9))
        with self.assertRaises(TypeError):
            self.calc.square_root(-6)

    def test_log_method_returns_correct_result(self):
        self.assertEqual(2, self.calc.log(100))
        self.assertEqual(3, self.calc.log(1000))
        self.assertEqual(0, self.calc.log(1))
        with self.assertRaises(TypeError):
            self.calc.log(-6)

    def test_add_method_fails_with_nan_parameter(self):
        self.assertRaises(TypeError, self.calc.add, "2", 2)
        self.assertRaises(TypeError, self.calc.add, 2, "2")
        self.assertRaises(TypeError, self.calc.add, "2", "2")
        self.assertRaises(TypeError, self.calc.add, None, 2)
        self.assertRaises(TypeError, self.calc.add, 2, None)
        self.assertRaises(TypeError, self.calc.add, object(), 2)
        self.assertRaises(TypeError, self.calc.add, 2, object())

    def test_divide_method_fails_with_nan_parameter(self):
        self.assertRaises(TypeError, self.calc.divide, "2", 2)
        self.assertRaises(TypeError, self.calc.divide, 2, "2")
        self.assertRaises(TypeError, self.calc.divide, "2", "2")
        self.assertRaises(TypeError, self.calc.divide, None, 2)
        self.assertRaises(TypeError, self.calc.divide, 2, None)
        self.assertRaises(TypeError, self.calc.divide, object(), 2)
        self.assertRaises(TypeError, self.calc.divide, 2, object())

    def test_power_method_fails_with_nan_parameter(self):
        self.assertRaises(TypeError, self.calc.power, "2", 2)
        self.assertRaises(TypeError, self.calc.power, 2, "2")
        self.assertRaises(TypeError, self.calc.power, "2", "2")
        self.assertRaises(TypeError, self.calc.power, None, 2)
        self.assertRaises(TypeError, self.calc.power, 2, None)
        self.assertRaises(TypeError, self.calc.power, object(), 2)
        self.assertRaises(TypeError, self.calc.power, 2, object())

    def test_square_root_method_fails_with_nan_parameter(self):
        self.assertRaises(TypeError, self.calc.square_root, "2", 2)
        self.assertRaises(TypeError, self.calc.square_root, 2, "2")
        self.assertRaises(TypeError, self.calc.square_root, "2", "2")
        self.assertRaises(TypeError, self.calc.square_root, None, 2)
        self.assertRaises(TypeError, self.calc.square_root, 2, None)
        self.assertRaises(TypeError, self.calc.square_root, object(), 2)
        self.assertRaises(TypeError, self.calc.square_root, 2, object())

    def test_log_method_fails_with_nan_parameter(self):
        self.assertRaises(TypeError, self.calc.log, "2", 2)
        self.assertRaises(TypeError, self.calc.log, 2, "2")
        self.assertRaises(TypeError, self.calc.log, "2", "2")
        self.assertRaises(TypeError, self.calc.log, None, 2)
        self.assertRaises(TypeError, self.calc.log, 2, None)
        self.assertRaises(TypeError, self.calc.log, object(), 2)
        self.assertRaises(TypeError, self.calc.log, 2, object())


    def test_square_root_method_fails_with_numbers_lesser_than_zero(self):
        self.assertRaises(TypeError, self.calc.square_root, 0)
        self.assertRaises(TypeError, self.calc.square_root, -5)
        self.assertRaises(TypeError, self.calc.square_root, "0")

    def test_log_method_fails_with_numbers_lesser_than_zero(self):
        self.assertRaises(TypeError, self.calc.log, 0)
        self.assertRaises(TypeError, self.calc.log, -5)
        self.assertRaises(TypeError, self.calc.log, "0")

    def test_divide_method_fails_with_division_by_zero(self):
        self.assertRaises(TypeError, self.calc.divide, 2, 0)
        self.assertRaises(TypeError, self.calc.divide, 2, -0)
        self.assertRaises(TypeError, self.calc.divide, 0, 0)
        self.assertRaises(TypeError, self.calc.divide, "0", 0)

    @patch('app.util.validate_permissions', side_effect=mocked_validation, create=True)
    def test_multiply_method_returns_correct_result(self, _validate_permissions):
        self.assertEqual(4, self.calc.multiply(2, 2))
        self.assertEqual(0, self.calc.multiply(1, 0))
        self.assertEqual(0, self.calc.multiply(-1, 0))
        self.assertEqual(-2, self.calc.multiply(-1, 2))


if __name__ == "__main__":  # pragma: no cover
    unittest.main()
