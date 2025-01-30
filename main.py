from datetime import datetime
import time
import colorama
from colorama import Fore, Style
from agents.market_agent import MarketAgent
from agents.trading_agent import TradingAgent
from communication.kqml import KQMLMessage, Performative
import logging

colorama.init()

def setup_logging():
    logging.basicConfig(level=logging.INFO)

def log_message(message: KQMLMessage, direction: str):
    timestamp = datetime.now().strftime("%H:%M:%S")
    
    if direction == "SENT":
        color = Fore.GREEN
    else:
        color = Fore.BLUE
        
    print(f"\n{color}[{timestamp}] {direction} Message:")
    print(f"From: {message.sender} → To: {message.receiver}")
    print(f"Type: {message.performative}")
    print(f"Content: {message.content}")
    print(f"{Style.RESET_ALL}")

def main():
    symbols = ['AAPL', 'GOOGL', 'MSFT']
    market_agent = MarketAgent("market", symbols)
    trading_agent = TradingAgent("trader", 100000)
    
    while True:
        try:
            print("\nEnter 'f' to fetch new data, 'q' to quit:")
            command = input()
            
            if command.lower() == 'f':
                print(f"\n{Fore.CYAN}[{datetime.now().strftime('%H:%M:%S')}] Fetching market data...{Style.RESET_ALL}")
                market_agent.market_data.fetch_data()
                
                for symbol in symbols:
                    price_request = KQMLMessage(
                        performative=Performative.ASK,
                        sender=trading_agent.name,
                        receiver=market_agent.name,
                        content={'price': True, 'symbol': symbol}
                    )
                    print(f"\n{Fore.GREEN}ASK: {trading_agent.name} requesting {symbol} price{Style.RESET_ALL}")
                    response = market_agent.handle_message(price_request)
                    if response:
                        print(f"{Fore.BLUE}TELL: {market_agent.name} responding with price: {response.content}{Style.RESET_ALL}")
                        trading_agent.handle_message(response)
                
                print("\nCurrent Portfolio:")
                print(f"Cash: ${trading_agent.capital:,.2f}")
                for sym, pos in trading_agent.positions.items():
                    print(f"Position {sym}: {pos['shares']} shares @ ${pos['price']:.2f}")
                    
            elif command.lower() == 'q':
                break
                
        except Exception as e:
            print(f"Error: {e}")

if __name__ == "__main__":
    main()