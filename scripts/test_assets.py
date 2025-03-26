"""By Théo Régi"""
import unittest
from scripts.assets import Shares
from scripts.data_sources import YahooFinance

class TestShares(unittest.TestCase):
    def setUp(self):
        source = YahooFinance()

        self.vk = Shares(
            isin="FR0013506730",
            source=source,
            pru=14.48,
            quantity=494,
            date_achat="2024-01-01"
        )

    def test_calculate_pnl(self):
        pnl = self.vk.pnl
        self.assertAlmostEqual(pnl, 1817.91992, places=2)

    def test_calculate_pnl_percent(self):
        pnl_percent = self.vk.pnl_percent
        self.assertAlmostEqual(pnl_percent, 0.25414, places=4)

    def test_actual_amount(self):
        actual_amount = self.vk.actual_amount
        self.assertAlmostEqual(actual_amount, 8980.92015, places=2)

    def test_invested_capital(self):
        invested_capital = self.vk.invested_capital
        self.assertEqual(invested_capital, 7153.12)

    def test_calculate_returns(self):
        self.vk.calculate_returns()
        returns = self.vk.returns
        self.assertIsNotNone(returns)
        print(returns)

    def test_track(self):
        self.vk.calculate_returns()
        self.vk.calculate_tracks()
        tracks=self.vk.tracks
        self.assertIsNotNone(tracks)
        print(tracks)

if __name__ == "__main__":
    unittest.main()