import streamlit as st
import yfinance as yf
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Title
st.title("📈 Stock Market Portfolio Analyzer")
st.write("Analyze Indian stocks - Returns, Risk & Correlation")

# Stock Selection
stocks = ["RELIANCE.NS", "TCS.NS", "INFY.NS", "HDFCBANK.NS", "WIPRO.NS"]
selected = st.multiselect("Select Stocks", stocks, default=stocks)

# Date Range
start = st.date_input("Start Date", value=pd.to_datetime("2023-01-01"))
end = st.date_input("End Date", value=pd.to_datetime("2024-01-01"))

# Fetch Data
if st.button("Analyze"):
    st.write("Fetching data...")
    data = yf.download(selected, start=start, end=end)["Close"]
    st.write("### Stock Closing Prices")
    st.line_chart(data)

    # Daily Returns
    returns = data.pct_change().dropna()
    st.write("### Daily Returns")
    st.line_chart(returns)

    # Correlation Heatmap
    st.write("### Correlation Heatmap")
    fig, ax = plt.subplots()
    sns.heatmap(returns.corr(), annot=True, cmap="coolwarm", ax=ax)
    st.pyplot(fig)

    st.success("Analysis Complete!")