from dataclasses import dataclass
from enum import Enum
from typing import Dict, Any, Optional, List, Set


class Performative(Enum):
    ASK = 'ask'
    TELL = 'tell'
    ACHIEVE = 'achieve'
    SUBSCRIBE = 'subscribe'
    REPLY = 'reply'

@dataclass
class KQMLMessage:
    performative: Performative
    sender: str
    receiver: str
    content: Dict[str, Any]
    reply_with: str = ''
    in_reply_to: str = ''