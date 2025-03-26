"""By Théo Régi"""
from .data_sources import YahooFinance
from .assets import Shares

#Supported sources and types:
LIST_SOURCES = {"YahooFinance": YahooFinance}
LIST_TYPES = {"Shares": Shares}