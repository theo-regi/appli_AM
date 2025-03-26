"""By Théo Régi"""
#-----------------------------------------------------------------------------------------------------
#------------------------------------SETUP de L'APP---------------------------------------------------
#-----------------------------------------------------------------------------------------------------
import subprocess
import sys
import os
#Absolute path to the scripts folder:
APP_DIR = os.path.dirname(os.path.abspath(__file__))
#Paths for each files:
#ASSETS_DIR = os.path.join(APP_DIR, "Assets")
import streamlit as st

#-------------------------------------------------------------------------------------------------------
#----------------------------Main Script for the App Architecture---------------------------------------
#-------------------------------------------------------------------------------------------------------
#Set up the session state (when launching the streamlit app):
if "portolios" not in st.session_state:
    st.session_state.portfolios = {}

if "selected_portfolio" not in st.session_state:
    st.session_state.selected_portfolio = None


