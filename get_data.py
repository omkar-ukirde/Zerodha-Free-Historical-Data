from jugaad_trader import Zerodha
import pandas as pd
import datetime
watchlist = {'HCLTECH','TECHM','SBILIFE','ASIANPAINT','WIPRO','ITC','INFY','TCS','RELIANCE','CIPLA','JSWSTEEL','HEROMOTOCO','NESTLEIND','HINDUNILVR','SHREECEM','BHARTIARTL','HDFCBANK','BRITANNIA','ICICIBANK','HDFCLIFE','TITAN','HINDALCO','BAJAJ-AUTO','DIVISLAB','SUNPHARMA','TATAMOTORS','UPL','TATASTEEL','BAJFINANCE','LT','SBIN','INDUSINDBK','TATACONSUM','COALINDIA','MARUTI','BPCL','ULTRACEMCO','HDFC','ADANIPORTS','DRREDDY','POWERGRID','BAJAJFINSV','AXISBANK','KOTAKBANK','IOC','M&M','ONGC','EICHERMOT','NTPC','GRASIM'}

delta = 100
interval = '5minute'
to_date = datetime.datetime.now().date()
from_date = to_date - datetime.timedelta(days=delta)


def get_data(name, from_, to, interval):

    kite = Zerodha()
    kite.set_access_token()
    q = kite.ltp('NSE:' + name)
    token = q['NSE:' + name]['instrument_token']
    data = kite.historical_data(token, from_date, to_date, interval)
    df = pd.DataFrame(data)
    df = df.set_index('date')
    df.to_csv(name + '.csv')


for name in watchlist:
    get_data(name, from_date, to_date, interval)
