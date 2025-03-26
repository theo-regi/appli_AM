"""By Théo Régi — Portfolio Overview Page"""
import streamlit as st
import pandas as pd

st.title("📊 Portfolio Overview")

# Check if any portfolios exist
if "portfolios" not in st.session_state or not st.session_state.portfolios:
    st.warning("No portfolio found. Please create one in the Setup page first.")
    st.stop()

# Select portfolio
portfolio_names = list(st.session_state.portfolios.keys())
selected_name = st.selectbox("Select a portfolio", portfolio_names)

# Get the selected portfolio object
ptf = st.session_state.portfolios[selected_name]

# Display positions
positions = ptf.all_positions
if not positions:
    st.info("This portfolio has no positions yet.")
else:
    st.subheader("📋 Held Positions")

    data = []
    for pos in positions:
        data.append({
            "ISIN": pos.isin,
            "Quantity": pos.quantity,
            "PRU": pos.pru,
            "Current Price": pos.current_price,
            "PnL (€)": pos.pnl,
            "PnL (%)": f"{pos.pnl_percent:.2%}",
            "Invested (€)": pos.invested_capital,
            "Actual Value (€)": pos.actual_amount
        })

    df = pd.DataFrame(data)
    st.dataframe(df, use_container_width=True)

    # Display summary metrics
    st.subheader("📈 Portfolio Metrics")
    col1, col2, col3 = st.columns(3)
    col1.metric("Invested Capital", f"{ptf.invested_capital:,.2f} €")
    col1.metric("Actual Capital", f"{ptf.actual_capital:,.2f} €")
    col2.metric("Total PnL", f"{ptf.pnl_ptf:,.2f} €")
    col2.metric("Total PnL (%)", f"{ptf.pnl_percent_ptf:.2%}")
    col3.metric("Unrealized PnL", f"{ptf.calculate_pnl_lat():,.2f} €")
    col3.metric("Unrealized PnL (%)", f"{ptf.calculate_pnl_percent_lat():.2%}")

