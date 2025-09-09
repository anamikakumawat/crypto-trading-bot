from binance.client import Client
from binance.enums import *
import logging

class BasicBot:
    def __init__(self, api_key, api_secret, testnet=True):
        self.client = Client(api_key, api_secret, testnet=testnet)
        logging.basicConfig(
            level=logging.INFO,
            filename="bot.log",
            format="%(asctime)s - %(levelname)s - %(message)s"
        )

    def place_market_order(self, symbol, side, quantity):
        try:
            order = self.client.futures_create_order(
                symbol=symbol,
                side=SIDE_BUY if side.lower() == "buy" else SIDE_SELL,
                type=ORDER_TYPE_MARKET,
                quantity=quantity
            )
            logging.info(f"Market order placed: {order}")
            return order
        except Exception as e:
            logging.error(f"Error placing market order: {e}")
            return None

    def place_limit_order(self, symbol, side, quantity, price):
        try:
            order = self.client.futures_create_order(
                symbol=symbol,
                side=SIDE_BUY if side.lower() == "buy" else SIDE_SELL,
                type=ORDER_TYPE_LIMIT,
                timeInForce=TIME_IN_FORCE_GTC,
                quantity=quantity,
                price=price
            )
            logging.info(f"Limit order placed: {order}")
            return order
        except Exception as e:
            logging.error(f"Error placing limit order: {e}")
            return None

    def place_stop_limit_order(self, symbol, side, quantity, stop_price, limit_price):
        try:
            order = self.client.futures_create_order(
                symbol=symbol,
                side=SIDE_BUY if side.lower() == "buy" else SIDE_SELL,
                type=ORDER_TYPE_STOP_MARKET,
                quantity=quantity,
                stopPrice=stop_price
            )
            logging.info(f"Stop-Limit order placed: {order}")
            return order
        except Exception as e:
            logging.error(f"Error placing stop-limit order: {e}")
            return None

    def get_order_status(self, symbol, order_id):
        try:
            status = self.client.futures_get_order(symbol=symbol, orderId=order_id)
            logging.info(f"Order status: {status}")
            return status
        except Exception as e:
            logging.error(f"Error fetching order status: {e}")
            return None
