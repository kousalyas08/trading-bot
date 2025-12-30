from binance import Client
from binance.exceptions import BinanceAPIException
from logger import logger
import config

class BasicBot:
    def __init__(self, api_key, api_secret):
        self.client = Client(api_key, api_secret)
        self.client.FUTURES_URL = "https://testnet.binancefuture.com"
       
       #part-2

    def market_order(self, symbol, side, quantity):
        try:
            order = self.client.futures_create_order(
                symbol=symbol,
                side=side,
                type="MARKET",
                quantity=quantity
            )
            logger.info(order)
            print("Market order successful")
            print(order)
        except BinanceAPIException as e:
            logger.error(e)
            print("Error:", e)

            #part-3


    def limit_order(self, symbol, side, quantity, price):
        try:
            order = self.client.futures_create_order(
                symbol=symbol,
                side=side,
                type="LIMIT",
                quantity=quantity,
                price=price,
                timeInForce="GTC"
            )
            logger.info(order)
            print("Limit order placed")
            print(order)
        except BinanceAPIException as e:
            logger.error(e)
            print("Error:", e)


            #part-4


def main():
        bot = BasicBot(config.API_KEY, config.API_SECRET)

        print("=== Binance Futures Testnet Bot ===")

        symbol = input("Symbol (BTCUSDT): ").upper()
        side = input("BUY or SELL: ").upper()
        order_type = input("market / limit: ").lower()
        quantity = float(input("Quantity: "))

        if order_type == "market":
          bot.market_order(symbol, side, quantity)

        elif order_type == "limit":
          price = float(input("Price: "))
          bot.limit_order(symbol, side, quantity, price)

        else:
           print("Invalid order type")

if __name__ == "__main__":
        main()



