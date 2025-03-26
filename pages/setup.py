"""By Théo Régi"""
from scripts.portfolio import Portfolio
from scripts.assets import Shares
from scripts.common_utilities import YahooFinance

import streamlit as st

########################################################################################################
#----------------------------Streamlit page for set_up interractions------------------------------------
########################################################################################################

#____________________________________Parameters_________________________________________________________
list_sources = {"Yahoo Finance": YahooFinance}
list_types = {"Shares": Shares}

#____________________________________Portfolios SetUp___________________________________________________
#------------------------------------Portfolio creation-------------------------------------------------
st.subheader("📁 Create a New Portfolio")
new_ptf_name = st.text_input("Portfolio Name")
invested_capital = st.number_input("Invested Capital")
if invested_capital is not None and invested_capital < 0:
    st.error("❌ Invested capital must be positive or not provided !")

#Create button:
if st.button("Create Portfolio"):
    if new_ptf_name in st.session_state.portfolios:
        st.error("❌ Portfolio already exists !")
    elif new_ptf_name == "":
        st.error("❌ Please enter a name for the portfolio !")
    else:
        st.session_state.portfolios[new_ptf_name] = Portfolio(name=new_ptf_name, invested_capital=invested_capital)
        st.session_state.selected_portfolio = st.session_state.portfolios[new_ptf_name]
        st.success(f"✅ Portfolio {new_ptf_name} created !")

#------------------------------------Portfolio Selection-------------------------------------------------
if st.session_state.portfolios:
    st.subheader("📌 Select a Portfolio to Edit")
    selected_name = st.selectbox("Choose portfolio", list(st.session_state.portfolios.keys()))
    st.session_state.selected_portfolio = st.session_state.portfolios[selected_name]

    #------------------------------------Portfolio Deletion-------------------------------------------
    if st.button("Delete Portfolio"):
        if st.session_state.selected_portfolio is not None:
            del st.session_state.portfolios[selected_name]
            st.session_state.selected_portfolio = None
            st.success("✅ Portfolio deleted !")
else:
    st.info("No portfolio yet. Create one above to get started.")

#____________________________________Positions SetUp_____________________________________________________
if st.session_state.selected_portfolio is not None:
    ptf = st.session_state.selected_portfolio
    #------------------------------------Add Position----------------------------------------------------
    st.subheader(f"➕ Add Position to {ptf.name}")

    isin = st.text_input("ISIN", max_chars=12)
    pru = st.number_input("PRU")
    quantity = st.number_input("Quantity")
    date_achat = st.date_input("Purchase Date")
    source = st.selectbox("Choose source", list(list_sources.keys()))
    type_asset = st.selectbox("Choose type", list(list_types.keys()))

    if st.button("Add Position"):
        if not isin:
            st.error("❌ Please enter an ISIN !")
        elif not source:
            st.error("❌ Please choose a source !")
        elif not type_asset:
            st.error("❌ Please choose a type !")
        else:
            if type_asset == "Shares":
                pos = Shares(isin=isin, source=list_sources[source](), pru=pru, quantity=quantity, date_achat=date_achat.strftime("%Y-%m-%d"))
                ptf.buy_position(isin, pos)
                st.success(f"✅ Added {quantity} units of {isin} to {ptf.name}")
    
