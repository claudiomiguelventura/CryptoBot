"""CryptoBot first file"""
# Python and API modules import
from binance.client import Client


# Own modules import
import binance_keychain


# Creating a client instance
client = Client(binance_keychain.api_key, binance_keychain.api_secret)
print(client)

client.ping()
#Get the server time
time_res = client.get_server_time()
print(time_res)
#Get system status
status = client.get_system_status()
print(status)
