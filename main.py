import logging
import ccxt
import config.secrets as secrets

from core.exchange import CryptoExchange
from core.telegrambot import TelegramBot
from core.tradeexcutor import TradeExecutor

if __name__ == '__main__':
    logging.basicConfig(format='%(asctime)s - %(levelname)s - %(message)s', level=logging.INFO)

    ccxt_ex = ccxt.binance({
        'apiKey': secrets.BINANCE_API_KEY,
        'secret': secrets.BINANCE_SECRET_KEY
    })

    exchange = CryptoExchange(ccxt_ex)
    trade_executor = TradeExecutor(exchange)
    telegram_bot = TelegramBot(secrets.TELEGRAM_TOKEN, secrets.TELEGRAM_USER_ID, trade_executor)

    telegram_bot.start_bot()
