
from typing import Optional, Dict, Callable
from communication.kqml import KQMLMessage, Performative
from abc import ABC, abstractmethod

class BaseAgent:
    def __init__(self, name: str):
        self.name = name
        self._message_handlers = {}
        
    def handle_message(self, message: KQMLMessage) -> Optional[KQMLMessage]:
        handler = self._message_handlers.get(message.performative)
        return handler(message) if handler else None
        
    def register_handler(self, performative: Performative, handler):
        self._message_handlers[performative] = handler