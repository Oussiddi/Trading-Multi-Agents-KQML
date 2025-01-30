from typing import List, Set, Dict, Optional
from agents.base_agent import BaseAgent
from communication.kqml import KQMLMessage, Performative
from data.market_data import MarketData
import pandas as pd
from datetime import datetime

class MarketAgent(BaseAgent):
    def __init__(self, name: str, symbols: list):
        super().__init__(name)
        self.market_data = MarketData(symbols)
        self.subscribers = set()
        self._setup_handlers()
        
    def _setup_handlers(self):
        self.register_handler(Performative.SUBSCRIBE, self._handle_subscribe)
        self.register_handler(Performative.ASK, self._handle_ask)
        
    def _handle_subscribe(self, message: KQMLMessage) -> KQMLMessage:
        self.subscribers.add(message.sender)
        return KQMLMessage(
            performative=Performative.TELL,
            sender=self.name,
            receiver=message.sender,
            content={'status': 'subscribed'},
            in_reply_to=message.reply_with
        )
        
    def _handle_ask(self, message: KQMLMessage) -> KQMLMessage:
        symbol = message.content.get('symbol', '')
        if symbol:
            price = self.market_data.get_latest_price(symbol)
            return KQMLMessage(
                performative=Performative.TELL,
                sender=self.name,
                receiver=message.sender,
                content={
                    'price': price,
                    'symbol': symbol
                },
                in_reply_to=message.reply_with
            )
        return None