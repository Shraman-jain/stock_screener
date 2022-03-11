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


mid_list = ['DEVYANI', 'INDIAMART', 'SUNTV', 'AJANTPHARM', 'SUMICHEM', 'L&TFH', 'SUNDRMFAST', 'HAPPSTMNDS', 'PRESTIGE', 'BCG', 'CARBORUNIV', 'NATIONALUM', 'SKFINDIA', 'CENTRALBK', 'M&MFIN', 'SANOFI', 'ALKYLAMINE', 'NUVOCO', 'AIAENG', 'METROPOLIS', 'FEDERALBNK', 'INDIANB', 'GILLETTE', 'PHOENIXLTD', 'APTUS', 'GRINFRA', 'KPITTECH', 'POONAWALLA', 'GSPL', 'RADICO', 'NATCOPHARM', 'CHAMBLFERT', 'WABCOINDIA', 'APLLTD', 'SFL', 'KIOCL', 'CDSL', 'UCOBANK', 'ABSLAMC', 'BSOFT', 'AFFLE', 'BLUEDART', 'TIMKEN', 'DCMSHRIRAM', 'GLENMARK', 'BAJAJELEC', 'WELSPUNIND', 'EXIDEIND', 'MANAPPURAM', 'APOLLOTYRE', 'JBCHEPHARM', 'TTKPRESTIG', 'MOTILALOFS', 'VTL', 'UTIAMC', 'CENTURYPLY', 'BASF', 'NH', 'CAMS', 'MAHABANK', 'FINPIPE', 'ALOKINDS', 'FSL', 'QUESS', 'IIFLWAM', 'SUVENPHAR', 'METROBRAND', 'MEDPLUS', 'KEC', 'CHOLAHLDNG', 'TATAMTRDVR', 'CASTROLIND', 'HINDCOPPER', 'SJVN', 'ZYDUSWELL', 'ZENSARTECH', 'ASAHIINDIA', 'SHRIRAMCIT', 'CESC', 'STLTECH', 'KIMS', 'LXCHEM', 'FINEORG', 'REDINGTON', 'BRIGADE', 'CYIENT', 'ROUTE', 'AMBER', 'GALAXYSURF', 'LATENTVIEW', 'LUXIND', 'BALAMINES', 'ITI', 'BIRLACORPN', 'AMARAJABAT', 'HFCL', 'POWERINDIA', 'IIFL', 'KEI', 'ERIS', 'CENTURYTEX', 'IBULHSGFIN', 'INDIGOPNTS', 'SAREGAMA', 'IDFC', 'JSL', 'INTELLECT', 'CUB', 'GODREJAGRO', 'GRAPHITE', 'ANURAS', 'ANGELONE', 'BLUESTARCO', 'VAIBHAVGBL', 'ALLCARGO', 'VGUARD', 'ELGIEQUIP', 'NETWORK18', 'JUBLPHARMA', 'AKZOINDIA', 'CREDITACC', 'SONATSOFTW', 'POLYMED', 'CGCL', 'LAXMIMACH', 'JUBLINGREA', 'ECLERX', 'RATNAMANI', 'SUZLON', 'MASTEK', 'MAPMYINDIA', 'MAHINDCIE', 'PGHL', 'SHYAMMETL', 'CHEMPLASTS', 'DHANI', 'ASTERDM', 'BSE', 'NLCINDIA', 'FACT', 'MGL', 'TCIEXP', 'SOBHA', 'KNRCON', 'PNBHOUSING', 'GRANULES', 'NBCC', 'JSLHISAR', 'BORORENEW', 'FINCABLES', 'RAIN', 'EIDPARRY', 'IRB', 'ORIENTELEC', 'PVR', 'HUDCO', 'EIHOTEL', 'AEGISCHEM', 'SAPPHIRE', 'ASTRAZEN', 'BBTC', 'PRINCEPIPE', 'GLS', 'BALRAMCHIN', 'AVANTIFEED', 'TV18BRDCST', 'SUNCLAYLTD', 'RBLBANK', 'VIPIND', 'MTARTECH', 'SPARC', 'MRPL', 'NAZARA', 'VMART', 'CANFINHOME', 'RVNL', 'SUNTECK', 'IBREALEST', 'BDL', 'TEAMLEASE', 'GMMPFAUDLR', 'PRIVISCL', 'JMFINANCIL', 'ROSSARI', 'KALYANKJIL', 'SYMPHONY','DELTACORP', 'HGS', 'HEG', 'TATAINVEST', 'GNFC', 'BEML', 'JUSTDIAL', 'EQUITASBNK', 'JKLAKSHMI', 'EDELWEISS', 'HOMEFIRST', 'SIS', 'PNCINFRA', 'MMTC', 'SUPPETRO', 'RTNINDIA', 'GARFIBRES', 'OLECTRA', 'EPL', 'PRSMJOHNSN', 'PSB', 'CAPLIPOINT', 'HIKAL', 'DBL', 'RENUKA', 'RITES', 'SCI', 'CERA', 'PRAJIND', 'SWSOLAR', 'TRITURBINE', 'NIITLTD', 'INDIACEM', 'SUPRAJIT', 'VIJAYA', 'RHIM', 'POLYPLEX', 'TATVA', 'THYROCARE', 'EASEMYTRIP', 'GODFRYPHLP', 'GOCOLORS', 'TCI', 'KRBL', 'CCL', 'MAZDOCK', 'BARBEQUE', 'KALPATPOWR', 'BURGERKING', 'JCHAC','INFIBEAM', 'TRIVENI', 'RALLIS', 'JBMA', 'ESABINDIA', 'GREENPANEL', 'FDC', 'HEIDELBERG', 'VARROC', 'JYOTHYLAB', 'AARTIDRUGS']

if(st.button("Start Screening",key="str_btn")):
    for i in mid_list:
        st.session_state.sym="{0}.NS".format(i)
        st.session_state.d = pdr.get_data_yahoo(st.session_state.sym,period="max",interval='1d')
        st.session_state.d = st.session_state.d.reset_index()
                
        st.dataframe(st.session_state.d)
