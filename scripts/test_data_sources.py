"""By Théo Régi"""
import unittest
import pandas as pd
from scripts.data_sources import YahooFinance

class TestYahooFinance(unittest.TestCase):
    def setUp(self):
        self.yahoo = YahooFinance()


    def test_get_ticker_as_str(self):
        result = self.yahoo.get_ticker_as_str('AAPL')
        self.assertEqual(result, 'AAPL')

    def test_fetch_hist_prices(self):
        result = self.yahoo.fetch_hist_prices('AAPL', '2025-01-01', '2025-01-03')
        self.assertTrue(isinstance(result, pd.DataFrame))
        print(result)

    def test_fetch_dividends(self):
        result = self.yahoo.fetch_dividends('AAPL')
        self.assertTrue(isinstance(result, pd.Series))
        print(result)

    def test_fetch_splits(self):
        result = self.yahoo.fetch_splits('AAPL')
        self.assertTrue(isinstance(result, pd.Series))
        print(result)

    def test_fetch_metadata(self):
        result = self.yahoo.fetch_metadata('AAPL')
        self.assertTrue(isinstance(result, dict))
        self.assertEqual(result['name'], 'Apple Inc.')
        self.assertEqual(result['sector'], 'Technology')
        print(result)

if __name__ == '__main__':
    unittest.main()
