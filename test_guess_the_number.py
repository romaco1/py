from gues_number_helper import isNotEqual
import unittest

class TestInputValidation(unittest.TestCase):
    def test_not_equlal_values(self):
        self.assertTrue(isNotEqual(2, 3))
    def test_equal_valus(self):
        self.assertFalse(isNotEqual(2, 2))