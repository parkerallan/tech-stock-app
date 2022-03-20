import yfinance as yf
import streamlit as st
import pandas as pd
from PIL import Image
import numpy as np

image = Image.open('logo.png')
st.image(image, caption=None, width=50, use_column_width=None, clamp=False, channels="RGB", output_format="auto")

st.title("""
Top 5 Tech Stocks
""")

#change ticker with selectbox
option = st.selectbox(
     'Select a stock to view',
     ('GOOGL', 'AMZN', 'MSFT', 'AAPL', 'TSLA'))
tickerSymbol = option
#get data on this ticker
tickerData = yf.Ticker(tickerSymbol)
#get historical prices for past 10 years for said ticker
tickerDf = tickerData.history(period='1d', start='2012-03-19')

#show and hide line charts with checkboxes
if st.checkbox(label='Close', value=True):
     st.line_chart(tickerDf.Close)

if st.checkbox(label='Volume', value=True):
     st.line_chart(tickerDf.Volume)

#create/show and hide history dataframe with checkbox
df = pd.DataFrame(
     tickerData.history(interval='3mo', start='2020-01-01')
)

if st.checkbox(label='History', value=True):
     st.table(df)