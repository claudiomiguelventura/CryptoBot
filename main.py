"""CryptoBot first file"""
# Python and API modules import
from binance.client import Client


# Own modules import
import binance_keychain


# Creating a client instance
client = Client(binance_keychain.api_key, binance_keychain.api_secret)
print(client)

#Ping the server
print(client.ping())
#Get the server time
time_res = client.get_server_time()
print(time_res)
#Get system status
status = client.get_system_status()
print(status)
#Get Exchange Info
info_exchange = client.get_exchange_info()
print(info_exchange)
#Get Symbol Info
#Get the exchange info for a particular symbol
info_MDA = client.get_symbol_info('MDABTC')
print(info_MDA)
#Get Current Products
#This call is deprecated, use the above Exchange Info call
products = client.get_products()
print(products)