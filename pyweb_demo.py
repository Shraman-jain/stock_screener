import streamlit as st
import pandas as pd
import numpy as np
from plotly import graph_objs as go
import matplotlib.pyplot as plt
import datetime as dt
import yfinance as yf
import pandas_datareader.data as pdr
import math
yf.pdr_override()

st.session_state
st.title('Cal')

sc_list = st.selectbox("SCRIPT LIST",('None','Nifty 500', 'Large Cap', 'Mid Cap','Small Cap'),key='r')
strgy = st.selectbox("STRATEGY LIST",('None','ABC', '44MA', 'BOLLINGER BAND','ATH','15 MIN BUY (ABC)','15 MIN SELL (ABC)','15 MIN BUY (44MA)','15 MIN SELL (44MA)','Trial'),key='e')

incr = st.button('Increment',key="inc")
dec = st.button('DEC',key="dec")
large_list = ['RELIANCE', 'TCS', 'HDFCBANK', 'INFY', 'HINDUNILVR', 'ICICIBANK', 'HDFC', 'BAJFINANCE', 'SBIN', 'WIPRO', 'BHARTIARTL', 'HCLTECH', 'KOTAKBANK', 'ASIANPAINT', 'DMART', 'ITC', 'LT', 'BAJAJFINSV', 'MARUTI', 'TITAN', 'ULTRACEMCO', 'AXISBANK', 'ADANIGREEN', 'SUNPHARMA', 'ADANITRANS', 'ATGL', 'ADANIENT', 'ONGC', 'TECHM', 'TATAMOTORS', 'JSWSTEEL', 'ADANIPORTS'] 
mid_list = ['DEVYANI', 'INDIAMART', 'SUNTV', 'AJANTPHARM', 'SUMICHEM', 'L&TFH', 'SUNDRMFAST', 'HAPPSTMNDS', 'PRESTIGE', 'BCG', 'CARBORUNIV', 'NATIONALUM', 'SKFINDIA', 'CENTRALBK', 'M&MFIN', 'SANOFI', 'ALKYLAMINE', 'NUVOCO', 'AIAENG', 'METROPOLIS', 'FEDERALBNK', 'INDIANB', 'GILLETTE', 'PHOENIXLTD', 'APTUS', 'GRINFRA', 'KPITTECH', 'POONAWALLA', 'GSPL', 'RADICO']
start = dt.datetime.now()- dt.timedelta(days=60)
end = dt.datetime.now() 

try:
    if st.session_state.inc:
        for i in large_list:
            st.write(i)
            sym="{0}.NS".format(i)
            d = pdr.get_data_yahoo(sym,start=start,end=end,interval='1d')
            d = d.reset_index()
            st.dataframe(d)

    if st.session_state.dec:
        for i in mid_list:
            st.write(i)
            sym="{0}.NS".format(i)
            d = pdr.get_data_yahoo(sym,start=start,end=end,interval='1d')
            d = d.reset_index()
            st.dataframe(d)
except Exception as e:
    st.exception(e)
