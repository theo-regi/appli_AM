"""By Régi Théo"""
from scripts.assets import Position

from itertools import chain
#-------------------------------------------------------------------------------------------------------
#----------------------------Script pour implémenter les classes portefeuilles--------------------------
#-------------------------------------------------------------------------------------------------------
#Class Portfolio:: to support investment portfolio
class Portfolio:
    """
    Class for investment portfolio

    Functions:
    - calculate_pnl: calculate the PnL of the portfolio
    - calculate_pnl_percent: calculate the PnL percent of the portfolio
    - calculate_returns_positions: calculate the returns of the portfolio positions
    - calculate_tracks_positions: calculate the tracks of the portfolio

    Input:
    - name: str: name of the portfolio
    - positions: dict: list of positions in the portfolio (optional), each position is an object
    """
    #-----todo-----
    #- Interface: Buy / Sell positions, maybe need to rethink the structure of the position dict to target on some ids / isin
    #- Interface: modify invested capital
    #- calculate TRI of the different lines (by regrouping the same support positions)
    #- calculateur des dividendes versées / à venir
    #- matrice de variance / covariance / corrélation des positions
    #- CTR / MCTR
    #- Alpha / Beta
    #- benchmark
    #- FX exposure
    #--------------
    def __init__(self, name:str, positions:dict={}, invested_capital:float=None):
        self.name = name
        self.__positions = positions
        self.__initial_capital = invested_capital

    def calculate_pnl_lat(self) -> float:
        """
        Calculate the unrealized PnL of the portfolio

        Returns: float: Unrealized PnL of the portfolio
        """
        pnl = 0
        for position in self.all_positions:
            pnl += position.pnl
        return pnl

    def calculate_pnl_percent_lat(self) -> float:
        """
        Calculate the unrealized PnL percent of the portfolio

        Returns: float: unrealized PnL percent of the portfolio
        """
        pnl = self.calculate_pnl_lat()
        return pnl / self.calculate_invested_capital_in_pos()

    def calculate_returns_positions(self) -> None:
        """
        Calculate the returns of the portfolio positions (instantiate the variable)
        """
        for position in self.all_positions:
            position.calculate_returns()
        pass

    def calculate_tracks_positions(self) -> None:
        """
        Calculate the tracks of the portfolio
        """
        for position in self.all_positions:
            position.calculate_tracks()
        pass
    
    def calculate_invested_capital_in_pos(self) -> float:
        """
        Calculate the invested capital in the positions

        Returns: float: invested capital in the positions
        """
        invested_capital = 0
        for position in self.all_positions:
            invested_capital += position.invested_capital
        return invested_capital
    
    #Interface functions:
    def modify_invested_capital(self, new_invested_capital:float) -> None:
        """
        Modify the invested capital of the portfolio
        """
        self.__initial_capital = new_invested_capital
        pass

    def buy_position(self, isin:str, position: Position) -> None:
        """
        Buy/Add a position in the portfolio
        """
        if isin not in self.__positions:
            self.__positions[isin] = [position]
        else:
            self.__positions[isin].append(position)
        pass

    #Property functions:
    @property
    def all_positions(self) -> list:
        """
        Return all the positions in the portfolio (list)
        """
        return list(chain.from_iterable(self.__positions.values()))
    
    @property
    def pnl_ptf(self) -> float:
        """
        Calculate the PnL of the portfolio

        Returns: float: PnL of the portfolio (actual value - invested capital)
        """
        value = 0
        for position in self.all_positions:
            value += position.actual_amount
        return value - self.invested_capital
    
    @property
    def pnl_percent_ptf(self) -> float:
        """
        Calculate the PnL percent of the portfolio

        Returns: float: PnL percent of the portfolio (actual value - invested capital)/invested capital
        """
        pnl = self.pnl_ptf
        return pnl / self.invested_capital

    @property
    def actual_capital(self) -> float:
        """
        Calculate the actual capital of the portfolio

        Returns: float: actual capital of the portfolio (actual value of the portfolio)
        """
        actual_capital = 0
        for position in self.all_positions:
            actual_capital += position.actual_amount
        return actual_capital

    @property
    def invested_capital(self):
        """"
        Returns how much money is invested.
        """
        if self.__initial_capital is None:
            return self.calculate_invested_capital_in_pos()
        else:
            return self.__initial_capital


