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

def get_sma(prices,rate):
  return prices.rolling(rate).mean()

def Boll_band(prices,rate=20):
  sma=get_sma(prices,rate)
  std=prices.rolling(rate).std()
  boll_up = sma + std*2
  boll_dw = sma - std*2  
  return boll_up,boll_dw

def risk_ana(entry_price,stop_loss,strgy="norm"):
    risk=150
    sl=entry_price-stop_loss
    no_of_share=math.ceil(risk/sl)
    if strgy=="norm":
        target1=entry_price+sl
        target2=entry_price+(sl*2)
        target1 = "{:.2f}".format(target1)
        target2 = "{:.2f}".format(target2)
        entry_price="{:.2f}".format(entry_price)
        stop_loss="{:.2f}".format(stop_loss)
        return (risk,entry_price,stop_loss,no_of_share,target1,target2)
    elif strgy=="BB":
        target1 = entry_price+(sl*3)
        target1 = "{:.2f}".format(target1)
        entry_price="{:.2f}".format(entry_price)
        stop_loss="{:.2f}".format(stop_loss)
        return (risk,entry_price,stop_loss,no_of_share,target1)





start = dt.datetime.now()- dt.timedelta(days=100)
end = dt.datetime.now() 

st.title('STOCK SCREENER')

strgy = st.selectbox("STRATEGY LIST",('None','ABC', '44MA', 'BOLLINGER BAND','ATH','15 MIN BUY (ABC)','15 MIN SELL (ABC)','15 MIN BUY (44MA)','15 MIN SELL (44MA)','Trial'))
st.write("selected",strgy)
sc_list = st.selectbox("SCRIPT LIST",('None','Nifty 500', 'Large Cap', 'Mid Cap','Small Cap'))
st.write("selected",sc_list)

#side bar
st.sidebar.write(
    "Risk Analysis Calculator")
r=st.sidebar.text_input('Risk')
ep=st.sidebar.text_input('Entry Price')
stop_l=st.sidebar.text_input('Stop Loss')
try:
  sl=int(ep)-int(stop_l)
  no_of_share=math.ceil(int(r)/sl)
  target1 = int(ep)+sl
  target2 = int(ep)+(sl*2)
  target3 = int(ep)+(sl*3)
except:
  pass
if st.sidebar.button('Calculate'):
  st.sidebar.text("Risk-- "+str(r)+"\n"+"ENTRY PRICE-- "+str(ep)+"\n"+"Stop Loss-- "+str(stop_l)+"\n"+"NO OF SHARES-- "+str(no_of_share)+"\n"+"TARGET 1:01 -- "+str(target1)+"\n"+"TARGET 1:02 -- "+str(target2)+"\n"+"TARGET 1:03 -- "+str(target3))





  
nifty_500=['3MINDIA', 'ABB', 'ACC', 'AIAENG', 'APLAPOLLO', 'AUBANK', 'AARTIDRUGS', 'AARTIIND', 'AAVAS', 'ABBOTINDIA', 'ADANIENT', 'ADANIGREEN', 'ADANIPORTS', 
           'ATGL', 'ADANITRANS', 'ABCAPITAL', 'ABFRL', 'ADVENZYMES', 'AEGISCHEM', 'AFFLE', 'AJANTPHARM', 'ALEMBICLTD', 'APLLTD', 'ALKEM', 'ALKYLAMINE', 'ALOKINDS', 
           'AMARAJABAT', 'AMBER', 'AMBUJACEM', 'ANGELONE', 'ANURAS', 'APOLLOHOSP', 'APOLLOTYRE', 'ASAHIINDIA', 'ASHOKLEY', 'ASHOKA', 'ASIANPAINT', 'ASTERDM', 'ASTRAZEN', 
           'ASTRAL', 'ATUL', 'AUROPHARMA', 'AVANTIFEED', 'DMART', 'AXISBANK', 'BASF', 'BEML', 'BSE', 'BAJAJ-AUTO', 'BAJAJCON', 'BAJAJELEC', 'BAJFINANCE', 'BAJAJFINSV', 
           'BAJAJHLDNG', 'BALAMINES', 'BALKRISIND', 'BALRAMCHIN', 'BANDHANBNK', 'BANKBARODA', 'BANKINDIA', 'MAHABANK', 'BATAINDIA', 'BAYERCROP', 'BERGEPAINT', 'BDL', 'BEL', 
           'BHARATFORG', 'BHEL', 'BPCL', 'BHARATRAS', 'BHARTIARTL', 'BIOCON', 'BIRLACORPN', 'BSOFT', 'BLUEDART', 'BLUESTARCO', 'BBTC', 'BOSCHLTD', 'BRIGADE', 'BRITANNIA', 
           'CCL', 'CESC', 'CGPOWER', 'CRISIL', 'CSBBANK', 'CANFINHOME', 'CANBK', 'CAPLIPOINT', 'CGCL', 'CARBORUNIV', 'CASTROLIND', 'CEATLTD', 'CENTRALBK', 'CDSL', 'CENTURYPLY', 'CENTURYTEX', 'CERA', 'CHALET', 'CHAMBLFERT', 'CHOLAHLDNG', 'CHOLAFIN', 'CIPLA', 'CUB', 'COALINDIA', 'COCHINSHIP', 'COFORGE', 'COLPAL', 'CAMS', 'CONCOR', 'COROMANDEL', 'CREDITACC', 'CROMPTON', 'CUMMINSIND', 'CYIENT', 'DCBBANK', 'DCMSHRIRAM', 'DLF', 'DABUR', 'DALBHARAT', 'DEEPAKNTR', 'DELTACORP', 'DHANI', 'DHANUKA', 'DBL', 'DIVISLAB', 'DIXON', 'LALPATHLAB', 'DRREDDY', 'EIDPARRY', 'EIHOTEL', 'EPL', 'EDELWEISS', 'EICHERMOT', 'ELGIEQUIP', 'EMAMILTD', 'ENDURANCE', 'ENGINERSIN', 'EQUITAS', 'EQUITASBNK', 'ERIS', 'ESCORTS', 'EXIDEIND', 'FDC', 'FEDERALBNK', 'FACT', 'FINEORG', 'FINCABLES', 'FINPIPE', 'FSL', 'FORTIS', 'FRETAIL', 'GAIL', 'GMMPFAUDLR', 'GALAXYSURF', 'GARFIBRES', 'GICRE', 'GILLETTE', 'GLAND', 'GLAXO', 'GLENMARK', 'GODFRYPHLP', 'GODREJAGRO', 'GODREJCP', 'GODREJIND', 'GODREJPROP', 'GRANULES', 'GRAPHITE', 'GRASIM', 'GESHIP', 'GREAVESCOT', 'GRINDWELL', 'GUJALKALI', 'GAEL', 'FLUOROCHEM', 'GUJGASLTD', 'GNFC', 'GPPL', 'GSFC', 'GSPL', 'HEG', 'HCLTECH', 'HDFCAMC', 'HDFCBANK', 'HDFCLIFE', 'HFCL', 'HAPPSTMNDS', 'HATHWAY', 'HATSUN', 'HAVELLS', 'HEIDELBERG', 'HEMIPROP', 'HEROMOTOCO', 'HIKAL', 'HINDALCO', 'HGS', 'HAL', 'HINDCOPPER', 'HINDPETRO', 'HINDUNILVR', 'HINDZINC', 'POWERINDIA', 'HOMEFIRST', 'HONAUT', 'HUDCO', 'HDFC', 'ICICIBANK', 'ICICIGI', 'ICICIPRULI', 'ISEC', 'IDBI', 'IDFCFIRSTB', 'IDFC', 'IFBIND', 'IIFL', 'IIFLWAM', 'IOLCP', 'IRB', 'IRCON', 'ITC', 'ITI', 'INDIACEM', 'IBULHSGFIN', 'IBREALEST', 'INDIAMART', 'INDIANB', 'IEX', 'INDHOTEL', 'IOC', 'IOB', 'IRCTC', 'IRFC', 'INDIGOPNTS', 'ICIL', 'INDOCO', 'IGL', 'INDUSTOWER', 'INDUSINDBK', 'INFIBEAM', 'NAUKRI', 'INFY', 'INGERRAND', 'INOXLEISUR', 'INTELLECT', 'INDIGO', 'IPCALAB', 'JBCHEPHARM', 'JKCEMENT', 'JKLAKSHMI', 'JKPAPER', 'JKTYRE', 'JMFINANCIL', 'JSWENERGY', 'JSWSTEEL', 'JAMNAAUTO', 'JINDALSAW', 'JSLHISAR', 'JSL', 'JINDALSTEL', 'JCHAC', 'JUBLFOOD', 'JUBLINGREA', 'JUBLPHARMA', 'JUSTDIAL', 'JYOTHYLAB', 'KPRMILL', 'KEI', 'KNRCON', 'KPITTECH', 'KRBL', 'KSB', 'KAJARIACER', 'KALPATPOWR', 'KALYANKJIL', 'KANSAINER', 'KARURVYSYA', 'KSCL', 'KEC', 'KOTAKBANK', 'L&TFH', 'LTTS', 'LICHSGFIN', 'LAOPALA', 'LAXMIMACH', 'LTI', 'LT', 'LAURUSLABS', 'LXCHEM', 'LEMONTREE', 'LINDEINDIA', 'LUPIN', 'LUXIND', 'MMTC', 'MOIL', 'MRF', 'LODHA', 'MGL', 'M&MFIN', 'M&M', 'MAHINDCIE', 'MHRIL', 'MAHLOG', 'MANAPPURAM', 'MRPL', 'MARICO', 'MARUTI', 'MASTEK', 'MFSL', 'MAXHEALTH', 'MAZDOCK', 'METROPOLIS', 'MINDTREE', 'MINDACORP', 'MINDAIND', 'MIDHANI', 'MOTILALOFS', 'MPHASIS', 'MCX', 'MUTHOOTFIN', 'NATCOPHARM', 'NBCC', 'NCC', 'NESCO', 'NHPC', 'NLCINDIA', 'NMDC', 'NOCIL', 'NTPC', 'NH', 'NATIONALUM', 'NFL', 'NAVINFLUOR', 'NAZARA', 'NESTLEIND', 'NETWORK18', 'NILKAMAL', 'NAM-INDIA', 'OBEROIRLTY', 'ONGC', 'OIL', 'OFSS', 'ORIENTELEC', 'PCBL', 'PIIND', 'PNBHOUSING', 'PNCINFRA', 'PVR', 'PAGEIND', 'PERSISTENT', 'PETRONET', 'PFIZER', 'PHOENIXLTD', 'PIDILITIND', 'PEL', 'POLYMED', 'POLYCAB', 'POLYPLEX', 'POONAWALLA', 'PFC', 'POWERGRID', 'PRAJIND', 'PRESTIGE', 'PRINCEPIPE', 'PRSMJOHNSN', 'PGHL', 'PGHH', 'PNB', 'QUESS', 'RBLBANK', 'RECLTD', 'RHIM', 'RITES', 'RADICO', 'RVNL', 'RAILTEL', 'RAIN', 'RAJESHEXPO', 
           'RALLIS', 'RCF', 'RATNAMANI', 'REDINGTON', 'RELAXO', 'RELIANCE', 'RBA', 'ROSSARI', 'ROUTE', 'SBICARD', 'SBILIFE', 'SIS', 
           'SJVN', 'SKFINDIA', 'SRF', 'SANOFI', 'SCHAEFFLER', 'SCHNEIDER', 'SEQUENT', 'SHARDACROP', 'SFL', 'SHILPAMED', 'SCI', 'SHREECEM', 'SHRIRAMCIT', 'SRTRANSFIN', 'SIEMENS', 'SOBHA', 'SOLARINDS', 'SOLARA', 'SONACOMS', 'SONATSOFTW', 'SPANDANA', 'SPICEJET', 'STARCEMENT', 'SBIN', 'SAIL', 'SWSOLAR', 'STLTECH', 'STAR', 'SUDARSCHEM', 'SUMICHEM', 'SPARC', 'SUNPHARMA', 'SUNTV', 'SUNDARMFIN', 'SUNDRMFAST', 'SUNTECK', 'SUPRAJIT', 'SUPREMEIND', 'SUPPETRO', 'SUVENPHAR', 'SUZLON', 'SYMPHONY', 'SYNGENE', 'TCIEXP', 'TCNSBRANDS', 'TTKPRESTIG', 'TV18BRDCST', 'TVSMOTOR', 'TANLA', 'TASTYBITE', 'TATACHEM', 'TATACOFFEE', 'TATACOMM', 'TCS', 'TATACONSUM', 'TATAELXSI', 'TATAMTRDVR', 'TATAMOTORS', 'TATAPOWER', 'TATASTLLP', 'TATASTEEL', 'TTML', 'TEAMLEASE', 'TECHM', 'NIACL', 'RAMCOCEM', 'THERMAX', 'THYROCARE', 'TIMKEN', 'TITAN', 'TORNTPHARM', 'TORNTPOWER', 'TRENT', 'TRIDENT', 'TRITURBINE', 'TIINDIA', 'UCOBANK', 'UFLEX', 'UPL', 'UTIAMC', 'UJJIVAN', 'UJJIVANSFB', 'ULTRACEMCO', 'UNIONBANK', 'UBL', 'MCDOWELL-N', 'VGUARD', 'VMART', 'VIPIND', 'VAIBHAVGBL', 'VAKRANGEE', 'VALIANTORG', 'VTL', 'VARROC', 'VBL', 'VEDL', 'VENKEYS', 'VINATIORGA', 'IDEA', 'VOLTAS', 'WABCOINDIA', 'WELCORP', 'WELSPUNIND', 'WESTLIFE', 'WHIRLPOOL', 'WIPRO', 'WOCKPHARMA', 'YESBANK', 'ZEEL', 'ZENSARTECH', 'ZYDUSLIFE', 'ZYDUSWELL', 'ECLERX']


large_list = ['RELIANCE', 'TCS', 'HDFCBANK', 'INFY', 'HINDUNILVR', 'ICICIBANK', 'HDFC', 'BAJFINANCE', 'SBIN', 'WIPRO', 'BHARTIARTL', 'HCLTECH', 'KOTAKBANK', 'ASIANPAINT', 'DMART', 'ITC', 'LT', 'BAJAJFINSV', 'MARUTI', 'TITAN', 'ULTRACEMCO', 'AXISBANK', 'ADANIGREEN', 'SUNPHARMA', 'ADANITRANS', 'ATGL', 'ADANIENT', 'ONGC', 'TECHM', 'TATAMOTORS', 'JSWSTEEL', 'ADANIPORTS', 'POWERGRID', 'TATASTEEL', 'HINDZINC', 'HDFCLIFE', 'LTI', 'VEDL', 'PIDILITIND', 'DIVISLAB', 'NTPC', 'SBILIFE', 'ZOMATO', 'HINDALCO', 'GRASIM', 'IOC', 'M&M', 'DABUR', 'NYKAA', 'GODREJCP', 'SHREECEM', 'DLF', 'BAJAJ-AUTO', 'COALINDIA', 'SBICARD', 'HAVELLS', 'BRITANNIA', 'PAYTM', 'SIEMENS', 'BPCL', 'DRREDDY', 'ICICIPRULI', 'MINDTREE', 'INDIGO', 'CIPLA', 'BERGEPAINT', 'AMBUJACEM', 'APOLLOHOSP', 'NAUKRI', 'SRF', 'EICHERMOT', 'TATAPOWER', 'MOTHERSUMI', 'INDUSINDBK', 'ICICIGI', 'TATACONSUM', 'INDUSTOWER', 'IRCTC', 'MARICO', 'MCDOWELL-N', 'MPHASIS', 'GLAND', 'PEL', 'BAJAJHLDNG', 'MUTHOOTFIN', 'LODHA', 'LTTS', 'GAIL', 'UPL', 'TORNTPHARM', 'HDFCAMC', 'GODREJPROP', 'BEL', 'BOSCHLTD', 'PGHH', 'IDBI', 'CADILAHC', 'JSWENERGY', 'HEROMOTOCO', 'JUBLFOOD', 'ABB', 'PIIND', 'ASTRAL', 'STARHEALTH', 'PAGEIND', 'BALKRISIND', 'SAIL', 'IDEA', 'BIOCON', 'GUJGASLTD', 'SONACOMS', 'ALKEM', 'LUPIN', 'AUROPHARMA', 'MAXHEALTH', 'CHOLAFIN', 'POLICYBZR', 'BANKBARODA', 'UBL', 'TATACOMM', 'ACC', 'HINDPETRO', 'PNB', 'BANDHANBNK', 'HAL', 'TTML', 'VOLTAS', 'COLPAL', 'NMDC', 'JINDALSTEL', 'IOB', 'VBL', 'ADANIPOWER', 'TRENT', 'PERSISTENT', 'CONCOR', 'HONAUT', 'POLYCAB', 'TATAELXSI', 'AARTIIND', 'CANBK', 'ASHOKLEY', 'COFORGE', 'MINDAIND', 'DALBHARAT', 'YESBANK', 'OFSS', 'DEEPAKNTR', 'TIINDIA', 'MFSL', 'IGL', 'SRTRANSFIN', 'DIXON', 'RELAXO', 'AUBANK', 'BHARATFORG', 'PETRONET', 'KANSAINER', 'LALPATHLAB', 'PFC', 'OBEROIRLTY', 'MRF', 'NHPC', 'ZEEL', 'IDFCFIRSTB', 'ABCAPITAL', 'IRFC', 'TVSMOTOR', 'GLAXO', 'UNIONBANK', 'LAURUSLABS', '3MINDIA', 'SUPREMEIND', 'GMRINFRA', 'IPCALAB', 'CROMPTON', 'SCHAEFFLER', 'HATSUN', 'TRIDENT', 'ATUL', 'TORNTPOWER', 'FLUOROCHEM', 'CLEAN', 'RECLTD', 'CGPOWER', 'JKCEMENT', 'CUMMINSIND', 'ESCORTS', 'TANLA', 'ISEC', 'ABFRL', 'SUNDARMFIN', 'RUCHI', 'APLAPOLLO', 'SYNGENE', 'GICRE', 'BATAINDIA', 'INDHOTEL', 'ENDURANCE', 'RAMCOCEM', 'PFIZER', 'NIACL', 'EMAMILTD', 'KPRMILL', 'TATACHEM', 'IEX', 'FORTIS', 'WHIRLPOOL', 'COROMANDEL', 'SOLARINDS', 'NAM-INDIA', 'RAJESHEXPO', 'OIL', 'THERMAX', 'GRINDWELL', 'LINDEINDIA', 'GODREJIND', 'BANKINDIA', 'CRISIL', 'NAVINFLUOR', 'AAVAS', 'KAJARIACER', 'BHEL', 'VINATIORGA', 'LICHSGFIN']

mid_list = ['DEVYANI', 'INDIAMART', 'SUNTV', 'AJANTPHARM', 'SUMICHEM', 'L&TFH', 'SUNDRMFAST', 'HAPPSTMNDS', 'PRESTIGE', 'BCG', 'CARBORUNIV', 'NATIONALUM', 'SKFINDIA', 'CENTRALBK', 'M&MFIN', 'SANOFI', 'ALKYLAMINE', 'NUVOCO', 'AIAENG', 'METROPOLIS', 'FEDERALBNK', 'INDIANB', 'GILLETTE', 'PHOENIXLTD', 'APTUS', 'GRINFRA', 'KPITTECH', 'POONAWALLA', 'GSPL', 'RADICO', 'NATCOPHARM', 'CHAMBLFERT', 'WABCOINDIA', 'APLLTD', 'SFL', 'KIOCL', 'CDSL', 'UCOBANK', 'ABSLAMC', 'BSOFT', 'AFFLE', 'BLUEDART', 'TIMKEN', 'DCMSHRIRAM', 'GLENMARK', 'BAJAJELEC', 'WELSPUNIND', 'EXIDEIND', 'MANAPPURAM', 'APOLLOTYRE', 'JBCHEPHARM', 'TTKPRESTIG', 'MOTILALOFS', 'VTL', 'UTIAMC', 'CENTURYPLY', 'BASF', 'NH', 'CAMS', 'MAHABANK', 'FINPIPE', 'ALOKINDS', 'FSL', 'QUESS', 'IIFLWAM', 'SUVENPHAR', 'METROBRAND', 'MEDPLUS', 'KEC', 'CHOLAHLDNG', 'TATAMTRDVR', 'CASTROLIND', 'HINDCOPPER', 'SJVN', 'ZYDUSWELL', 'ZENSARTECH', 'ASAHIINDIA', 'SHRIRAMCIT', 'CESC', 'STLTECH', 'KIMS', 'LXCHEM', 'FINEORG', 'REDINGTON', 'BRIGADE', 'CYIENT', 'ROUTE', 'AMBER', 'GALAXYSURF', 'LATENTVIEW', 'LUXIND', 'BALAMINES', 'ITI', 'BIRLACORPN', 'AMARAJABAT', 'HFCL', 'POWERINDIA', 'IIFL', 'KEI', 'ERIS', 'CENTURYTEX', 'IBULHSGFIN', 'INDIGOPNTS', 'SAREGAMA', 'IDFC', 'JSL', 'INTELLECT', 'CUB', 'GODREJAGRO', 'GRAPHITE', 'ANURAS', 'ANGELONE', 'BLUESTARCO', 'VAIBHAVGBL', 'ALLCARGO', 'VGUARD', 'ELGIEQUIP', 'NETWORK18', 'JUBLPHARMA', 'AKZOINDIA', 'CREDITACC', 'SONATSOFTW', 'POLYMED', 'CGCL', 'LAXMIMACH', 'JUBLINGREA', 'ECLERX', 'RATNAMANI', 'SUZLON', 'MASTEK', 'MAPMYINDIA', 'MAHINDCIE', 'PGHL', 'SHYAMMETL', 'CHEMPLASTS', 'DHANI', 'ASTERDM', 'BSE', 'NLCINDIA', 'FACT', 'MGL', 'TCIEXP', 'SOBHA', 'KNRCON', 'PNBHOUSING', 'GRANULES', 'NBCC', 'JSLHISAR', 'BORORENEW', 'FINCABLES', 'RAIN', 'EIDPARRY', 'IRB', 'ORIENTELEC', 'PVR', 'HUDCO', 'EIHOTEL', 'AEGISCHEM', 'SAPPHIRE', 'ASTRAZEN', 'BBTC', 'PRINCEPIPE', 'GLS', 'BALRAMCHIN', 'AVANTIFEED', 'TV18BRDCST', 'SUNCLAYLTD', 'RBLBANK', 'VIPIND', 'MTARTECH', 'SPARC', 'MRPL', 'NAZARA', 'VMART', 'CANFINHOME', 'RVNL', 'SUNTECK', 'IBREALEST', 'BDL', 'TEAMLEASE', 'GMMPFAUDLR', 'PRIVISCL', 'JMFINANCIL', 'ROSSARI', 'KALYANKJIL', 'SYMPHONY', 'DELTACORP', 'HGS', 'HEG', 'TATAINVEST', 'GNFC', 'BEML', 'JUSTDIAL', 'EQUITASBNK', 'JKLAKSHMI', 'EDELWEISS', 'HOMEFIRST', 'SIS', 'PNCINFRA', 'MMTC', 'SUPPETRO', 'RTNINDIA', 'GARFIBRES', 'OLECTRA', 'EPL', 'PRSMJOHNSN', 'PSB', 'CAPLIPOINT', 'HIKAL', 'DBL', 'RENUKA', 'RITES', 'SCI', 'CERA', 'PRAJIND', 'SWSOLAR', 'TRITURBINE', 'NIITLTD', 'INDIACEM', 'SUPRAJIT', 'VIJAYA', 'RHIM', 'POLYPLEX', 'TATVA', 'THYROCARE', 'EASEMYTRIP', 'GODFRYPHLP', 'GOCOLORS', 'TCI', 'KRBL', 'CCL', 'MAZDOCK', 'BARBEQUE', 'KALPATPOWR', 'BURGERKING', 'JCHAC', 'INFIBEAM', 'TRIVENI', 'RALLIS', 'JBMA', 'ESABINDIA', 'GREENPANEL', 'FDC', 'HEIDELBERG', 'VARROC', 'JYOTHYLAB', 'AARTIDRUGS']

small_list = ['ICIL', 'CEATLTD', 'VSTIND', 'MAHLOG', 'GSFC', 'BHARATRAS', 'GPPL', 'BOROLTD', 'TCNSBRANDS', 'CRAFTSMAN', 'TEJASNET', 'GUJALKALI', 'LAOPALA', 'COCHINSHIP', 'JINDWORLD', 'VAKRANGEE', 'WELCORP', 'SHILPAMED', 'RPOWER', 'JSWHL', 'PHILIPCARB', 'WOCKPHARMA', 'IFBIND', 'JINDALPOLY', 'RESPONIND', 'DEEPAKFERT', 'ISGEC', 'CHALET', 'GESHIP', 'PDSMFL', 'MAHSCOOTER', 'INOXLEISUR', 'GREENLAM', 'NCC', 'JPPOWER', 'KSB', 'IRCON', 'RCF', 'RELIGARE', 'INDOCO', 'RAYMOND', 'NEWGEN', 'JAMNAAUTO', 'NESCO', 'CSBBANK', 'SANSERA', 'MINDACORP', 'STAR', 'MOIL', 'SEQUENT', 'TATACOFFEE', 'RATEGAIN', 'RTNPOWER', 'CARTRADE', 'DATAPATTNS', 'ENGINERSIN', 'TEGA', 'STARCEMENT', 'GPIL', 'SUPRIYA', 'AMIORG', 'DHANUKA', 'RSYSTEMS', 'GAEL', 
             'HATHWAY', 'NOCIL', 'SUDARSCHEM', 'NEOGEN', 'EQUITAS', 'VRLLOG', 'MANINFRA', 'MHRIL', 'VENKEYS', 'RAILTEL', 'MAHLIFE', 'HGINFRA', 'UFLEX', 'INGERRAND', 'GLOBUSSPR', 'LEMONTREE', 'SOLARA', 'ADVENZYMES', 'HEMIPROP', 'KARURVYSYA', 'NILKAMAL', 'SHOPERSTOP', 'IPL', 'KSCL', 'SOMANYCERA', 'GHCL', 'ARVINDFASN', 'SWANENERGY', 'TASTYBITE', 'TATASTLLP', 'CMSINFO', 'RUPA', 'JKPAPER', 'GDL', 'MASFIN', 'TARSONS', 'JKTYRE', 'GET&D', 'MAHSEAMLES', 'DISHTV', 'MIDHANI', 'J&KBANK', 'HIL', 'BANARISUG', 'SHAREINDIA', 'IFCI', 'PURVA', 'ICRA', 'DODLA', 'ORIENTCEM', 'PTC', 'UJJIVANSFB', 'SHARDACROP', 'GREAVESCOT', 'STOVEKRAFT', 'SURYAROSNI', 'SAGCEM', 'ROLEXRINGS', 'JINDALSAW', 'DCAL', 'ARVIND', 'MFL', 'DALMIASUG', 'FINOPB', 'PAISALO', 'SHIL', 'SUBEXLTD', 'RKFORGE', 'HCG', 'APARINDS', 'INDOSTAR', 'SPANDANA', 'GTPL', 'MAITHANALL', 'BAJAJCON', 'ITDC', 'SARDAEN', 'PARAS', 'TINPLATE', 'SEAMECLTD', 'IOLCP', 'VALIANTORG', 'ASHOKA', 'INDIAGLYCO', 'MOL', 'ASTEC', 'BEPL', 'IIFLSEC', 'FRETAIL', 'USHAMART', 'AMRUTANJAN', 'ALEMBICLTD', 'OPTIEMUS', 'HERANBA', 'AHLUCONT', 'EKC', 'SSWL', 'BBOX', 'KIRLOSENG', 'KIRLOSBROS', 'GTLINFRA', 'TATAMETALI', 'ACE', 'TECHNOE', 'SHARDAMOTR', 'OAL', 'TIDEWATER', 'NFL', 'INOXWIND', 'GRSE', 'COSMOFILMS', 'TVTODAY', 'SCHNEIDER', 'MOREPENLAB', 'GREENPLY', 'RELINFRA', 'HCC', 'HIMATSEIDE', 'MARKSANS', 'IMFA', 'SUBROS', 'MAYURUNIQ', 'ANANDRATHI', 'JPASSOCIAT', 'DCBBANK', 'MOLDTKPAC', 'TIRUMALCHM', 'INEOSSTYRO', 'HINDOILEXP', 'ATFL', 'DAAWAT', 'TIPSINDLTD', 'VSTTILLERS', 'DOLLAR', 'AUTOAXLES', 'JAYNECOIND', 'GMDCLTD', 'MSTCLTD', 'KRSNAA', 'GATI', 'GUFICBIO', 'KOLTEPATIL', 'ANANTRAJ', 'GULFOILLUB', 'JTEKTINDIA', 'BOMDYEING', 'THOMASCOOK', 'MTNL', 'BECTORFOOD', 'CONFIPET', 'VESUVIUS', 'JAICORPLTD', 'POKARNA', 'ACRYSIL', 'SHK', 'FAIRCHEMOR', 'FILATEX', 'RAMCOIND', 'HESTERBIO', 'IGPL', 'EVEREADY', 'MATRIMONY', 'APOLLOPIPE', 'PFOCUS', 'BALMLAWRIE', 'ELECON', 'JISLJALEQS', 'BUTTERFLY', 'PILANIINVS', 'LGBBROSLTD', 'DHAMPURSUG', 'RAJRATAN', 'SIYSIL', 'ASTRAMICRO', 'NAVNETEDUL', 'GRAVITA', 'VOLTAMP', 'DEN', 'NURECA', 'GABRIEL', 'SAFARI', 'SASKEN', 'NEULANDLAB', 'DIAMONDYD', 'VIDHIING', 'SWARAJENG', 'KIRIINDUS', 'BLS', 'BAJAJHIND', 'WABAG', 'KTKBANK', 'GOKEX', 'TIIL', 'RPSGVENT', 'MAXVIL', 'HERITGFOOD', 'HSCL', 'THANGAMAYL', 'SHRIPISTON', 'MANALIPETC', 'APCOTEXIND', 'SOUTHBANK', 'NACLIND', 'GOLDIAM', 'KINGFA', 'ANDHRSUGAR', 'CARERATING', 'RGL', 'DATAMATICS', 'NAHARSPING', 'GEOJITFSL', 'STYLAMIND', 'PUNJABCHEM', 'KCP', 'MUKANDLTD', 'GENUSPOWER', 'LSIL', 'EXPLEOSOL', 'ASHIANA', 'UNICHEMLAB', 'MMFL', 'PSPPROJECT', 'HBLPOWER', 'SUNDARMHLD', 'HUHTAMAKI', 'TIMETECHNO', 'ZENTEC', 'GEPIL', 'APTECHT', 'PGEL', 'REPCOHOME', 'CAMLINFINE', 'DPSCLTD', 'NELCO', 'DBCORP', 'JAGRAN', 'JSWISPL', 'NUCLEUS', 'ADFFOODS', 'ORCHPHARMA', 'UJJIVAN', 'NBVENTURES', 
             'ACCELYA', 'ELECTCAST', '3IINFOLTD', 'GNA', 'WSTCSTPAPR', 'NRBBEARING', 'SURYODAY', 'SASTASUNDR', 'JMCPROJECT', 'STEELXIND', 'FCL', 'SOTL', 'INDORAMA', 'PATELENG', 'CHENNPETRO', 'SHALBY', 'IGARASHI', 'SANDHAR', 'SHIVALIK', 'CIGNITITEC', 'GOCLCORP', 'TVSSRICHAK', 'MIRZAINT', 'SANGAMIND', 'KABRAEXTRU', 'PANAMAPET', 'FCONSUMER', 'WHEELS', 'GMBREW', 'FIEMIND', 'DFMFOODS', 'TARC', 'SIRCA', 'KIRLOSIND', 'NITINSPIN', 'SHRIRAMPPS', 'GREENPOWER', 'DYNAMATECH', 'RAMCOSYS', 'BFUTILITIE', 'SBCL', 'KKCL', 'QUICKHEAL', 'GALLISPAT', 'WELENT', 'SANGHIIND', 'KOPRAN', 'INSECTICID', 'TDPOWERSYS', 'KSL', 'OMAXE', 'ITDCEM', 'UGROCAP', 'POWERMECH', 'ORISSAMINE', 'PRECAM', 'BODALCHEM', 'HSIL', 'PRICOLLTD', 'HMT', 'CHEMCON', 'DWARKESH', 'RAMKY', 'SUTLEJTEX', 'CENTRUM', 'VINDHYATEL', 'HONDAPOWER', 'CANTABIL', 'ALICON', 'TI', 'RIIL', 'KITEX', 'GULPOLY', 'PFS', 'NXTDIGITAL', 'PCJEWELLER', 'SUNFLAG', 'GIPCL', 'MONTECARLO', 'BANCOINDIA', 'SIGACHI', 'THEJO', 'JKIL', 'XCHANGING', 'PANACEABIO', 'SHANKARA', 'BFINVEST', 'PNBGILTS', 'FMGOETZE', '5PAISA', 'AVTNPL', 'CAPACITE', 'KDDL', 'SHAKTIPUMP', 'WONDERLA', 'SJS', 'DCW', 'BAJAJHCARE', 'JUBLINDS', 'CLNINDIA', 'IFGLEXPOR', 'SHANTIGEAR', 'MPSLTD', 'SUVEN', 'DBREALTY', 'SPIC', 'JYOTISTRUC', 'EXCELINDUS', 'GANECOS', 'SPAL', 'LUMAXIND', 'TWL', 'SINTEX', 'AMBIKCO', 'XPROINDIA', 'DIGISPICE', 'EQUIPPP', 'SMSPHARMA', 'BBL', 'MEDICAMEQ', 'RSWM', 'KBCGLOBAL', 'GANESHHOUC', 'BHAGERIA', 'ONMOBILE', 'RCOM', 'BLISSGVS', 'TEXRAIL', 'SHRIRAMEPC', 'ESTER', 'PARAGMILK', 'LUMAXTECH', 'URJA', '63MOONS', 'EIHAHOTELS', 'VISHNU', 'ASAL', 'SAKSOFT', 'SHREDIGCEM', 'MANGLMCEM', 'VSSL', 'FLFL', 'VISAKAIND', 'RPGLIFE', 'SANGHVIMOV', 'JETAIRWAYS', 'IMPAL', 'PARSVNATH', 'WENDT', 'KESORAMIND', 'INFOBEAN', 'ANUP', 'TTKHLTCARE', 'AJMERA', 'TNPETRO', 'ZOTA', 'CENTENKA', 'PRAKASH', 'OCCL', 'ALLSEC', 'CEREBRAINT', 'DPABHUSHAN', 'NCLIND', 'ADORWELD', 'SVPGLOB', 'VHL', 'ISMTLTD', 'SRIPIPES', 'INDIANHUME', 'SESHAPAPER', 'UNIDT', 'GOODLUCK', 'APEX', 'UNITECH', 'AWHCL', 'SMLISUZU', 'ASALCBR', 'ARVSMART', 'AVADHSUGAR', 'UNIENTER', 'FOSECOIND', 'GENESYS', 'VIMTALABS', 'ASHAPURMIN', 'COFFEEDAY', 'GOKULAGRO', 'SPENCERS', 'MANORG', 'RANEHOLDIN', 'TEXINFRA', 'DREDGECORP', 'SATIA', 'SPTL', 'THEMISMED', 'ANDHRAPAP', 'SMCGLOBAL', 'ARSHIYA', 'EVERESTIND', 'MANGCHEFER', 'TNPL', 'IWEL', 'ZEEMEDIA', 'PRECWIRE', 'RADIOCITY', 'DHARAMSI', 'FCSSOFT', 'INDNIPPON', 'DECCANCE', 'BINDALAGRO', 'ENIL', 'EMAMIPAP', 'BHAGCHEM', 'DVL', 'SKIPPER', 'YAARI', 'GICHSGFIN', 'AARTISURF', 'TAJGVK', 'NSIL', 'GFLLIMITED', 'ASIANTILES', 'SUULD', 'KICL', 'APCL', 'CENTUM', 'BCLIND', 'JAYBARMARU', 'DCMSRIND', 'UNIVPHOTO', 'PGIL', 'RUSHIL', 'PITTIENG', 'ADSL', 'VLSFINANCE', 'NDTV', 'HCL-INSYS', 'HEXATRADEX', 'ARMANFIN', 'HPAL', 'TAKE', 'NAGAFERT', 'LINCOLN', 'SUMMITSEC', 'YUKEN', 
             'ARIHANTSUP', 'NELCAST', 'DYNPRO', 'KANORICHEM', 'INDRAMEDCO', 'ORIENTHOT', 'NAHARPOLY', 'UTTAMSUGAR', 'KUANTUM', 'SALASAR', 'LIKHITHA', 'SNOWMAN', 'AURIONPRO', 'ORIENTPPR', 'REPRO', 'HLVLTD', 'BLKASHYAP', 'VADILALIND', 'SHREEPUSHK', 'SADBHAV', 'STERTOOLS', 'MIRCELECTR', 'EXXARO', 'KRITI', 'ONWARDTEC', 'HTMEDIA', 'SATIN', 'NAVKARCORP', 'LYKALABS', 'RBL', 'DELPHIFX', 'DLINKINDIA', 'STCINDIA', 'JAIBALAJI', 'JAYAGROGN', 'HITECH', 'SHALPAINTS', 'ORICONENT', 'BALAJITELE', 'GANESHBE', 'CYBERTECH', 'KOKUYOCMLN', 'KHAICHEM', 'BGRENERGY', 'MSPL', 'BETA', 'VASCONEQ', 'NAHARCAP', 'KELLTONTEC', 'WINDLAS', 'NECLIFE', 'STEELCAS', 'PLASTIBLEN', 'GALLANTT', 'IFBAGRO', 'RICOAUTO', 'RML', 'KAMDHENU', 'MUTHOOTCAP', 'KPIGLOBAL', 'XELPMOC', 'NDL', 'WEBELSOLAR', 'MANINDS', 'MEGASOFT', 'RAMASTEEL', 'SRHHYPOLTD', 'SANDESH', 'NBIFIN', 'KAYA', 'V2RETAIL', 'PROZONINTU', 'UNIVCABLES', 'GAYAPROJ', 'CONTROLPR', 'ARTEMISMED', 'MINDTECK', 'VENUSREM', 'CREATIVE', 'TFCILTD', 'SARLAPOLY', 'OSWALAGRO', 'HMVL', 'SADBHIN', 'VISHWARAJ', 'TBZ', 'MUNJALAU', 'BASML', 'AGARIND', 'DCMNVL', 'ROSSELLIND', 'ASIANENE', 'SHREYAS', 'HITECHCORP', 'THEINVEST', 'JASH', 'BALAXI', 'MANAKSIA', 'PENIND', 'MARATHON', 'TRIGYN', 'ZUARI', 'NATHBIOGEN', 'CLSEL', 'DEEPINDS', 'ZEELEARN', 'ORIENTBELL', 'KRISHANA', 'AYMSYNTEX', 'MARINE', 'CONSOFINVT', 'MUNJALSHOW', 'HUBTOWN', 'INTLCONV', 'NAHARINDUS', 'TALBROAUTO', 'GANDHITUBE', 'HINDCOMPOS', 'ANDHRACEMT', 'KHADIM', 'JAGSNPHARM', 'TCPLPACK', 'TRIL', 'HITECHGEAR', 'MADRASFERT', 'JPINFRATEC', 'ROHITFERRO', 'MENONBE', 'HPL', 'SECURKLOUD', 'HERCULES', 'AURUM', 'FOODSIN', 'NRAIL', 'FEL', 'SWELECTES', 'CREST', 'RUBYMILLS', 'KREBSBIO', 'VINYLINDIA', 'PENINLAND', 'MARALOVER', 'VARDHACRLC', 'SPECIALITY', 'GINNIFILA', 'PASUPTAC', 'ATULAUTO', 'BIGBLOC', 'SREEL', 'GOKUL', 'PTL', 'KSOLVES', 'ARIHANTCAP', 'BIL', 'ZUARIGLOB', 'AXISCADES', 'SITINET', 'MAXIND', 'INDSWFTLAB', 'SOUTHWEST', 'REPL', 'GTL', 'BANSWRAS', 'SHIVAMAUTO', 'HIRECT', 'CEBBCO', 'KILITCH', 'MEP', 'SHYAMCENT', 'LGBFORGE', 'SCHAND', 'MBAPL', 'JINDRILL', 'DHUNINV', 'RANASUG', 'MMP', 'DUCON', 'KOTHARIPET', 'VIKASLIFE', 'GKWLIMITED', 'GSCLCEMENT', 'DHANBANK', 'AKSHARCHEM', 'BHARATWIRE', 'BPL', 'NIPPOBATRY', 'EIFFL', 'RELCAPITAL', 'DICIND', 'BAFNAPH', 'ASHIMASYN', 'INDOWIND', 'ORIENTABRA', 'RNAVAL', 'EMAMIREAL', 'MAGADSUGAR', 'LINC', 'ASAHISONG', 'GOACARBON', 'BIRLAMONEY', 'INDOTHAI', 'ADVANIHOTR', 'UFO', 'NGIL', 'PRIMESECU', 'BIRLATYRE', 
             'OMINFRAL', 'PDMJEPAPER', 'BBTCL', 'ALBERTDAVD', 'SHEMAROO', 'APOLLO', 'COASTCORP', 'DONEAR', 'ARTNIRMAN', 'UGARSUGAR', 'BSHSL', 'BALLARPUR', 'MBLINFRA', 'JITFINFRA', 'GOLDTECH', 'PRECOT', 'MAHEPC', 'TVSELECT', 'IRISDOREME', 'ISFT', 'CLEDUCATE', 'DPWIRES', 'SORILINFRA', 'UCALFUEL', 'IVC', 'ALMONDZ', 'BIRLACABLE', 'RAJMET', 'PPL', 'GEECEE', 'PRAXIS', 'SILINV', 'MAWANASUG', 'MGEL', 'ACCURACY', 'FSC', 'PPAP', 'SAKUMA', 'HINDNATGLS', 'SALZERELEC', 'SHIVATEX', 'GENUSPAPER', 'KCPSUGIND', 'AKASH', 'RAMANEWS', 'REFEX', 'PODDARMENT', 'CUPID',
             'RPPL', 'VIPULLTD', 'INSPIRISYS', 'INVENTURE', 'AIRAN', 'KOTHARIPRO', 'HARRMALAYA', 'TEMBO', 'WEALTH', 'ABAN', 'CINELINE', 'STEL', 'JAYSREETEA', 'CHEMBOND', 'INNOVANA', 'JPOLYINVST', 'SREINFRA', 'NILAINFRA', 'SDBL', 'LASA', 'MANAKCOAT', 'SAKAR', 'MCLEODRUSS', 'IRIS', 'ESSARSHPNG', 'KOTARISUG', 'KANPRPLA', 'MAHESHWARI', 'WANBURY', 'DTIL', 'MODISNME', 'ZODIACLOTH', 'PARACABLES', 'BRFL', 'VISESHINFO', 'INDOSOLAR', 'LIBERTSHOE', 'HDIL', 'JINDALPHOT', 'EMKAY', 'TPLPLASTEH', 'AHLWEST', 'RHFL', 'PREMEXPLN', 'LOVABLE', 'EMKAYTOOLS', 'INDTERRAIN', 'BRNL', 'SUVIDHAA', 'WINDMACHIN', 'KMSUGAR', 'SIMPLEXINF', 'BROOKS', 'PAR', 'DCM', 'DENORA', 'SETCO', 'MAZDA', 'HINDMOTORS', 'INDOTECH', 'AAKASH', 'PIONDIST', 'MOLDTECH', 'MOKSH', 'CAREERP', 'GUJAPOLLO', 'GPTINFRA', 'SGIL', 'GULFPETRO', 'PANSARI', 'NDRAUTO', 'ASTRON', 'SMARTLINK', 'ALPHAGEO', 'ROHLTD', 'ALANKIT', 'SHRENIK', 'AJRINFRA', 'GLOBE', 'GIRRESORTS', 'GOLDENTOBC', '20MICRONS', 'PALREDTEC', 'GANGAFORGE', 'COMPUSOFT', 'NITCO', 'SMSLIFE', 'SINTERCOM', 'SIGMA', 'CHEMFAB', 'NRL', 'APOLSINHOT', 'AUTOIND', 'AHLEAST', 'REVATHI', 'AKSHOPTFBR', 'ANKITMETAL', 'RAJTV', 'MANAKSTEEL', 'BEDMUTHA', 'PILITA', 'ONEPOINT', 'MANGALAM', 'RUCHINFRA', 'DANGEE', 'WALCHANNAG', 'RVHL', 'TEXMOPIPES', 'MANAKALUCO', 'GSS', 'INTENTECH', 'TTL', 'SELAN', 'STARPAPER', 'VETO', 'MACPOWER', 'SUNDARAM', 'PREMIERPOL', 'SKMEGGPROD', 'EIMCOELECO', 'COMPINFO', 'RUCHIRA', 'VIPCLOTHNG', 'ORBTEXP', 'ANSALAPI', 'PVP', 'ELGIRUBCO', 'MODIRUBBER', 'ARIES', 'RANEENGINE', 'ANMOL', 'SILVERTUC', 'VIKASECO', 'DSSL', 'KANANIIND', 'CAPTRUST', 'PONNIERODE', 'NILASPACES', 'ENERGYDEV', 'VISASTEEL', 'SUPERHOUSE', 'EMMBI', 'EROSMEDIA', 'SAKHTISUG', 'VIVIMEDLAB', 'IL&FSTRANS', 'MCDHOLDING', 'IITL', 'JHS', 'ELECTHERM', 'PRITIKAUTO', 'SEPOWER', 'ARROWGREEN', 'JOCIL', 'EUROBOND', 'AHLADA', 'JBFIND', 'PIONEEREMB', 'KAKATCEM', 'INDIANCARD', 'A2ZINFRA', 'ALPA', 'PRAENG', 'UNITEDTEA', 'BHAGYANGR', 'RKEC', 'CTE', 'GENCON', 'CORALFINAC', 'SMLT', 'MAANALU', 'JMA', 'SBC', 'LPDC', 'BALPHARMA', 'DRCSYSTEMS', 'UMANGDAIRY', 'RPPINFRA', 'NOIDATOLL', 'BHANDARI', 'KERNEX', 'MURUDCERA', '3RDROCK', 'SEYAIND', 'ATLANTA', 'JMTAUTOLTD', 'KECL', 'TRF', 'BHARATGEAR', 'CCHHL', 'WORTH', 'SUNDRMBRAK', 'SURANASOL', 'LOKESHMACH', 'SURANAT&P', 'DEEPENR', 'OSIAHYPER', 'WFL', 'AARVI', 'TIL', 'SERVOTECH', 'ASIANHOTNR', 'KOTYARK', 'SPLIL', 'SHREYANIND', 'AMJLAND', 'GRPLTD', 'DAMODARIND', 'ROLTA', 'MAHAPEXLTD', 'GILLANDERS', 'SIGIND', 'NDGL', 'PUNJLLOYD', 'SHIVAMILLS', 'REMSONSIND', 'PENTAGOLD', 'PASHUPATI', 'NIRAJ', 'PAVNAIND', 'KAPSTON', 'MBECL', 'SAMBHAAV', 'SURYALAXMI', 'TOTAL', 'SALONA', 'IVP', 'MICEL', 'PODDARHOUS', 'AROGRANITE', 'MAHASTEEL', 'BYKE', 'VERTOZ', 'INCREDIBLE', 'TCIDEVELOP', 'BEWLTD', 'AIROLAM', 'SOFTTECH', 'PRAKASHSTL', 'IZMO', 'BSL', 'ASPINWALL', 
             'DBSTOCKBRO', 'BHAGYAPROP', 'TOUCHWOOD', 'E2E', 'BLBLIMITED', 'AARON', 'ROML', 'KAMATHOTEL', 'CENTEXT', 'ICEMAKE', 'DRSDILIP', 'TIRUPATIFL', 'MOTOGENFIN', 'RSSOFTWARE', 'RAJSREESUG', 'CINEVISTA', 'DSML', 'TOKYOPLAST', 'GROBTEA', 'FOCE', 'LOTUSEYE', 'MUKTAARTS', 'SHAHALLOYS', 'OMAXAUTO', 'AUSOMENT', 'MORARJEE', 'SALSTEEL', 'DGCONTENT', 'LAMBODHARA', 'SANWARIA', 'MRO-TEK', 'GLOBALVECT', 'TREJHARA', 'BIOFILCHEM', 'WELINV', 'BAGFILMS', 'AAREYDRUGS', 'ROLLT', 'SIL', 'SPMLINFRA', 'WEIZMANIND', 'SARVESHWAR', 'IMAGICAA', 'SUMEETINDS', 'LAGNAM', 'INDBANK', 'SHREERAMA', 'JAIPURKURT', 'ARVEE', 'UJAAS', 'TARMAT', 'NECCLTD', 'ALKALI', 'STEELCITY', 'VMARCIND', 'ABMINTLLTD', 'IL&FSENGG', 'GAL', 'GANGESSECU', 'PKTEA', 'JAINAM', 'PALASHSECU', 'MITCON', 'SHIVAUM', 'CELEBRITY', 'MCL', 'ZODIAC', 'PARIN', 'PANACHE', 'UTTAMSTL', 'SRPL', 'EASTSILK', 'FOCUS', 'MADHUCON', 'EXCEL', 'AMDIND', 'SVLL', 'ARCHIDPLY', 'SICAL', 'SAGARDEEP', 'PNC', 'SIMBHALS', 'DHRUV', 'AVG', 'DEVIT', 'HOVS', 'GEEKAYWIRE', 'GODHA', 'NITIRAJ', 'CORDSCABLE', 'HINDCON', 'CMICABLES', 'SPECTRUM', 'BANKA', 'PRESSMN', 'VCL', 'ARSSINFRA', 'ATALREAL', 'VINEETLAB', 'MERCATOR', 'ANIKINDS', 'CALSOFT', 'EDUCOMP', 'OPTOCIRCUI', 'KEYFINSERV', 'KRIDHANINF', 'SIKKO', 'UNIVASTU', 'NIDAN', 'AJOONI', 'DELTAMAGNT', 'ORIENTLTD', 'SONAMCLOCK', 'SOLEX', 'URAVI', 'AARVEEDEN', 'INDSWFTLTD', 'MTEDUCARE', 'VIVO', 'LCCINFOTEC', 'NEXTMEDIA', 'KALYANIFRG', 'SUPERSPIN', 'GLOBAL', 'HISARMETAL', 'OMKARCHEM', 'MAHICKRA', 'PRITI', 'TAINWALCHM', 'OSWALSEEDS', 'HPIL', 'SUPREMEINF', 'SGL', 'TERASOFT', 'AMBANIORG', 'ARCHIES', 'AURDIS', 'ANSALHSG', 'ICDSLTD', 'SUPREMEENG', 'MHHL', 'DHARSUGAR', 'TARACHAND', 'KHFM', 'MANUGRAPH', 'KRITIKA', 'NIBL', 'BDR', 'JAKHARIA', 'MALUPAPER', 'CCCL', 'PROLIFE', 'GOENKA', 'NITINFIRE', 'JETFREIGHT', 'SKIL', 'SCAPDVR', 'SHRADHA', 'VARDMNPOLY', 'FLEXITUFF', 'MARSHALL', 'FELDVR', 'FMNL', 'KKVAPOW', 'LIBAS', 'VASWANI', 'TANTIACONS', 'VIJIFIN', 'BEARDSELL', 'NAGREEKEXP', 'VIVIDHA', 'BANARBEADS', 'AAATECH', 'MADHAV', 'AKG', 'MKPL', 'BANG', 'DCI', 'DIGJAMLMTD', 'ZENITHEXPO', 'AGROPHOS', 'DIAPOWER', 'JISLDVREQS', '21STCENMGM', 'DUDIGITAL', 'SOMICONVEY', 'NPST', 'ASLIND', 'SECL', 'MRO', 'HBSL', 'BURNPUR', 'MDL', 'BVCL', 'TIRUPATI', 'COUNCODOS', 'AISL', 'TREEHOUSE', 'DYNAMIC', 'ASCOM', 'KARMAENG', 'LAXMICOT', 'SANGINITA', 'PATSPINLTD', 'OILCOUNTUB', 'PIGL', 'UCL', 'WIPL', 'LFIC', 'PATINTLOG', 'PARTYCRUS', 'JETKNIT', 'UNIINFO', 'CUBEXTUB', 'REXPIPES', 'TIMESGTY', 'BCONCEPTS', 'BALKRISHNA', 'HAVISHA', 'SHAIVAL', 'VAISHALI', 'KSHITIJPOL', 'RELIABLE', 'AGRITECH', 'SPENTEX', 'AMBICAAGAR', 'SUMIT', 'WEWIN', 'MAGNUM', 'VSCL', 'UNITEDPOLY', 'QUADPRO', 'SETUINFRA', 'TMRVL', 'AVROIND', 'PREMIER', 'SOMATEX', 'ARIHANT', 'SPCENET', 'HECPROJECT', 'BARTRONICS', 'COX&KINGS', 'SILGO', 'DKEGL', 
             'MUKANDENGG', 'VINNY', 'ORIENTALTL', 'GIRIRAJ', 'CROWN', 'MANGTIMBER', 'SECURCRED', 'INFOMEDIA', 'GAYAHWS', 'LGHL', 'PEARLPOLY', 'METALFORGE', 'DNAMEDIA', '3PLAND', 'TGBHOTELS', 'MITTAL', 'LEXUS', 'WILLAMAGOR', 'LATTEYS', 'WSI', 'ORTINLAB', 'ACEINTEG', 'GOLDSTAR', 'SURANI', 'HILTON', 'RMCL', 'SONAHISONA', 'ADL', 'MILTON', 'TIJARIA', 'ANTGRAPHIC', 'TNTELE', 'SILLYMONKS', 'SPYL', 'NATNLSTEEL', 'MOHITIND', 'KHANDSE', 'SIDDHIKA', 'SHANTI', 'RKDL', 'GUJRAFFIA', 'ALPSINDUS', 'CMMIPL', 'NTL', 'STAMPEDE', 'S&SPOWER', 'KEERTI', 'SABEVENTS', 'CADSYS', 'TFL', 'BMETRICS', 'ONELIFECAP', 'NKIND', 'GICL', 'VICEROY', 'ADROITINFO', 'UMESLTD', 'CYBERMEDIA', 'BTML', 'BRIGHT', 'ZENITHSTL', 'ARENTERP', 'AVSL', 'PBAINFRA', 'LYPSAGEMS', 'NARMADA', 'KAVVERITEL', 'BKMINDST', 'SHYAMTEL', 'AUTOLITIND', 'THOMASCOTT', 'GTNTEX', 'SATHAISPAT', 'UWCSL', 'INDLMETER', 'JINDCOT', 'INTEGRA', 'SSINFRA', 'CANDC', 'FELIX', 'KHAITANLTD', 'GFSTEELS', 'JALAN', 'SANCO', 'VERA', 'INNOVATIVE', 'TVVISION', 'SHUBHLAXMI', 'DRL', 'WALPAR', 'NAGREEKCAP', 'EMCO', 'SMVD', 'MPTODAY', 'EASUNREYRL', 'EUROTEXIND', 'DALALSTCOM', 'TECHIN', 'RAJRAYON', 'KAUSHALYA', 'MASKINVEST', 'GLFL', 'AHIMSA', 'PDPL', 'NORBTEAEXP', 'PERFECT', 'IMPEXFERRO', 'SRIRAM', 'MOHOTAIND', 'TARAPUR', 'PULZ', 'RMDRIP', 'CONTI', 'BOHRA', 'ABINFRA', 'CREATIVEYE', 'BLUECOAST', 'SABTN', 'MINDPOOL', 'MELSTAR', 'LAKPRE', 'ABNINT', 'TCIFINANCE', 'AMJUMBO', 'SUBCAPCITY', 'RADAAN', 'HOTELRUGBY', 'DCMFINSERV', 'SKSTEXTILE', 'NIRAJISPAT', 'AILIMITED', 'DESTINY', 'OMFURN', 'BGLOBAL', 'ACCORD', 'KALYANI', 'PAEL', 'PRADIP', 'MANAV', 'ORTEL', 'REGENCERAM', 'GANGOTRI', 'SONISOYA', 'BHALCHANDR', 'GRETEX', 'JIKIND', 'QUINTEGRA', 'TRANSWIND', 'CKPLEISURE', 'GISOLUTION', 'RAJVIR', 'VASA', 'JAINSTUDIO', 'POWERFUL', 'BLUECHIP', 'SELMC', 'ATNINTER', 'SEJALLTD']

timelist=['09:15','09:30','09:45','10:00','10:15','10:30','10:45','11:00','11:15','11:30','11:45','12:00','12:15','12:30','12:45','13:00','13:15','13:30','13:45','14:00','14:15','14:30','14:45','15:00','15:15']

if sc_list == "Nifty 500":
    final_list=nifty_500
elif sc_list == "Large Cap":
    final_list=large_list
elif sc_list == "Mid Cap":
    final_list=mid_list
elif sc_list == "Small Cap":
    final_list=small_list
else:
    st.text("select some script")
        

if(st.button("Start Screening")):
    if strgy == "ABC":
        j=0
        my_bar = st.progress(0)
        for i in final_list:
            j+=1
            percent_complete=j/len(final_list)
            my_bar.progress(percent_complete)
            sym="{0}.NS".format(i)
            try:
                d = pdr.get_data_yahoo(sym,period="max",interval='1d')
                d = d.reset_index()
                d = d.drop(['Volume'],axis = 1)
                ma50 = get_sma(d.Close,50)
                bwl_up,bwl_dw=Boll_band(d.Close)
                ma_list=list(ma50)
                bwl_up_list = list(bwl_up)
                bwl_dw_list = list(bwl_dw)
                close_list = list(d.Close)
                open_list = list(d.Open)
                low_list = list(d.Low)
                high_list = list(d.High)
                date_list = list(d.Date)
                check=ma_list[-1]-bwl_dw_list[-1]
            
            
                if ma_list[-1]>ma_list[-3]:
                    if bwl_dw_list[-1]>ma_list[-1] or check<=12:
                        if (((0.0001 < ((close_list[-1]-bwl_dw_list[-1])/close_list[-1])) and  ( ((close_list[-1]-bwl_dw_list[-1])/close_list[-1])<0.03)) and ((0.0001< float((close_list[-1]-ma_list[-1])/close_list[-1])) and (float((close_list[-1]-ma_list[-1])/close_list[-1])<0.03))):
                            if close_list[-1]>open_list[-1]:
                                per=(((high_list[-1]-low_list[-1])/high_list[-1])*100)
                                if ((0<int(round(per,1)))or(int(round(per,1))<=6)):
                                    set1 = { 'x': date_list[-100:], 'open': open_list[-100:], 'close': close_list[-100:], 'high': high_list[-100:], 'low': low_list[-100:], 'type': 'candlestick','name' : 'price'}
                                    set2 = { 'x': date_list[-100:], 'y': ma50[-100:], 'type': 'scatter', 'mode': 'lines', 'line': { 'width': 1, 'color': 'black' },'name': 'MA 50 periods','hoverinfo':'skip'}
                                    set3 = { 'x': date_list[-100:], 'y': bwl_up[-100:], 'type': 'scatter', 'mode': 'lines', 'line': { 'width': 1, 'color': 'green' },'name': 'Bollinger up','hoverinfo':'skip'}
                                    set4 = { 'x': date_list[-100:], 'y': bwl_dw[-100:], 'type': 'scatter', 'mode': 'lines', 'line': { 'width': 1, 'color': 'red' },'name': 'Bollinger down','hoverinfo':'skip'}
                                    data = [set1, set2,set3,set4]
                                    fig = go.Figure(data=data)
                                    fig.update_layout(title_text=i +" CLOSE: "+str(round(list(d.Close)[-1],3))+" OPEN: "+str(round(list(d.Open)[-1],3))+" HIGH: "+str(round(list(d.High)[-1],3))+
                                            " LOW: "+str(round(list(d.Low)[-1],3))+" \n AS ON "+str(end.date()))
                                    fig.update_layout(width=1250,height=700) 
                                    fig.show(config={'modeBarButtonsToAdd':['drawline','eraseshape']})
                                    st.plotly_chart(fig)
                                    if low_list[-1]>low_list[-2]:
                                        fin=low_list[-2]
                                    else:
                                        fin=low_list[-1]
                                    risk,ep,sl,nos,tg1,tg2=risk_ana(high_list[-1]+1,fin-1)          
                                    st.text("Risk-- "+str(risk)+"\n"+"ENTRY PRICE-- "+str(ep)+"\n"+"Stop Loss-- "+str(sl)+"\n"+"NO OF SHARES-- "+str(nos)+"\n"+"TARGET 1:01 -- "+str(tg1)+"\n"+"TARGET 1:02 -- "+str(tg2))
                                else:
                                    pass
    
                            elif ((((close_list[-1]==high_list[-1])or(close_list[-1]>=high_list[-1]-2))and (open_list[-1]>=(2*low_list[-1]))) 
                                or (((open_list[-1]==high_list[-1])or(open_list[-1]>=high_list[-1]-2)) and (close_list[-1]>=(2*low_list[-1])))):
                                    set1 = { 'x': date_list[-100:], 'open': open_list[-100:], 'close': close_list[-100:], 'high': high_list[-100:], 'low': low_list[-100:], 'type': 'candlestick','name' : 'price'}
                                    set2 = { 'x': date_list[-100:], 'y': ma50[-100:], 'type': 'scatter', 'mode': 'lines', 'line': { 'width': 1, 'color': 'black' },'name': 'MA 50 periods','hoverinfo':'skip'}
                                    set3 = { 'x': date_list[-100:], 'y': bwl_up[-100:], 'type': 'scatter', 'mode': 'lines', 'line': { 'width': 1, 'color': 'green' },'name': 'Bollinger up','hoverinfo':'skip'}
                                    set4 = { 'x': date_list[-100:], 'y': bwl_dw[-100:], 'type': 'scatter', 'mode': 'lines', 'line': { 'width': 1, 'color': 'red' },'name': 'Bollinger down','hoverinfo':'skip'}
                                    data = [set1, set2,set3,set4]
                                    fig = go.Figure(data=data)
                                    fig.update_layout(title_text=i +" CLOSE: "+str(round(list(d.Close)[-1],3))+" OPEN: "+str(round(list(d.Open)[-1],3))+" HIGH: "+str(round(list(d.High)[-1],3))+
                                            " LOW: "+str(round(list(d.Low)[-1],3))+" \n AS ON "+str(end.date()))
                                    fig.update_layout(width=1250,height=700)
                                    fig.show(config={'modeBarButtonsToAdd':['drawline','eraseshape']}) 
                                    st.plotly_chart(fig)
                                    if low_list[-1]>low_list[-2]:
                                        fin=low_list[-2]
                                    else:
                                        fin=low_list[-1]
                                    risk,ep,sl,nos,tg1,tg2=risk_ana(high_list[-1]+1,fin-1)          
                                    st.text("Risk-- "+str(risk)+"\n"+"ENTRY PRICE-- "+str(ep)+"\n"+"Stop Loss-- "+str(sl)+"\n"+"NO OF SHARES-- "+str(nos)+"\n"+"TARGET 1:01 -- "+str(tg1)+"\n"+"TARGET 1:02 -- "+str(tg2),key="txt2")
    
            except Exception as e:
                pass            
        my_bar.empty()
        st.balloons()    
        
    
    elif strgy == "44MA":
        j=0
        my_bar = st.progress(0)
        for i in final_list:
            j+=1
            percent_complete=j/len(final_list)
            my_bar.progress(percent_complete)    
            sym="{0}.NS".format(i)
            try:
                d = pdr.get_data_yahoo(sym,period="max",interval='1d')
                d = d.reset_index()
                d = d.drop(['Volume'],axis = 1)
                ma44 = get_sma(d.Close,44)
                bwl_up,bwl_dw=Boll_band(d.Close)
                ma_list=list(ma44)

                bwl_up_list = list(bwl_up)
                bwl_dw_list = list(bwl_dw)
                close_list = list(d.Close)
                open_list = list(d.Open)
                low_list = list(d.Low)
                high_list = list(d.High)
                date_list = list(d.Date)

    
                if ma_list[-1]>ma_list[-3]:
                    if (((0.0001 < ((close_list[-1]-bwl_dw_list[-1])/close_list[-1])) and  ( ((close_list[-1]-bwl_dw_list[-1])/close_list[-1])<0.03)) and ((0.0001< float((close_list[-1]-ma_list[-1])/close_list[-1])) and (float((close_list[-1]-ma_list[-1])/close_list[-1])<0.03))):
                        if close_list[-1]>open_list[-1]:
                            per=(((high_list[-1]-low_list[-1])/high_list[-1])*100)
                            if ((0<int(round(per,1)))or(int(round(per,1))<=6)):
                                set1 = { 'x': date_list[-100:], 'open': open_list[-100:], 'close': close_list[-100:], 'high': high_list[-100:], 'low': low_list[-100:], 'type': 'candlestick','name' : 'price'}
                                set2 = { 'x': date_list[-100:], 'y': ma44[-100:], 'type': 'scatter', 'mode': 'lines', 'line': { 'width': 1, 'color': 'black' },'name': 'MA 44 periods','hoverinfo':'skip'}
                            
                                data = [set1, set2]
    
                                fig = go.Figure(data=data)
                                fig.update_layout(title_text=i +" CLOSE: "+str(round(list(d.Close)[-1],3))+" OPEN: "+str(round(list(d.Open)[-1],3))+" HIGH: "+str(round(list(d.High)[-1],3))+
                                            " LOW: "+str(round(list(d.Low)[-1],3))+" \n AS ON "+str(end.date()))
                                fig.update_layout(width=1250,height=700)
                                fig.show(config={'modeBarButtonsToAdd':['drawline','eraseshape']}) 
                                     
                                st.plotly_chart(fig)
                        
                                if low_list[-1]>low_list[-2]:
                                    fin=low_list[-2]
                                else:
                                    fin=low_list[-1]
                                risk,ep,sl,nos,tg1,tg2=risk_ana(high_list[-1]+1,fin-1)          
                                st.text("Risk-- "+str(risk)+"\n"+"ENTRY PRICE-- "+str(ep)+"\n"+"Stop Loss-- "+str(sl)+"\n"+"NO OF SHARES-- "+str(nos)+"\n"+"TARGET 1:01 -- "+str(tg1)+"\n"+"TARGET 1:02 -- "+str(tg2))
                        
                        elif ((((0<=high_list[-1]-close_list[-1])and(1>=high_list[-1]-close_list[-1]))and((close_list[-1]-open_list[-1])*2 <=(open_list[-1]-low_list[-1]))) or 
                                (((0<=high_list[-1]-open_list[-1])and(1>=high_list[-1]-open_list[-1]))and((open_list[-1]-close_list[-1])*2 <=(close_list[-1]-low_list[-1])))):
                                set1 = { 'x': date_list[-100:], 'open': open_list[-100:], 'close': close_list[-100:], 'high': high_list[-100:], 'low': low_list[-100:], 'type': 'candlestick','name' : 'price'}
                                set2 = { 'x': date_list[-100:], 'y': ma44[-100:], 'type': 'scatter', 'mode': 'lines', 'line': { 'width': 1, 'color': 'black' },'name': 'MA 44 periods','hoverinfo':'skip'}
                            
                                data = [set1, set2]
    
                                fig = go.Figure(data=data)
                                fig.update_layout(title_text=i +" CLOSE: "+str(round(list(d.Close)[-1],3))+" OPEN: "+str(round(list(d.Open)[-1],3))+" HIGH: "+str(round(list(d.High)[-1],3))+
                                            " LOW: "+str(round(list(d.Low)[-1],3))+" \n AS ON "+str(end.date()))
                                fig.update_layout(width=1250,height=700) 
                                fig.show(config={'modeBarButtonsToAdd':['drawline','eraseshape']}) 
                                    
                                st.plotly_chart(fig)
                        
                                if low_list[-1]>low_list[-2]:
                                    fin=low_list[-2]
                                else:
                                    fin=low_list[-1]
                                risk,ep,sl,nos,tg1,tg2=risk_ana(high_list[-1]+1,fin-1)          
                                st.text("Risk-- "+str(risk)+"\n"+"ENTRY PRICE-- "+str(ep)+"\n"+"Stop Loss-- "+str(sl)+"\n"+"NO OF SHARES-- "+str(nos)+"\n"+"TARGET 1:01 -- "+str(tg1)+"\n"+"TARGET 1:02 -- "+str(tg2))
                        else:
                            pass
                    else:
                        pass
                else:
                    pass
            except Exception as e:
                pass        
        my_bar.empty()
        st.balloons()    
    
        

    elif strgy == "BOLLINGER BAND":
        j=0
        my_bar = st.progress(0)
        for i in final_list:
            j+=1
            percent_complete=j/len(final_list)
            my_bar.progress(percent_complete)    
            sym="{0}.NS".format(i)
            try:
                d = pdr.get_data_yahoo(sym,period="max",interval='1d')
                d = d.reset_index()
                d = d.drop(['Volume'],axis = 1)
                bwl_up,bwl_dw=Boll_band(d.Close)
                bwl_up_list = list(bwl_up)
                bwl_dw_list = list(bwl_dw)
                close_list = list(d.Close)
                open_list = list(d.Open)
                low_list = list(d.Low)
                high_list = list(d.High)
                date_list = list(d.Date)
            
    
                if open_list[-2]>close_list[-2] and bwl_dw_list[-2]>close_list[-2]:
                    if close_list[-1]>open_list[-1] and close_list[-1]>bwl_dw_list[-1]:
                        set1 = { 'x': date_list[-100:], 'open': open_list[-100:], 'close': close_list[-100:], 'high': high_list[-100:], 'low': low_list[-100:], 'type': 'candlestick','name' : 'price'}
                        set2 = { 'x': date_list[-100:], 'y': bwl_up_list[-100:], 'type': 'scatter', 'mode': 'lines', 'line': { 'width': 1, 'color': 'green' },'name': 'Bollinger up','hoverinfo':'skip'}
                        set3 = { 'x': date_list[-100:], 'y': bwl_dw_list[-100:], 'type': 'scatter', 'mode': 'lines', 'line': { 'width': 1, 'color': 'red' },'name': 'Bollinger down','hoverinfo':'skip'}
                        data = [set1, set2,set3]
                        fig = go.Figure(data=data)
                        fig.update_layout(title_text=i +" CLOSE: "+str(round(list(d.Close)[-1],3))+" OPEN: "+str(round(list(d.Open)[-1],3))+" HIGH: "+str(round(list(d.High)[-1],3))+
                                            " LOW: "+str(round(list(d.Low)[-1],3))+" \n AS ON "+str(end.date()))
                        fig.update_layout(width=1250,height=700) 
                        fig.show(config={'modeBarButtonsToAdd':['drawline','eraseshape']}) 
                                    
                        st.plotly_chart(fig)
                        if low_list[-1]>low_list[-2]:
                            fin=low_list[-2]
                        else:
                            fin=low_list[-1]
                        risk,ep,sl,nos,tg1=risk_ana(high_list[-1]+1,fin-1,"BB")          
                        st.text("Risk-- "+str(risk)+"\n"+"ENTRY PRICE-- "+str(ep)+"\n"+"Stop Loss-- "+str(sl)+"\n"+"NO OF SHARES-- "+str(nos)+"\n"+"TARGET 1:03 -- "+str(tg1))
                    else:
                        pass
                else:
                    pass
            except Exception as e:
                pass
        my_bar.empty()
        st.balloons()
        
    elif strgy == "ATH":
        j=0
        my_bar = st.progress(0)
        for i in final_list:
            j+=1
            percent_complete=j/len(final_list)
            my_bar.progress(percent_complete)    
            s="{0}.NS".format(i)
            try:
                y = pdr.get_data_yahoo(s,period="max",interval='1mo')
                y = y.reset_index()
                hgh=max(list(y['High']))
                per_close = (hgh-list(y['Close'])[-1])/(list(y['Close'])[-1]) 
                if (hgh == list(y['Close'])[-1]) or (0<per_close and per_close<0.05): 
                    st.write('[{0}](https://in.tradingview.com/chart/YV59lPqR/?symbol=NSE%3A{0})'.format(i))
            except Exception as e:
                pass
        my_bar.empty()
        st.balloons()    
    
    elif strgy == "15 MIN BUY (ABC)":
        j=0
        my_bar = st.progress(0)
        for i in final_list:
            j+=1
            percent_complete=j/len(final_list)
            my_bar.progress(percent_complete)    
            s="{0}.NS".format(i)
            try:
                y1 = pdr.get_data_yahoo(s,period="1mo",interval='15m')  
                y2 = pdr.get_data_yahoo(s,period="1d",interval='15m')
                ma50=get_sma(y1.Close,50)
                y1 = y1.reset_index()
                y2 = y2.reset_index()
                td_len = int(y2.shape[0])
                bwl_up,bwl_dw=Boll_band(y1.Close)
                last_bwl_dw=list(bwl_dw)[-td_len+1:]
                last_bwl_up=list(bwl_up)[-td_len+1:]
                last_close=list(y2.Close)[-2]
                last_open=list(y2.Open)[-2]
                last_high=list(y2.High)[-2]
                last_low=list(y2.Low)[-2]
                last_low2=list(y2.Low)[-3]
                ma50_list=list(ma50)
                date_list=timelist[:td_len+1]
                fig = go.Figure()
                
                rising=list(ma50)[-td_len:]
                bwl_up_1=bwl_up[-td_len:]
                bwl_dw_1=bwl_dw[-td_len:]
                
                check=abs((last_bwl_dw[-2]-rising[-2])/last_bwl_dw[-2])
                check1=abs((last_high-last_close)/last_close)
                check2=abs((last_high-last_open)/last_open)
                
                if (rising[-1]>rising[-3]) or  ma50_list[-1] > ma50_list[-3] :
                    if abs(check)<=0.001:
                        if ( (0.0001 < abs(((last_open-last_bwl_dw[-1])/last_bwl_dw[-1]))) and  (abs(((last_open-last_bwl_dw[-1])/last_bwl_dw[-1]))<0.001)) and ((0.0001< abs((last_open-rising[-2])/last_open)) and (abs((last_open-rising[-2])/last_open)<0.001)):
                            if last_open<last_close:
                                per=abs((last_close-last_open)/last_open)
                                if ((0<per)or (per<=6)):  
                                    set1 = { 'x': date_list, 'open': y2.Open, 'close': y2.Close, 'high': y2.High, 'low': y2.Low, 'type': 'candlestick','name' : 'price'}
                                    set2 = { 'x': date_list, 'y': rising, 'type': 'scatter', 'mode': 'lines', 'line': { 'width': 1, 'color': 'black' },'name': 'MA 50 periods','hoverinfo':'skip'}
                                    set3 = { 'x': date_list, 'y':bwl_up_1 , 'type': 'scatter', 'mode': 'lines', 'line': { 'width': 1, 'color': 'green' },'name': 'Bollinger up','hoverinfo':'skip'}
                                    set4 = { 'x': date_list, 'y': bwl_dw_1, 'type': 'scatter', 'mode': 'lines', 'line': { 'width': 1, 'color': 'red' },'name': 'Bollinger down','hoverinfo':'skip'}
                                    data = [set1, set2,set3,set4]
                                    fig = go.Figure(data=data)
                                    fig.update_layout(title_text=i +" CLOSE: "+str(round(last_close,3))+" OPEN: "+
                                        str(round(last_open,3))+" HIGH: "+str(round(last_high,3))+
                                        " LOW: "+str(round(last_low,3))+
                                        " AS ON "+str(end.date())+" STRATEGY - 15MIN ABC (GBC)")
                                    fig.show(config={'modeBarButtonsToAdd':['drawline','eraseshape']})
                                    fig.update_layout(width=1250,height=700) 
                                    fig.show(config={'modeBarButtonsToAdd':['drawline','eraseshape']}) 
                                    
                                    st.plotly_chart(fig)
                                    if last_low>last_low2:
                                        fin=last_low2
                                    else:
                                        fin=last_low
                                    risk,ep,sl,nos,tg1,tg2=risk_ana(last_high+1,fin-1)          
                                    st.text("Risk-- "+str(risk)+"\n"+"ENTRY PRICE-- "+str(ep)+"\n"+"Stop Loss-- "+str(sl)+"\n"+"NO OF SHARES-- "+str(nos)+"\n"+"TARGET 1:01 -- "+str(tg1)+"\n"+"TARGET 1:02 -- "+str(tg2))
                                
                            
            
                            elif ((((last_high==last_close)or((check1>=0)and(check1<=0.005)))and (last_low>=(2*last_open))) or (((last_open==last_high)or((check2>=0)and(check2<=0.005))) and (last_low>=(2*last_close)))):
                                set1 = { 'x': date_list, 'open': y2.Open, 'close': y2.Close, 'high': y2.High, 'low': y2.Low, 'type': 'candlestick','name' : 'price'}
                                set2 = { 'x': date_list, 'y': rising, 'type': 'scatter', 'mode': 'lines', 'line': { 'width': 1, 'color': 'black' },'name': 'MA 50 periods','hoverinfo':'skip'}
                                set3 = { 'x': date_list, 'y':bwl_up_1 , 'type': 'scatter', 'mode': 'lines', 'line': { 'width': 1, 'color': 'green' },'name': 'Bollinger up','hoverinfo':'skip'}
                                set4 = { 'x': date_list, 'y': bwl_dw_1, 'type': 'scatter', 'mode': 'lines', 'line': { 'width': 1, 'color': 'red' },'name': 'Bollinger down','hoverinfo':'skip'}
                                data = [set1, set2,set3,set4]
                                fig = go.Figure(data=data)
                                fig.update_layout(title_text=i +" CLOSE: "+str(round(last_close,3))+" OPEN: "+
                                    str(round(last_open,3))+" HIGH: "+str(round(last_high,3))+
                                    " LOW: "+str(round(last_low,3))+
                                    " AS ON "+str(end.date())+" STRATEGY - ABC (Hammer)")
                                fig.show(config={'modeBarButtonsToAdd':['drawline','eraseshape']})
                                fig.update_layout(width=1250,height=700) 
                                fig.show(config={'modeBarButtonsToAdd':['drawline','eraseshape']}) 
                                    
                                st.plotly_chart(fig)
                                if last_low>last_low2:
                                    fin=last_low2
                                else:
                                    fin=last_low
                                risk,ep,sl,nos,tg1,tg2=risk_ana(last_high+1,fin-1)         
                                st.text("Risk-- "+str(risk)+"\n"+"ENTRY PRICE-- "+str(ep)+"\n"+"Stop Loss-- "+str(sl)+"\n"+"NO OF SHARES-- "+str(nos)+"\n"+"TARGET 1:01 -- "+str(tg1)+"\n"+"TARGET 1:02 -- "+str(tg2))
            except Exception as e:
                pass
        my_bar.empty()
        st.balloons()    

    elif strgy == "15 MIN SELL (ABC)":
        j=0
        my_bar = st.progress(0)
        for i in final_list:
            j+=1
            percent_complete=j/len(final_list)
            my_bar.progress(percent_complete)    
            s="{0}.NS".format(i)
            try:
                y1 = pdr.get_data_yahoo(s,period="1mo",interval='15m')  
                y2 = pdr.get_data_yahoo(s,period="1d",interval='15m')
                ma50=get_sma(y1.Close,50)
                y1 = y1.reset_index()
                y2 = y2.reset_index()
                td_len = int(y2.shape[0])
                bwl_up,bwl_dw=Boll_band(y1.Close)
                last_bwl_dw=list(bwl_dw)[-td_len+1:]
                last_bwl_up=list(bwl_up)[-td_len+1:]
                last_close=list(y2.Close)[-2]
                last_open=list(y2.Open)[-2]
                last_high=list(y2.High)[-2]
                last_low=list(y2.Low)[-2]
                last_low2=list(y2.Low)[-3]
                date_list=timelist[:td_len+1]
                fig = go.Figure()
                rising=list(ma50)[-td_len:]
                bwl_up_1=bwl_up[-td_len:]
                bwl_dw_1=bwl_dw[-td_len:]
                check=abs((last_bwl_up[-2]-rising[-2])/last_bwl_up[-2])
                #inverted hammer
                #red
                check1=abs((last_open-last_low)/last_low)
                #green
                check2=abs((last_close-last_low)/last_low)
                if rising[-3]>rising[-1]:
                    if check<=0.001:
                        if ( (0.0001 < abs((last_open-last_bwl_up[-1])/last_bwl_up[-1])) and  ((abs((last_open-last_bwl_up[-1])/last_bwl_up[-1])<0.001)) and ((0.0001< abs((last_open-rising[-2])/last_open)) and (abs((last_open-rising[-2])/last_open)<0.001))):
                            if last_open>last_close:
                                per=abs((last_open-last_close)/last_close)
                                #print("yoo2",per,i)
                                if ((0<per)or(per<=6)):  
                                    set1 = { 'x': date_list, 'open': y2.Open, 'close': y2.Close, 'high': y2.High, 'low': y2.Low, 'type': 'candlestick','name' : 'price'}
                                    set2 = { 'x': date_list, 'y': rising, 'type': 'scatter', 'mode': 'lines', 'line': { 'width': 1, 'color': 'black' },'name': 'MA 50 periods','hoverinfo':'skip'}
                                    set3 = { 'x': date_list, 'y':bwl_up_1 , 'type': 'scatter', 'mode': 'lines', 'line': { 'width': 1, 'color': 'green' },'name': 'Bollinger up','hoverinfo':'skip'}
                                    set4 = { 'x': date_list, 'y': bwl_dw_1, 'type': 'scatter', 'mode': 'lines', 'line': { 'width': 1, 'color': 'red' },'name': 'Bollinger down','hoverinfo':'skip'}
                                    data = [set1, set2,set3,set4]
                                    fig = go.Figure(data=data)
                                    fig.update_layout(title_text=i +" CLOSE: "+str(round(last_close,3))+" OPEN: "+
                                        str(round(last_open,3))+" HIGH: "+str(round(last_high,3))+
                                        " LOW: "+str(round(last_low,3))+
                                        " AS ON "+str(end.date())+" STRATEGY - 15 MIN BUY (GBC)")
                                    fig.show(config={'modeBarButtonsToAdd':['drawline','eraseshape']})
                                    fig.update_layout(width=1250,height=700) 
                                    fig.show(config={'modeBarButtonsToAdd':['drawline','eraseshape']}) 
                                    
                                    st.plotly_chart(fig)
                        
                                    if last_low>last_low2:
                                        fin=last_low2
                                    else:
                                        fin=last_low
                                    risk,ep,sl,nos,tg1,tg2=risk_ana(fin-1,last_high+1)          
                                    st.text("Risk-- "+str(risk)+"\n"+"ENTRY PRICE-- "+str(ep)+"\n"+"Stop Loss-- "+str(sl)+"\n"+"NO OF SHARES-- "+str(nos)+"\n"+"TARGET 1:01 -- "+str(tg1)+"\n"+"TARGET 1:02 -- "+str(tg2))
                        #break
                            elif ((((last_open==last_low)or((check1>=0)and(check1<=0.005)))and (last_high>=(2*last_close))) or (((last_close==last_low)or((check2>=0)and(check2<=0.005))) and (last_high>=(2*last_open)))):
                                set1 = { 'x': date_list, 'open': y2.Open, 'close': y2.Close, 'high': y2.High, 'low': y2.Low, 'type': 'candlestick','name' : 'price'}
                                set2 = { 'x': date_list, 'y': rising, 'type': 'scatter', 'mode': 'lines', 'line': { 'width': 1, 'color': 'black' },'name': 'MA 50 periods','hoverinfo':'skip'}
                                set3 = { 'x': date_list, 'y':bwl_up_1 , 'type': 'scatter', 'mode': 'lines', 'line': { 'width': 1, 'color': 'green' },'name': 'Bollinger up','hoverinfo':'skip'}
                                set4 = { 'x': date_list, 'y': bwl_dw_1, 'type': 'scatter', 'mode': 'lines', 'line': { 'width': 1, 'color': 'red' },'name': 'Bollinger down','hoverinfo':'skip'}
                                data = [set1, set2,set3,set4]
                                fig = go.Figure(data=data)
                                fig.update_layout(title_text=i +" CLOSE: "+str(round(last_close,3))+" OPEN: "+
                                    str(round(last_open,3))+" HIGH: "+str(round(last_high,3))+
                                    " LOW: "+str(round(last_low,3))+
                                    " AS ON "+str(end.date())+" STRATEGY - 15 MIN SELL  (GBC)")
                                fig.show(config={'modeBarButtonsToAdd':['drawline','eraseshape']})
                                fig.update_layout(width=1250,height=700) 
                                fig.show(config={'modeBarButtonsToAdd':['drawline','eraseshape']}) 
                                    
                                st.plotly_chart(fig)
                        
                                if last_low>last_low2:
                                    fin=last_low2
                                else:
                                    fin=last_low
                                risk,ep,sl,nos,tg1,tg2=risk_ana(fin-1,last_high+1)         
                                st.text("Risk-- "+str(risk)+"\n"+"ENTRY PRICE-- "+str(ep)+"\n"+"Stop Loss-- "+str(sl)+"\n"+"NO OF SHARES-- "+str(nos)+"\n"+"TARGET 1:01 -- "+str(tg1)+"\n"+"TARGET 1:02 -- "+str(tg2))
            except Exception as e:
                pass
        my_bar.empty()
        st.balloons()    
    elif strgy == "15 MIN BUY (44MA)":
        j=0
        my_bar = st.progress(0)
        for i in final_list:
            j+=1
            percent_complete=j/len(final_list)
            my_bar.progress(percent_complete)    
            s="{0}.NS".format(i)
            try:
                y1 = pdr.get_data_yahoo(s,period="1mo",interval='15m')  
                y2 = pdr.get_data_yahoo(s,period="1d",interval='15m')
                ma44=get_sma(y1.Close,44)
                y1 = y1.reset_index()
                y2 = y2.reset_index()
                td_len = int(y2.shape[0])
                bwl_up,bwl_dw=Boll_band(y1.Close)
                last_bwl_dw=list(bwl_dw)[-td_len+1:]
                last_bwl_up=list(bwl_up)[-td_len+1:]
                last_close=list(y2.Close)[-2]
                last_open=list(y2.Open)[-2]
                last_high=list(y2.High)[-2]
                last_low=list(y2.Low)[-2]
                last_low2=list(y2.Low)[-3]
                date_list=timelist[:td_len+1]
                fig = go.Figure()
                rising=list(ma44)[-td_len:]

                if rising[-1]>rising[-3] or  ma50_list[-1] > ma50_list[-3] :
                    if (((0.0001 < ((last_close-last_bwl_dw[-1])/last_close)) and  ( ((last_close-last_bwl_dw[-1])/last_close)<0.03)) and ((0.0001< float((last_close-rising[-1])/last_close)) and (float((last_close-rising[-1])/last_close)<0.03))):
                        if last_close>last_open:
                            per=(((last_high-last_low)/last_high)*100)
                            if ((0<int(round(per,1)))or(int(round(per,1))<=6)):
                                set1 = { 'x': date_list, 'open': y2.Open, 'close': y2.Close, 'high': y2.High, 'low': y2.Low, 'type': 'candlestick','name' : 'price'}
                                set2 = { 'x': date_list, 'y': rising, 'type': 'scatter', 'mode': 'lines', 'line': { 'width': 1, 'color': 'black' },'name': 'MA 44 periods','hoverinfo':'skip'}
                            
                                data = [set1, set2]
    
                                fig = go.Figure(data=data)
                                fig.update_layout(title_text=i +" CLOSE: "+str(round(last_close,3))+" OPEN: "+str(round(last_open,3))+" HIGH: "+str(round(last_high,3))+
                                            " LOW: "+str(round(last_low,3))+" \n AS ON "+str(end.date())+" STRATEGY - 15MIN 44MA")
                                fig.update_layout(width=1250,height=700) 
                                fig.show(config={'modeBarButtonsToAdd':['drawline','eraseshape']}) 
                                    
                                st.plotly_chart(fig)
                        
                                if last_low>last_low2:
                                    fin=last_low2
                                else:
                                    fin=last_low
                                risk,ep,sl,nos,tg1,tg2=risk_ana(last_high+1,fin-1)
                                st.text("Risk-- "+str(risk)+"\n"+"ENTRY PRICE-- "+str(ep)+"\n"+"Stop Loss-- "+str(sl)+"\n"+"NO OF SHARES-- "+str(nos)+"\n"+"TARGET 1:01 -- "+str(tg1)+"\n"+"TARGET 1:02 -- "+str(tg2))
                        
                        elif ((((0<=last_high-last_close)and(1>=last_high-last_close))and((last_close-last_open)*2 <=(last_open-last_low))) or 
                                (((0<=last_high-last_open)and(1>=last_high-last_open))and((last_open-last_close)*2 <=(last_close-last_low)))):
                                set1 = { 'x': date_list, 'open': y2.Open, 'close': y2.Close, 'high': y2.High, 'low': y2.Low, 'type': 'candlestick','name' : 'price'}
                                set2 = { 'x': date_list, 'y': rising, 'type': 'scatter', 'mode': 'lines', 'line': { 'width': 1, 'color': 'black' },'name': 'MA 44 periods','hoverinfo':'skip'}
                            
                                data = [set1, set2]
    
                                fig = go.Figure(data=data)
                                fig.update_layout(title_text=i +" CLOSE: "+str(round(last_close,3))+" OPEN: "+str(round(last_open,3))+" HIGH: "+str(round(last_high,3))+
                                            " LOW: "+str(round(last_low,3))+" \n AS ON "+str(end.date())+" STRATEGY - 15MIN 44MA")
                                fig.update_layout(width=1250,height=700) 
                                fig.show(config={'modeBarButtonsToAdd':['drawline','eraseshape']}) 
                                    
                                st.plotly_chart(fig)
                        
                                if last_low>last_low2:
                                    fin=last_low2
                                else:
                                    fin=last_low
                                risk,ep,sl,nos,tg1,tg2=risk_ana(last_high+1,fin-1)
                                st.text("Risk-- "+str(risk)+"\n"+"ENTRY PRICE-- "+str(ep)+"\n"+"Stop Loss-- "+str(sl)+"\n"+"NO OF SHARES-- "+str(nos)+"\n"+"TARGET 1:01 -- "+str(tg1)+"\n"+"TARGET 1:02 -- "+str(tg2))
                        else:
                            pass
                    else:
                        pass
                else:
                    pass
            except Exception as e:
                pass 
        my_bar.empty()
        st.balloons()    
    
    elif strgy == "15 MIN SELL (44MA)":
        j=0
        my_bar = st.progress(0)
        for i in final_list:
            j+=1
            percent_complete=j/len(final_list)
            my_bar.progress(percent_complete)    
            s="{0}.NS".format(i)
            try:
                y1 = pdr.get_data_yahoo(s,period="1mo",interval='15m')  
                y2 = pdr.get_data_yahoo(s,period="1d",interval='15m')
                ma44=get_sma(y1.Close,44)
                y1 = y1.reset_index()
                y2 = y2.reset_index()
                td_len = int(y2.shape[0])
                bwl_up,bwl_dw=Boll_band(y1.Close)
                last_bwl_dw=list(bwl_dw)[-td_len+1:]
                last_bwl_up=list(bwl_up)[-td_len+1:]
                last_close=list(y2.Close)[-2]
                last_open=list(y2.Open)[-2]
                last_high=list(y2.High)[-2]
                last_low=list(y2.Low)[-2]
                last_low2=list(y2.Low)[-3]
                date_list=timelist[:td_len+1]
                fig = go.Figure()
                rising=list(ma44)[-td_len:]

                if rising[-1]<rising[-3] or  ma50_list[-1] < ma50_list[-3] :
                    if (((0.0001 < ((last_close-last_bwl_dw[-1])/last_close)) and  ( ((last_close-last_bwl_dw[-1])/last_close)<0.03)) and ((0.0001< float((last_close-rising[-1])/last_close)) and (float((last_close-rising[-1])/last_close)<0.03))):
                        if last_open>last_close:
                            per=(((last_high-last_low)/last_high)*100)
                            if ((0<int(round(per,1)))or(int(round(per,1))<=6)):
                                set1 = { 'x': date_list, 'open': y2.Open, 'close': y2.Close, 'high': y2.High, 'low': y2.Low, 'type': 'candlestick','name' : 'price'}
                                set2 = { 'x': date_list, 'y': rising, 'type': 'scatter', 'mode': 'lines', 'line': { 'width': 1, 'color': 'black' },'name': 'MA 44 periods','hoverinfo':'skip'}
                            
                                data = [set1, set2]
    
                                fig = go.Figure(data=data)
                                fig.update_layout(title_text=i +" CLOSE: "+str(round(last_close,3))+" OPEN: "+str(round(last_open,3))+" HIGH: "+str(round(last_high,3))+
                                            " LOW: "+str(round(last_low,3))+" \n AS ON "+str(end.date())+" STRATEGY - 15MIN 44MA")
                                fig.update_layout(width=1250,height=700) 
                                st.plotly_chart(fig)
                        
                                if last_low>last_low2:
                                    fin=last_low2
                                else:
                                    fin=last_low
                                risk,ep,sl,nos,tg1,tg2=risk_ana(last_high+1,fin-1)
                                st.text("Risk-- "+str(risk)+"\n"+"ENTRY PRICE-- "+str(ep)+"\n"+"Stop Loss-- "+str(sl)+"\n"+"NO OF SHARES-- "+str(nos)+"\n"+"TARGET 1:01 -- "+str(tg1)+"\n"+"TARGET 1:02 -- "+str(tg2))
                        
                        elif ((((0<=last_low-last_close)and(1>=last_low-last_close))and((last_close-last_open)*2 <=(last_high-last_close))) or 
                                (((0<=last_low-last_open)and(1>=last_low-last_open))and((last_open-last_close)*2 <=(last_high-last_open)))):
                                set1 = { 'x': date_list, 'open': y2.Open, 'close': y2.Close, 'high': y2.High, 'low': y2.Low, 'type': 'candlestick','name' : 'price'}
                                set2 = { 'x': date_list, 'y': rising, 'type': 'scatter', 'mode': 'lines', 'line': { 'width': 1, 'color': 'black' },'name': 'MA 44 periods','hoverinfo':'skip'}
                            
                                data = [set1, set2]
    
                                fig = go.Figure(data=data)
                                fig.update_layout(title_text=i +" CLOSE: "+str(round(last_close,3))+" OPEN: "+str(round(last_open,3))+" HIGH: "+str(round(last_high,3))+
                                            " LOW: "+str(round(last_low,3))+" \n AS ON "+str(end.date())+" STRATEGY - 15MIN 44MA")
                                fig.update_layout(width=1250,height=700) 
                                st.plotly_chart(fig)
                        
                                if last_low>last_low2:
                                    fin=last_low2
                                else:
                                    fin=last_low
                                risk,ep,sl,nos,tg1,tg2=risk_ana(last_high+1,fin-1)
                                st.text("Risk-- "+str(risk)+"\n"+"ENTRY PRICE-- "+str(ep)+"\n"+"Stop Loss-- "+str(sl)+"\n"+"NO OF SHARES-- "+str(nos)+"\n"+"TARGET 1:01 -- "+str(tg1)+"\n"+"TARGET 1:02 -- "+str(tg2))
                        else:
                            pass
                    else:
                        pass
                else:
                    pass
            except Exception as e:
                pass
                    
        my_bar.empty()
        st.balloons()
    elif strgy == "Trial":
        j=0
        my_bar = st.progress(0)
        for i in final_list:
            j+=1
            percent_complete=j/len(final_list)
            my_bar.progress(percent_complete)    
            s="{0}.NS".format(i)
            try:
                y = pdr.get_data_yahoo(s,period="max",interval='1d')
                y = y.reset_index()
                ma50 = get_sma(y.Close,50)
                ma44 = get_sma(y.Close,44)
                ma_list_50=list(ma50)
                ma_list_44=list(ma44)
                close_list = list(y.Close)
                open_list = list(y.Open)
                low_list = list(y.Low)
                high_list = list(y.High)
                date_list = list(y.Date)
                if ma_list_44[-1]>ma_list_44[-100] and ma_list_44[-1]>ma_list_44[-50] and ma_list_44[-1]>ma_list_44[-25]and ma_list_44[-1]>ma_list_44[-10]:
                    set1 = { 'x': date_list[-100:], 'open': open_list[-100:], 'close': close_list[-100:], 'high': high_list[-100:], 'low': low_list[-100:], 'type': 'candlestick','name' : 'price'}
                    set2 = { 'x': date_list[-100:], 'y': ma50[-100:], 'type': 'scatter', 'mode': 'lines', 'line': { 'width': 1, 'color': 'blue' },'name': 'MA 50 periods','hoverinfo':'skip'}
                    set3 = { 'x': date_list[-100:], 'y': ma44[-100:], 'type': 'scatter', 'mode': 'lines', 'line': { 'width': 1, 'color': 'black' },'name': 'MA 44 periods','hoverinfo':'skip'}
                    data = [set1, set2,set3]
                    fig = go.Figure(data=data)
                    fig.update_layout(title_text=i +" CLOSE: "+str(round(list(y.Close)[-1],3))+" OPEN: "+str(round(list(y.Open)[-1],3))+" HIGH: "+str(round(list(y.High)[-1],3))+
                            " LOW: "+str(round(list(y.Low)[-1],3))+" \n AS ON "+str(end.date()))
                    fig.update_layout(width=1250,height=700) 
                    fig.show(config={'modeBarButtonsToAdd':['drawline','eraseshape']})
                    st.plotly_chart(fig)
                else:
                    pass    
            except Exception as e:
                st.exception(e)
        my_bar.empty()
        st.balloons()    
    
    else:
        st.text("Select some strategy ")  
else:
    st.text("click on start Screening")      


st.secrets["DB_USERNAME"]
st.secrets["DB_TOKEN"]
