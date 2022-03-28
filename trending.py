from coingecko import CoinGecko
import requests
import json

from pricebot.ads import get_current_add as myads
from telegram.ext.dispatcher import run_async
from telegram import Update
from telegram.ext import Updater, CommandHandler, CallbackQueryHandler, CallbackContext, Filters
from pricebot.ads import get_current_add as myads


run_async
def send_trending(update, context) -> None:
    """Replies to command with trending crypto coins
    Args:
        message (Message): Message to reply to
    """
    #logger.info("Retrieving trending addresses from CoinGecko")
    coin_gecko = CoinGecko()
    coin_gecko_trending_coins = "\n\n".join(
        f"{coin['item']['name']} ({coin['item']['symbol']})"
        for coin in coin_gecko.get_trending_coins()
    )

    
    reply = (
        f"*Top 7 Trending on Coingecko*\n`{coin_gecko_trending_coins} `\n\n{myads()}"
    )

    update.effective_message.reply_text(reply,parse_mode='markdown',disable_web_page_preview=True)
