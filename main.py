"""CryptoBot first file"""
# Python and API modules import
from binance.client import Client
import time

# Own modules import
import binance_keychain

def server_time_to_local_time(servertime):
    return time.ctime(servertime/1000)

def current_time():
    #print("Current %s time: %s"%(timezone,server_time_to_local_time(server_time)))
    return info_exchange.get('serverTime')

def percentage_difference(open_price, close_price):
    if close_price == open_price:
        return 0
    elif close_price > open_price:
        increase = close_price - open_price
        pd = (increase/open_price)*100
        return pd
    else:
        decrease = open_price - close_price
        pd = (decrease/open_price)*100
        return (-1)*pd

def trade_session_status(last_candle):
    last_open_time=last_candle[0]
    last_open=last_candle[1]
    last_high=last_candle[2]
    last_low=last_candle[3]
    last_close=last_candle[4]
    last_volume=last_candle[5]
    last_close_time=last_candle[6]
    last_qa_volume=last_candle[7]
    n_trades=last_candle[8]

    started_at=str(server_time_to_local_time(last_open_time))
    time_remaining=str((last_close_time - current_time())/1000)
    percent_completed=str(round(((current_time()-last_open_time)*100)/(last_close_time-last_open_time),2))
    open_price=str(last_open)
    current_price=str(last_close)
    closing_at=str(server_time_to_local_time(last_close_time))
    server_time = info_exchange.get('serverTime')
    current_server_time=server_time_to_local_time(server_time)
    pd = str(round(percentage_difference(float(last_open), float(last_close)),2))
    volume = str(round(float(last_volume),2))
    qa_volume=str(round(float(last_qa_volume),2))
    session="""
$MDA
Started: %s
Tweet: %s
Open: %s $BTC
Current: %s $BTC
Diff. Open: %s%%
Closing: %s
Trades: %s
Volume: %s MDA
QA Volume: %s BTC
    """%(started_at,current_server_time,open_price,current_price,pd,closing_at,str(n_trades), volume, qa_volume)
    return session

# Creating a client instance
client = Client(binance_keychain.api_key, binance_keychain.api_secret)
print(client)

#Get Exchange Info
info_exchange = client.get_exchange_info()
timezone = info_exchange.get('timezone')
server_time = info_exchange.get('serverTime')


#Get Kline/Candlesticks
candles = client.get_klines(symbol='MDABTC', interval=Client.KLINE_INTERVAL_30MINUTE)
last_candle=candles[len(candles)-1]

print(trade_session_status(last_candle))

from bearbot import BearBot

bot1 = BearBot()

bot1.tweet(trade_session_status(last_candle))

#1499040000000,      #0 Open time
#"0.01634790",       #1 Open
#"0.80000000",       #2 High
#"0.01575800",       #3 Low
#"0.01577100",       #4 Close
#"148976.11427815",  #5 Volume
#1499644799999,      #6 Close time
#"2434.19055334",    #7 Quote asset volume
#308,                #8 Number of trades
#"1756.87402397",    #9 Taker buy base asset volume
#"28.46694368",      #10 Taker buy quote asset volume
#"17928899.62484339" #11 Can be ignored