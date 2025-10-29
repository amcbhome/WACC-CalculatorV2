# wacc_calculator.py

import streamlit as st

st.set_page_config(page_title="WACC Calculator", page_icon="💰")
st.title("💰 Weighted Average Cost of Capital (WACC) Calculator")

st.sidebar.header("Capital Structure Inputs")

# Inputs
equity_value = st.sidebar.number_input("Market Value of Equity (E)", min_value=0.0, value=500000.0)
debt_value = st.sidebar.number_input("Market Value of Debt (D)", min_value=0.0, value=200000.0)
cost_of_equity = st.sidebar.slider("Cost of Equity (Re) %", 0.0, 20.0, 10.0) / 100
cost_of_debt = st.sidebar.slider("Cost of Debt (Rd) %", 0.0, 20.0, 5.0) / 100
tax_rate = st.sidebar.slider("Corporate Tax Rate (Tc) %", 0.0, 50.0, 30.0) / 100

# Calculation
total_value = equity_value + debt_value
equity_weight = equity_value / total_value if total_value else 0
debt_weight = debt_value / total_value if total_value else 0

wacc = (equity_weight * cost_of_equity) + (debt_weight * cost_of_debt * (1 - tax_rate))

# Output
st.subheader("📈 Results")
st.write(f"**Total Capital Value (V):** ${total_value:,.2f}")
st.write(f"**Equity Weight (E/V):** {equity_weight:.2%}")
st.write(f"**Debt Weight (D/V):** {debt_weight:.2%}")
st.write(f"**WACC:** {wacc:.2%}")

st.caption("Formula: WACC = (E/V × Re) + (D/V × Rd × (1 - Tc))")
