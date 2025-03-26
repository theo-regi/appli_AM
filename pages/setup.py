"""By Théo Régi"""
from services.portfolio_store import PortfolioStore

from scripts.portfolio import Portfolio
from scripts.assets import Shares
from scripts.registry import LIST_SOURCES, LIST_TYPES
import streamlit as st

########################################################################################################
#----------------------------Streamlit page for set_up interractions------------------------------------
########################################################################################################

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

st.write("")
st.divider()
st.write("")  
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
            store = PortfolioStore(st.session_state.session)
            res = store.delete_portfolio(selected_name)
            if res == True:
                st.success("✅ Portfolio deleted !")
            else:
                st.error("❌ Portfolio not deleted !")
else:
    st.info("No portfolio yet. Create one above to get started.")

st.write("") 
st.divider()
st.write("")  
#____________________________________Positions SetUp_____________________________________________________
if st.session_state.selected_portfolio is not None:
    ptf = st.session_state.selected_portfolio
    #------------------------------------Add Position----------------------------------------------------
    st.subheader(f"➕ Add Position to {ptf.name}")

    isin = st.text_input("ISIN", max_chars=12)
    pru = st.number_input("PRU")
    quantity = st.number_input("Quantity")
    date_achat = st.date_input("Purchase Date")
    source = st.selectbox("Choose source", list(LIST_SOURCES.keys()))
    type_asset = st.selectbox("Choose type", list(LIST_TYPES.keys()))

    if st.button("Add Position"):
        if not isin:
            st.error("❌ Please enter an ISIN !")
        elif not source:
            st.error("❌ Please choose a source !")
        elif not type_asset:
            st.error("❌ Please choose a type !")
        else:
            if type_asset == "Shares":
                pos = Shares(isin=isin, source=LIST_SOURCES[source](), pru=pru, quantity=quantity, date_achat=date_achat)
                ptf.buy_position(isin, pos)
                st.success(f"✅ Added {quantity} units of {isin} to {ptf.name}")
    
st.write("") 
st.divider()
st.write("")

#------------------------------------Save Porfolio---------------------------------------------------------
if st.session_state.selected_portfolio is not None:
    ptf = st.session_state.selected_portfolio
    if st.button("Save Portfolio"):
        store = PortfolioStore(st.session_state.session)
        store.save_portfolio(ptf)
        st.success(f"✅ Portfolio {ptf.name} saved !")
