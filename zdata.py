import click
import pickle as pk
import csv
from jugaad_trader import Zerodha

watchlist = {'HCLTECH','TECHM','SBILIFE','ASIANPAINT','WIPRO','ITC','INFY','TCS','RELIANCE','CIPLA','JSWSTEEL','HEROMOTOCO','NESTLEIND','HINDUNILVR','SHREECEM','BHARTIARTL','HDFCBANK','BRITANNIA','ICICIBANK','HDFCLIFE','TITAN','HINDALCO','BAJAJ-AUTO','DIVISLAB','SUNPHARMA','TATAMOTORS','UPL','TATASTEEL','BAJFINANCE','LT','SBIN','INDUSINDBK','TATACONSUM','COALINDIA','MARUTI','BPCL','ULTRACEMCO','HDFC','ADANIPORTS','DRREDDY','POWERGRID','BAJAJFINSV','AXISBANK','KOTAKBANK','IOC','M&M','ONGC','EICHERMOT','NTPC','GRASIM'}
@click.command()
#@click.option("--instrument", "-i", help='Instrument name "NSE:INFY"', type=str)
@click.option("--from", "-f", "from_", help="from date yyyy-mm-dd")
@click.option("--to", "-t", help="to date yyyy-mm-dd")
@click.option("--interval", "-n", default="day", help="Data interval eg. minute, day")
@click.option("--output", "-o", help="Output file name")
def main(instrument, from_, to, interval, output):
    #print(instrument, from_, to, interval, output)
    kite = Zerodha()

    kite.set_access_token()
    q = kite.ltp(instrument)
    token = q[instrument]['instrument_token']
    for name in watchlist:
        
        data = kite.historical_data(NSE+'name', from_, to, interval)
        with open(output, 'w') as fp:
            writer = csv.DictWriter(fp, ["date", "open", "high", "low", "close", "volume"])
            writer.writeheader()
            writer.writerows(data)


if __name__ == "__main__":
    main()
