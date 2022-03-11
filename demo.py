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

strgy = st.selectbox("STRATEGY LIST",('None','ABC', '44MA', 'BOLLINGER BAND','ATH','15 MIN BUY (ABC)','15 MIN SELL (ABC)','15 MIN BUY (44MA)','15 MIN SELL (44MA)','Rising'),key='strgy')
#st.write("selected",st.session_state.strgy)
sc_list = st.selectbox("SCRIPT LIST",('None','Nifty 500', 'Large Cap', 'Mid Cap','Small Cap'),key="sc_list")
#st.write("selected",st.session_state.sc_list)


st.session_state.mid_list = ['DEVYANI', 'INDIAMART', 'SUNTV', 'AJANTPHARM', 'SUMICHEM', 'L&TFH', 'SUNDRMFAST', 'HAPPSTMNDS', 'PRESTIGE', 'BCG', 'CARBORUNIV', 'NATIONALUM', 'SKFINDIA', 'CENTRALBK', 'M&MFIN', 'SANOFI', 'ALKYLAMINE', 'NUVOCO', 'AIAENG', 'METROPOLIS', 'FEDERALBNK', 'INDIANB', 'GILLETTE', 'PHOENIXLTD', 'APTUS', 'GRINFRA', 'KPITTECH', 'POONAWALLA', 'GSPL', 'RADICO', 'NATCOPHARM', 'CHAMBLFERT', 'WABCOINDIA', 'APLLTD', 'SFL', 'KIOCL', 'CDSL', 'UCOBANK', 'ABSLAMC', 'BSOFT', 'AFFLE', 'BLUEDART', 'TIMKEN', 'DCMSHRIRAM', 'GLENMARK', 'BAJAJELEC', 'WELSPUNIND', 'EXIDEIND', 'MANAPPURAM', 'APOLLOTYRE', 'JBCHEPHARM', 'TTKPRESTIG', 'MOTILALOFS', 'VTL', 'UTIAMC', 'CENTURYPLY', 'BASF', 'NH', 'CAMS', 'MAHABANK', 'FINPIPE', 'ALOKINDS', 'FSL', 'QUESS', 'IIFLWAM', 'SUVENPHAR', 'METROBRAND', 'MEDPLUS', 'KEC', 'CHOLAHLDNG', 'TATAMTRDVR', 'CASTROLIND', 'HINDCOPPER', 'SJVN', 'ZYDUSWELL', 'ZENSARTECH', 'ASAHIINDIA', 'SHRIRAMCIT', 'CESC', 'STLTECH', 'KIMS', 'LXCHEM', 'FINEORG', 'REDINGTON', 'BRIGADE', 'CYIENT', 'ROUTE', 'AMBER', 'GALAXYSURF', 'LATENTVIEW', 'LUXIND', 'BALAMINES', 'ITI', 'BIRLACORPN', 'AMARAJABAT', 'HFCL', 'POWERINDIA', 'IIFL', 'KEI', 'ERIS', 'CENTURYTEX', 'IBULHSGFIN', 'INDIGOPNTS', 'SAREGAMA', 'IDFC', 'JSL', 'INTELLECT', 'CUB', 'GODREJAGRO', 'GRAPHITE', 'ANURAS', 'ANGELONE', 'BLUESTARCO', 'VAIBHAVGBL', 'ALLCARGO', 'VGUARD', 'ELGIEQUIP', 'NETWORK18', 'JUBLPHARMA', 'AKZOINDIA', 'CREDITACC', 'SONATSOFTW', 'POLYMED', 'CGCL', 'LAXMIMACH', 'JUBLINGREA', 'ECLERX', 'RATNAMANI', 'SUZLON', 'MASTEK', 'MAPMYINDIA', 'MAHINDCIE', 'PGHL', 'SHYAMMETL', 'CHEMPLASTS', 'DHANI', 'ASTERDM', 'BSE', 'NLCINDIA', 'FACT', 'MGL', 'TCIEXP', 'SOBHA', 'KNRCON', 'PNBHOUSING', 'GRANULES', 'NBCC', 'JSLHISAR', 'BORORENEW', 'FINCABLES', 'RAIN', 'EIDPARRY', 'IRB', 'ORIENTELEC', 'PVR', 'HUDCO', 'EIHOTEL', 'AEGISCHEM', 'SAPPHIRE', 'ASTRAZEN', 'BBTC', 'PRINCEPIPE', 'GLS', 'BALRAMCHIN', 'AVANTIFEED', 'TV18BRDCST', 'SUNCLAYLTD', 'RBLBANK', 'VIPIND', 'MTARTECH', 'SPARC', 'MRPL', 'NAZARA', 'VMART', 'CANFINHOME', 'RVNL', 'SUNTECK', 'IBREALEST', 'BDL', 'TEAMLEASE', 'GMMPFAUDLR', 'PRIVISCL', 'JMFINANCIL', 'ROSSARI', 'KALYANKJIL', 'SYMPHONY','DELTACORP', 'HGS', 'HEG', 'TATAINVEST', 'GNFC', 'BEML', 'JUSTDIAL', 'EQUITASBNK', 'JKLAKSHMI', 'EDELWEISS', 'HOMEFIRST', 'SIS', 'PNCINFRA', 'MMTC', 'SUPPETRO', 'RTNINDIA', 'GARFIBRES', 'OLECTRA', 'EPL', 'PRSMJOHNSN', 'PSB', 'CAPLIPOINT', 'HIKAL', 'DBL', 'RENUKA', 'RITES', 'SCI', 'CERA', 'PRAJIND', 'SWSOLAR', 'TRITURBINE', 'NIITLTD', 'INDIACEM', 'SUPRAJIT', 'VIJAYA', 'RHIM', 'POLYPLEX', 'TATVA', 'THYROCARE', 'EASEMYTRIP', 'GODFRYPHLP', 'GOCOLORS', 'TCI', 'KRBL', 'CCL', 'MAZDOCK', 'BARBEQUE', 'KALPATPOWR', 'BURGERKING', 'JCHAC','INFIBEAM', 'TRIVENI', 'RALLIS', 'JBMA', 'ESABINDIA', 'GREENPANEL', 'FDC', 'HEIDELBERG', 'VARROC', 'JYOTHYLAB', 'AARTIDRUGS']

st.session_state.large_list = ['RELIANCE', 'TCS', 'HDFCBANK', 'INFY', 'HINDUNILVR', 'ICICIBANK', 'HDFC', 'BAJFINANCE', 'SBIN', 'WIPRO', 'BHARTIARTL', 'HCLTECH', 'KOTAKBANK', 'ASIANPAINT', 'DMART', 'ITC', 'LT', 'BAJAJFINSV', 'MARUTI', 'TITAN', 'ULTRACEMCO', 'AXISBANK', 'ADANIGREEN', 'SUNPHARMA', 'ADANITRANS', 'ATGL', 'ADANIENT', 'ONGC', 'TECHM', 'TATAMOTORS', 'JSWSTEEL', 'ADANIPORTS', 'POWERGRID', 'TATASTEEL', 'HINDZINC', 'HDFCLIFE', 'LTI', 'VEDL', 'PIDILITIND', 'DIVISLAB', 'NTPC', 'SBILIFE', 'ZOMATO', 'HINDALCO', 'GRASIM', 'IOC', 'M&M', 'DABUR', 'NYKAA', 'GODREJCP', 'SHREECEM', 'DLF', 'BAJAJ-AUTO', 'COALINDIA', 'SBICARD', 'HAVELLS', 'BRITANNIA', 'PAYTM', 'SIEMENS', 'BPCL', 'DRREDDY', 'ICICIPRULI', 'MINDTREE', 'INDIGO', 'CIPLA', 'BERGEPAINT', 'AMBUJACEM', 'APOLLOHOSP', 'NAUKRI', 'SRF', 'EICHERMOT', 'TATAPOWER', 'MOTHERSUMI', 'INDUSINDBK', 'ICICIGI', 'TATACONSUM', 'INDUSTOWER', 'IRCTC', 'MARICO', 'MCDOWELL-N', 'MPHASIS', 'GLAND', 'PEL', 'BAJAJHLDNG', 'MUTHOOTFIN', 'LODHA', 'LTTS', 'GAIL', 'UPL', 'TORNTPHARM', 'HDFCAMC', 'GODREJPROP', 'BEL', 'BOSCHLTD', 'PGHH', 'IDBI', 'CADILAHC', 'JSWENERGY', 'HEROMOTOCO', 'JUBLFOOD', 'ABB', 'PIIND', 'ASTRAL', 'STARHEALTH', 'PAGEIND', 'BALKRISIND', 'SAIL', 'IDEA', 'BIOCON', 'GUJGASLTD', 'SONACOMS', 'ALKEM', 'LUPIN', 'AUROPHARMA', 'MAXHEALTH', 'CHOLAFIN', 'POLICYBZR', 'BANKBARODA', 'UBL', 'TATACOMM', 'ACC', 'HINDPETRO', 'PNB', 'BANDHANBNK', 'HAL', 'TTML', 'VOLTAS', 'COLPAL', 'NMDC', 'JINDALSTEL', 'IOB', 'VBL', 'ADANIPOWER', 'TRENT', 'PERSISTENT', 'CONCOR', 'HONAUT', 'POLYCAB', 'TATAELXSI', 'AARTIIND', 'CANBK', 'ASHOKLEY', 'COFORGE', 'MINDAIND', 'DALBHARAT', 'YESBANK', 'OFSS', 'DEEPAKNTR', 'TIINDIA', 'MFSL', 'IGL', 'SRTRANSFIN', 'DIXON', 'RELAXO', 'AUBANK', 'BHARATFORG', 'PETRONET', 'KANSAINER', 'LALPATHLAB', 'PFC', 'OBEROIRLTY', 'MRF', 'NHPC', 'ZEEL', 'IDFCFIRSTB', 'ABCAPITAL', 'IRFC', 'TVSMOTOR', 'GLAXO', 'UNIONBANK', 'LAURUSLABS', '3MINDIA', 'SUPREMEIND', 'GMRINFRA', 'IPCALAB', 'CROMPTON', 'SCHAEFFLER', 'HATSUN', 'TRIDENT', 'ATUL', 'TORNTPOWER', 'FLUOROCHEM', 'CLEAN', 'RECLTD', 'CGPOWER', 'JKCEMENT', 'CUMMINSIND', 'ESCORTS', 'TANLA', 'ISEC', 'ABFRL', 'SUNDARMFIN', 'RUCHI', 'APLAPOLLO', 'SYNGENE', 'GICRE', 'BATAINDIA', 'INDHOTEL', 'ENDURANCE', 'RAMCOCEM', 'PFIZER', 'NIACL', 'EMAMILTD', 'KPRMILL', 'TATACHEM', 'IEX', 'FORTIS', 'WHIRLPOOL', 'COROMANDEL', 'SOLARINDS', 'NAM-INDIA', 'RAJESHEXPO', 'OIL', 'THERMAX', 'GRINDWELL', 'LINDEINDIA', 'GODREJIND', 'BANKINDIA', 'CRISIL', 'NAVINFLUOR', 'AAVAS', 'KAJARIACER', 'BHEL', 'VINATIORGA', 'LICHSGFIN']

try:
    if(st.button("Start Screening",key="str_btn")):
        for i in st.session_state.mid_list:
            st.session_state.sym="{0}.NS".format(i)
            st.session_state.d = pdr.get_data_yahoo(st.session_state.sym,period="max",interval='1d')
            st.session_state.d = st.session_state.d.reset_index()
            st.write(st.session_state.sym)        
            st.dataframe(st.session_state.d)
    if(st.button("S",key="str_btn_2")):
        for j in st.session_state.large_list:
            st.session_state.sym1="{0}.NS".format(j)
            st.session_state.d1 = pdr.get_data_yahoo(st.session_state.sym1,period="max",interval='1d')
            st.session_state.d1 = st.session_state.d1.reset_index()
            st.write(st.session_state.sym1)        
            st.dataframe(st.session_state.d1)
except Exception as e:
    st.exception(e)
