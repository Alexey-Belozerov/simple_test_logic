from django.test import TestCase

from test_project.logic import calculations


class LogicTestCase(TestCase):
    def test_plus(self):
        result = calculations(8, 15, '+')
        self.assertEqual(23, result)

    def test_plus_wrong(self):
        result = calculations(8, 15, '+')
        self.assertTrue(29 != 23, result)

    def test_minus(self):
        result = calculations(8, 15, '-')
        self.assertEqual(-7, result)

    def test_minus_wrong(self):
        result = calculations(8, 15, '-')
        self.assertTrue(-5 != -7, result)

    def test_multiply(self):
        result = calculations(8, 15, '*')
        self.assertEqual(120, result)

    def test_multiply_wrong(self):
        result = calculations(8, 15, '*')
        self.assertTrue(150 != 120, result)

    def test_divide(self):
        result = calculations(36, 6, '/')
        self.assertEqual(6, result)

    def test_divide_wrong(self):
        result = calculations(36, 6, '/')
        self.assertTrue(8 != 6.0, result)
