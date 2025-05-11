
import MetaTrader5 as mt5
import pandas as pd
from dotenv import load_dotenv
import os
from datetime import datetime
import plotly.express as px 

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


def print_chart_symbol(symbol : str):
    tick_data = pd.DataFrame(mt5.copy_rates_range(symbol, mt5.TIMEFRAME_D1, datetime(2025, 5, 11), datetime.now()))
    
    fig = px.line(tick_data, x=tick_data['time'], y=tick_data['close'])
    # fig.show()
    print(tick_data)

print_chart_symbol('BTCUSDm')
mt5.shutdown()