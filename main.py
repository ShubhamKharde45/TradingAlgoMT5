
import MetaTrader5 as mt5
import pandas as pd
from dotenv import load_dotenv
import os
from datetime import datetime
import plotly.express as px 
import ta

load_dotenv()
def initialize_MT5():
    login = int(os.getenv('MT5_LOGIN'))
    password = os.getenv('MT5_PASSWORD')
    server = os.getenv('MT5_SERVER')

    if not mt5.initialize(path="C:\\Program Files\\MetaTrader 5\\terminal64.exe"):
        print("initialize() failed, error code:", mt5.last_error())

    if not mt5.login(login, password, server):
        print("Connection failed")

initialize_MT5()

def get_rsi(symbol):

    rsi_period = 14
    rates = mt5.copy_rates_from_pos(symbol, mt5.TIMEFRAME_M1, 0, 100)

    df = pd.DataFrame(rates)
    df['rsi'] = ta.momentum.RSIIndicator(close=df['close'], window=rsi_period).rsi()
    return df['rsi'].iloc[-1]
        

def main_signal():
    i = 0
    while i < 10:
        rsi = get_rsi('BTCUSDm')
        if rsi>70:
            print("Selling Zone")
        elif rsi<70:
            print("Buying Zone")
        else:
            print("RSI IS IN NEUTRAL RANGE")
        print("*" * 10)
        i += 1
main_signal()
        
mt5.shutdown()