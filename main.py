"""CryptoBot first file"""
# Python and API modules import
from binance.client import Client
import time

# Own modules import
import binance_keychain

def server_time_to_local_time(servertime):
  return time.ctime(servertime/1000)

def current_time():
  print("Current %s time: %s"%(timezone,server_time_to_local_time(server_time)))
  return info_exchange.get('serverTime')

def trade_session_status(open_time,close_time):
  percentage_completed=(current_time()*100)/close_time
  time_remaining=close_time - current_time()
  print("The current session started at "+str(server_time_to_local_time(open_time)))
  print("Is "+percentage_completed+'%'+" completed")
  print("There are %d seconds remaining until close."%(time_remaining/1000))
  return percentage_completed

# Creating a client instance
client = Client(binance_keychain.api_key, binance_keychain.api_secret)
print(client)

#Get Exchange Info
info_exchange = client.get_exchange_info()
timezone = info_exchange.get('timezone')
server_time = info_exchange.get('serverTime')


#Ping the server
#print(client.ping())

#Get the server time
#epoch_seconds = client.get_server_time().get('serverTime')
#print("Server Time since epoch: "+str(epoch_seconds))
#local_time = time.ctime(epoch_seconds)
#print("Local time is: "+local_time)

        
#Get system status
#status = client.get_system_status()
#print(status)



#Get Symbol Info
#Get the exchange info for a particular symbol
#info_MDA = client.get_symbol_info('MDABTC')
#print(info_MDA)

#Get Current Products
#This call is deprecated, use the above Exchange Info call
#products = client.get_products()
#print(products)

#Get Kline/Candlesticks
candles = client.get_klines(symbol='MDABTC', interval=Client.KLINE_INTERVAL_30MINUTE)
last_open_time=candles[0]
last_open=candles[1]
last_high=candles[2]
last_low=candles[3]
last_close=candles[4]
last_volume=candles[5]
last_close_time=candles[6]

trade_session_status(last_open_time,last_close_time)


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