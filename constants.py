"""By Théo Régi"""
import os

#-----------------------------------------------------------------------------------------------------
#------------------------------------Used to store parameters-----------------------------------------
#-----------------------------------------------------------------------------------------------------
APP_DIR = os.path.dirname(os.path.abspath(__file__))
DATABASE_DIR = os.path.join(APP_DIR, "database")
DATABASE_PATH = os.path.join(DATABASE_DIR, "portfolios.db")
