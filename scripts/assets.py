"""By Régi Théo"""
from abc import ABC, abstractmethod
from scripts.common_utilities import DataSource
import scripts.common_utilities as cu
import pandas as pd
#-------------------------------------------------------------------------------------------------------
#----------------------------Script to implement basic types of assets to invest in---------------------
#-------------------------------------------------------------------------------------------------------
#Class Position:: Abstract class
class Position(ABC):
    """
    Abstract class for financial positions

    Input:
    - name: str: name of the position
    - isin: str: isin of the position
    - source: DataSource: source of data
    - pru: float: price of the position (optional)
    - quantity: float: quantity of the position (optional)
    - date_achat: str: purchase date of the position (optional)
    - tickers: dict: tickers of the position (optional)
    """
    def __init__(self, isin:str=None, source: DataSource=None, name:str=None,  pru:float=None, quantity:float=0, date_achat:str=None, tickers:dict=None):
        self.name = name
        self.isin = isin

        self.tickers = tickers
        self.pru = pru
        self.quantity = quantity
        self.date_achat = date_achat
        self.type = None
        self.source = source

        self._returns = None
        self.tracks = None

#Class Shares:: to support shares positions
class Shares(Position):
    """
    Class for shares positions

    Input:
    - name: str: name of the position
    - isin: str: isin of the position
    - source: DataSource: source of data
    - pru: float: price of the position (optional)
    - quantity: float: quantity of the position (optional)
    - date_achat: str: purchase date of the position (optional)
    - tickers: dict: tickers of the position (optional)
    """

    def __init__(self, isin:str, source:DataSource, name:str=None, pru:float=None, quantity:float=0, date_achat:str=None, tickers:dict=None):
        super().__init__(isin, source, name, pru, quantity, date_achat, tickers)
        self.type = 'Shares'

    def calculate_returns(self) -> pd.DataFrame:
        """
        Calculate the returns of the position.

        Returns: pd.DataFrame: returns of the position
        """
        try:
            prices = self.source.fetch_hist_prices(self.isin, self.date_achat)
            self.returns = cu.calculate_returns(prices)
            pass
        except:
            print('Error: Could not calculate returns')
            pass
    
    def calculate_tracks(self) -> pd.DataFrame:
        """
        Track the cumulative returns based on the current price.

        Returns: pd.DataFrame: tracking of the position
        """
        try:
            returns = self.returns
            if returns is not None:
                self.tracks = cu.calculate_tracks(returns)
            pass
        except:
            print('Error: Could not track the position')
            pass

    @property
    def pnl(self) -> float:
        """
        Calculate the profit and loss of the position based on the current price.

        Returns: float: profit and loss of the position
        """
        if self.pru is None:
            return self.current_price * self.quantity
        else:
            return (self.current_price - self.pru) * self.quantity

    @property    
    def pnl_percent(self) -> float:
        """
        Calculate the profit and loss percentage of the position based on the current price.

        Returns: float: profit and loss percentage of the position
        """
        return (self.pnl / (self.pru * self.quantity))
    
    @property
    def invested_capital(self) -> float:
        """
        Calculate the invested capital of the position.

        Returns: float: invested capital of the position
        """
        return self.pru * self.quantity

    @property
    def actual_amount(self) -> float:
        """
        Calculate the actual amount of the position based on the current price.

        Returns: float: actual amount of the position
        """
        return self.current_price * self.quantity
    
    @property
    def current_price(self) -> float:
        """
        Get the current price of the position.

        Returns: float: current price of the position
        """
        return self.source.get_current_price(isin=self.isin)

#Class Currency:: to support currency positions (may be a cash position or a fx position):
#class Currency(Position):




