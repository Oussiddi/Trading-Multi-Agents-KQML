from typing import List, Set, Dict, Optional
from agents.base_agent import BaseAgent
from communication.kqml import KQMLMessage, Performative
from data.market_data import MarketData
import pandas as pd
from datetime import datetime
from colorama import Fore, Style


class TradingAgent(BaseAgent):
    def __init__(self, name: str, capital: float):
        super().__init__(name)
        self.capital = capital
        self.positions = {}
        self._setup_handlers()
        
    def _setup_handlers(self):
        self.register_handler(Performative.TELL, self._handle_tell)
        
    def _handle_tell(self, message: KQMLMessage) -> Optional[KQMLMessage]:
        if 'price' in message.content:
            symbol = message.content.get('symbol', '')
            price = message.content.get('price', 0)
            if symbol and price:
                self._evaluate_position(symbol, price)
        return None
            
    def _evaluate_position(self, symbol: str, price: float):
        print(f"\n{Fore.YELLOW}[TRADE ANALYSIS] {symbol}")
        print(f"Current Price: ${price:.2f}")
        
        if symbol not in self.positions:
            cost = price * 100
            if self.capital > cost:
                print(f"BUY SIGNAL: Sufficient capital (${self.capital:.2f}) for 100 shares")
                self.positions[symbol] = {'shares': 100, 'price': price}
                self.capital -= cost
                print(f"[TRADE EXECUTED] Bought 100 shares of {symbol} at ${price:.2f}")
        else:
            current_position = self.positions[symbol]
            profit_pct = ((price - current_position['price']) / current_position['price']) * 100
            print(f"Position Analysis: {profit_pct:.2f}% profit/loss")
            
            if price > current_position['price'] * 1.02:
                profit = (price - current_position['price']) * current_position['shares']
                print(f"SELL SIGNAL: 2% profit target reached")
                self.capital += price * current_position['shares']
                del self.positions[symbol]
                print(f"[TRADE EXECUTED] Sold {current_position['shares']} shares at ${price:.2f} (Profit: ${profit:.2f})")