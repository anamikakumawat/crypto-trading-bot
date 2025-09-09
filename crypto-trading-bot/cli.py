from bot import BasicBot

def main():
    print("🚀 Welcome to Crypto Trading Bot (Binance Testnet) 🚀")

    api_key = input("Enter your API Key: ")
    api_secret = input("Enter your API Secret: ")

    bot = BasicBot(api_key, api_secret)

    while True:
        print("\nOptions:")
        print("1. Place Market Order")
        print("2. Place Limit Order")
        print("3. Place Stop-Limit Order (Bonus)")
        print("4. Check Order Status")
        print("5. Exit")

        choice = input("Select option: ")

        if choice == "1":
            symbol = input("Symbol (e.g. BTCUSDT): ")
            side = input("Buy/Sell: ")
            qty = float(input("Quantity: "))
            print(bot.place_market_order(symbol, side, qty))

        elif choice == "2":
            symbol = input("Symbol (e.g. BTCUSDT): ")
            side = input("Buy/Sell: ")
            qty = float(input("Quantity: "))
            price = input("Price: ")
            print(bot.place_limit_order(symbol, side, qty, price))

        elif choice == "3":
            symbol = input("Symbol (e.g. BTCUSDT): ")
            side = input("Buy/Sell: ")
            qty = float(input("Quantity: "))
            stop_price = input("Stop Price: ")
            limit_price = input("Limit Price: ")
            print(bot.place_stop_limit_order(symbol, side, qty, stop_price, limit_price))

        elif choice == "4":
            symbol = input("Symbol: ")
            order_id = int(input("Order ID: "))
            print(bot.get_order_status(symbol, order_id))

        elif choice == "5":
            print("Exiting bot... Goodbye!")
            break

if __name__ == "__main__":
    main()
