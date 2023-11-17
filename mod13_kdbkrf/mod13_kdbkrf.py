import unittest
from unittest.mock import patch
from datetime import datetime
import re
from userInput import is_valid_end_date, is_valid_chart_type, is_valid_date, is_valid_stock_symbol, is_valid_time_series

class TestStockVisualizerInputs(unittest.TestCase):

    def test_valid_stock_symbol(self):
        self.assertTrue(is_valid_stock_symbol('AAPL'))

    def test_invalid_stock_symbol(self):
        self.assertFalse(is_valid_stock_symbol('invalid'))

    def test_valid_chart_type(self):
        self.assertTrue(is_valid_chart_type('1'))

    def test_invalid_chart_type(self):
        self.assertFalse(is_valid_chart_type('3'))

    def test_valid_time_series(self):
        self.assertTrue(is_valid_time_series('2'))

    def test_invalid_time_series(self):
        self.assertFalse(is_valid_time_series('5'))

    def test_valid_start_date(self):
        self.assertTrue(is_valid_date('2023-05-01'))

    def test_invalid_start_date(self):
        self.assertFalse(is_valid_date('2023-13-01'))

    def test_valid_end_date(self):
        self.assertTrue(is_valid_end_date('2023-05-01', '2023-06-01'))

    def test_invalid_end_date(self):
        self.assertFalse(is_valid_end_date('2023-06-01', '2023-05-01'))

if __name__ == '__main__':
    unittest.main()
