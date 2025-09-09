import logging

def setup_logging():
    logging.basicConfig(
        level=logging.INFO,
        filename="bot.log",
        format="%(asctime)s - %(levelname)s - %(message)s"
    )
