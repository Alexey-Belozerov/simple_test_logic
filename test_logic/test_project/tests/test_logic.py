from django.test import TestCase

from test_project.logic import calculations


class LogicTestCase(TestCase):
    def test_plus(self):
        result = calculations(8, 15, '+')
        self.assertEqual(23, result)
