"""By Théo Régi"""
import unittest
from scripts.data_sources import YahooFinance
from scripts.assets import Shares
from scripts.portfolio import Portfolio

class TestPorfolio(unittest.TestCase):
    def setUp(self):
        yahoo = YahooFinance()
        self.vk = Shares(
            isin="FR0013506730",
            source=yahoo,
            pru=13.48,
            quantity=247,
            date_achat="2024-01-01"
        )
        self.vk2 = Shares(
            isin="FR0013506730",
            source=yahoo,
            pru=15.48,
            quantity=247,
            date_achat="2024-02-01"
        )
        self.abc = Shares(
            isin="FR0004040608",
            source=yahoo,
            pru=4.67,
            quantity=1337,
            date_achat="2024-06-01"
        )

        self.portfolio = Portfolio("tests_perso")
        self.portfolio.buy_position(self.vk.isin, self.vk)
        self.portfolio.buy_position(self.vk2.isin, self.vk2)
        self.portfolio.buy_position(self.abc.isin, self.abc)


    def test_positions(self):
        self.assertEqual(len(self.portfolio.all_positions), 3)

    def test_invested_capital(self):
        invested_target = 13396.91
        self.assertEqual(self.portfolio.invested_capital, invested_target)

    def test_calculate_pnl_ptf(self):
        pnl = self.portfolio.pnl_ptf
        self.assertAlmostEqual(pnl, 2969.3503, places=2)

    def test_calculate_pnl_percent_ptf(self):
        pnl_percent = self.portfolio.pnl_percent_ptf
        self.assertAlmostEqual(pnl_percent, ((2969.3503)/13396.91), places=2)

    def test_modify_invested_capital(self):
        self.portfolio.modify_invested_capital(20000)
        self.assertEqual(self.portfolio.invested_capital, 20000)

    def test_calculate_pnl_ptf_m(self):
        self.portfolio.modify_invested_capital(20000)
        pnl = self.portfolio.pnl_ptf
        self.assertTrue(pnl<=0)

    def test_calculate_pnl_percent_ptf_m(self):
        self.portfolio.modify_invested_capital(20000)
        pnl_percent = self.portfolio.pnl_percent_ptf
        self.assertTrue(pnl_percent<=0)

if __name__ == "__main__":
    unittest.main()
    