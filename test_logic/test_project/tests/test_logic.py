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
        self.assertTrue(-7, result)

    def test_minus_wrong(self):
        result = calculations(8, 15, '-')
        self.assertTrue(-5 != -7, result)

    def test_multiply(self):
        result = calculations(8, 15, '*')
