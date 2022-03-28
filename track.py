import requests
import telegram
import _thread as thread
import os
import time
from telegram.ext import *
from telegram import *
from tacker import get_top_coins
from pricebot.ads import get_current_add as myads


def top(update,context):
    chat_id = update.effective_chat.id

    try:
        coins = get_top_coins(10)
        message = ""
        for coin in coins:
            message +=  f"`Top 10 Crypto:\n{coin['name']}  {coin['ticker']}\nPrice: {coin['price']}\nH|L: {coin['day_high']}|{coin['day_low']}\nVol 24h: {coin['volume_day']}\nCap: {coin['market_cap']}\n\n`"
            msd = f'{myads()}'
        context.bot.send_message(chat_id=chat_id,text='' + message +'\n' + msd + '',parse_mode='markdownv2',disable_web_page_preview=True)
    except Exception as e:
        context.bot.send_message(chat_id=chat_id,text="Some error occured 🐸")