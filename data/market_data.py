import yfinance as yf
import pandas as pd
import numpy as np
from datetime import datetime, timedelta
from typing import Dict, Optional

class MarketData:
    def __init__(self, symbols: list):
        self.symbols = symbols
        self.data = {}
        
    def fetch_data(self, period="1d", interval="1m"):
        for symbol in self.symbols:
            ticker = yf.Ticker(symbol)
            self.data[symbol] = ticker.history(period=period, interval=interval)
        return self.data

    def get_latest_price(self, symbol: str) -> float:
        return self.data[symbol]['Close'].iloc[-1]