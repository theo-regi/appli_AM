"""By Régi Théo"""
from abc import ABC, abstractmethod
#-------------------------------------------------------------------------------------------------------
#----------------------------Script pour implémenter les classes de bases titres------------------------
#-------------------------------------------------------------------------------------------------------
#Class Position:: Abstract class
class Position(ABC):
    def __init__(self, name:str, isin: str, pru: float=None, quantity: float=0, date_achat: str=None, tickers:dict=None):
        self.name = name
        self.isin = isin

        self.tickers = tickers
        self.pru = pru
        self.quantity = quantity
        self.date_achat = date_achat
        self.type = None        

#Class Shares:: pour supporter les fonctionnalités de bases actions
class Shares(Position):
    def __init__(self, name:str, isin: str=None, pru: float=None, quantity: float=0, date_achat: str=None):
        super().__init__(name, isin, pru, quantity, date_achat)
        self.type = 'Shares'
