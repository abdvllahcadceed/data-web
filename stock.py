# Importing & Loading Packages and Libraries
import yfinance as yf
import streamlit as st
import pandas as pd

st.markdown('''
# **Stock Price App**
Application built in `Python` + `Streamlit` + `GitHub` by [Abdullahi M. Cadceed](https://twitter.com/@abdullahcadceed)


Shown are the stock **Closing Price** and ***Volume*** of Google!

---
''')

# define the ticker symbol
tickerSymbol = 'GOOGL'

# get data on this ticker
tickerData = yf.Ticker(tickerSymbol)

# get the historical prices for this ticker
tickerDf = tickerData.history(period='id', start='2010-1-1', end='2022-12-31')

# Open high low close volume dividends stock splits
st.write("""
### Closing Price
""")
st.line_chart(tickerDf.Close)
st.write("""
### Volume Price
""")
st.line_chart(tickerDf.Volume)
