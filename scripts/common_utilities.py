"""By Régi Théo"""
from abc import ABC, abstractmethod
import yfinance as yf
import pandas as pd
#-------------------------------------------------------------------------------------------------------
#----------------------------Scripts to implement utils classes ----------------------------------------
#-------------------------------------------------------------------------------------------------------
#Class DataSource:: to get data from assets
class DataSource(ABC):
    """
    Class to get data from different sources
    """
    @abstractmethod
    def get_ticker_as_str(self, isin:str=None) -> str:
        """
        Get the ticker of the asset based on the isin and the source of data.

        Input:
        - isin: str: isin of the asset (optional)

        Returns: str: ticker of the asset
        """

        pass

    @abstractmethod
    def fetch_hist_prices(self, isin:str=None, start:str=None, end:str=None) -> pd.Series:
        """
        Fetch historical prices of the asset based on the isin, start and end date."

        Input:
        - isin: str: isin of the asset (optional)
        - start: str: start date (optional)
        - end: str: end date (optional)

        Returns: pd.DataFrame: historical prices of the asset
        """
        pass

#Class YahooFinance:: to get data from Yahoo Finance
class YahooFinance(DataSource): #Could be continuer with other functionnalities
    """
    Class to get data from Yahoo Finance
    """
    def get_ticker_as_obj(self, isin:str) -> yf.Ticker:
        """
        Get the ticker of the asset based on the isin and the source of data.

        Input:
        - isin: str: isin of the asset

        Returns: yf.Ticker: ticker of the asset
        """
        return yf.Ticker(isin)

    def get_ticker_as_str(self, isin:str) -> str:
        """
        Get the ticker of the asset based on the isin and the source of data.

        Input:
        - isin: str: isin of the asset

        Returns: str: ticker of the asset
        """
        return yf.Ticker(isin).info['symbol']

    def fetch_hist_prices(self, isin:str, start:str=None, end:str=None) -> pd.DataFrame:
        """
        Fetch historical prices of the asset based on the isin, start and end date."

        Input:
        - isin: str: isin of the asset
        - start: str: start date (optional)
        - end: str: end date (optional)

        Returns: pd.DataFrame: historical prices of the asset
        """
        try:
            ticker = self.get_ticker_as_str(isin)
            data = yf.download(ticker, start=start, end=end, auto_adjust=True)
            return data['Close']
        except Exception as e:
            print(f"Error: {e}")
            pass

    def fetch_volumes(self, isin:str, start:str=None, end:str=None) -> pd.DataFrame:
        """
        Fetch volumes of the asset based on the isin, start and end date."

        Input:
        - isin: str: isin of the asset
        - start: str: start date (optional)
        - end: str: end date (optional)

        Returns: pd.DataFrame: volumes of the asset
        """
        try:
            ticker = yf.Ticker(isin)
            data = ticker.history(start=start, end=end)['Volume']
            return data
        except Exception as e:
            print(f"Error: {e}")
            pass

    def fetch_dividends(self, isin:str, start:str=None, end:str=None) -> pd.Series:
        """
        Fetch dividends of the asset based on the isin, start and end date."

        Input:
        - isin: str: isin of the asset
        - start: str: start date (optional)
        - end: str: end date (optional)

        Returns: pd.DataFrame: dividends of the asset
        """
        try:
            ticker = yf.Ticker(isin)
            data = ticker.dividends
            return data
        except Exception as e:
            print(f"Error: {e}")
            pass

    def fetch_splits(self, isin:str, start:str=None, end:str=None) -> pd.Series:
        """
        Fetch splits of the asset based on the isin, start and end date."

        Input:
        - isin: str: isin of the asset
        - start: str: start date (optional)
        - end: str: end date (optional)"
        """
        try:
            ticker = yf.Ticker(isin)
            data = ticker.splits
            return data
        except Exception as e:
            print(f"Error: {e}")
            pass

    def fetch_metadata(self, isin:str) -> dict:
        """
        Fetch metadata of the asset based on the isin."

        Input:
        - isin: str: isin of the asset

        Returns: dict: metadata of the asset
        """
        try:
            ticker = yf.Ticker(isin)
            if not ticker: return {}
            data = ticker.info
            return {"name": data['shortName'], "sector": data['sector'], "industry": data['industry'], "country": data['country']}
        except Exception as e:
            print(f"Error: {e}")
            pass
