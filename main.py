import pandas as pd
import numpy as np
import yfinance as yf
import datetime as dt
import streamlit as st

st.set_page_config(page_title='Portfolio Tracker',layout='centered',page_icon=':zap:')
st.subheader('Portfolio Tracker')

file = st.file_uploader('Upload Excel File',accept_multiple_files=False)

if file is None:
    st.stop()
else:
    # read excel file
    df = pd.read_csv(file)
    df = df.sort_values(by='Ticker',ascending=True)
    
    # create a list of tickers
    tickers = df['Ticker']
    tickers = tickers.astype(str)
    tickers_list = tickers.to_list()

    # fetch prices
    #with st.spinner('Please wait'):
    df_2 = yf.download(tickers = tickers_list, period = "5y", interval = "1d")
    prices = df_2['Close']
    prices.index = pd.to_datetime(prices.index)
    #prices = prices.T

    # select start date & today date
    start_date = st.date_input('Select Date')
    today_date = dt.datetime.now().date()

    # diff between start date and today date in days
    diff = today_date - start_date
    diff = diff.days

    # exclude sat and sun
    diff_weekdays = diff - (diff // 7) * 2
    start_date = -(diff_weekdays)

    # show start date and end date data for confirmation
    col1, col2 = st.columns(2)
    with col1:
        start_value = prices.iloc[start_date]
        st.write('Prices on Start Date')
        st.dataframe(start_value)
    with col2:
        end_value = prices.iloc[-1]
        st.write('Prices as on last working date')
        st.dataframe(end_value)
  
    # change in % of stock holding
    pct_change = (end_value - start_value) / start_value * 100
    pct_change = round(pct_change,2)
    pct_change = pct_change.sort_values(ascending=False)
    st.write('Individual / Stock Wise PNL')
    st.dataframe(pct_change,width=300,height=750)

    win = []
    loss = []
    st.subheader(f'Total Portfolio Gain is {round(pct_change.mean(),2)}%')
    for i in pct_change:
        if i > 0:
            win.append(i)
        elif i <= 0:
            loss.append(i)

wincount = len(win)
losscount = len(loss)
winrate = round(wincount/(wincount+losscount)*100,2)

avgwin = round(sum(win)/len(win),2)
avgloss = round(sum(loss)/len(loss),2)
avgrr = round(avgwin/-avgloss,2)

st.text_area('Other Metrics',

f'''Win Trades : {wincount}
Loss Trades : {losscount}
Win Rate : {winrate}%

Avg Win : {avgwin}%
Avg Loss : {avgloss}%
Avg RR : {avgrr}

''',height=300)
