"""By Théo Régi"""
#-----------------------------------------------------------------------------------------------------
#------------------------------------SETUP de L'APP---------------------------------------------------
#-----------------------------------------------------------------------------------------------------
import streamlit as st

from constants import APP_DIR
from database import init_db, Session
from services.portfolio_store import PortfolioStore
init_db()
#-------------------------------------------------------------------------------------------------------
#----------------------------Main Script for the App Architecture---------------------------------------
#-------------------------------------------------------------------------------------------------------
#Set up the session state (when launching the streamlit app):
if "portolios" not in st.session_state:
    st.session_state.portfolios = {}

if "selected_portfolio" not in st.session_state:
    st.session_state.selected_portfolio = None

#Loading the portfolio database:
session = Session()
st.session_state.session = session
store = PortfolioStore(session)
loaded = store.load_portfolios()
for name, ptf in loaded.items():
    st.session_state.portfolios[name] = ptf


