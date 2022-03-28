from pycoingecko import CoinGeckoAPI
import requests
import json
from telegram import Update
from telegram.ext import Updater, CommandHandler, CallbackQueryHandler, CallbackContext, Filters

cg = CoinGeckoAPI()

coin_list = requests.get("https://api.coingecko.com/api/v3/coins/list").json()

def info(update,context):
    test = update.message.text.split()
    if len(test) == 2:
        ticker = test[1].lower()
        for coin in coin_list:
            if coin['symbol'] == ticker or coin['id'] == ticker:
                coin_id = coin['id']
                co = cg.get_coin_by_id(id=coin_id)
                na = co['name'].upper()
                ti = co['symbol'].upper()
                des = co['description']['en']
                ms = f'<code>{na} ({ti})\n{des}</code>'
                update.effective_message.reply_text(ms,parse_mode='html')
                break
        else:
            update.effective_message.reply_text('`data not found`',parse_mode='markdown',disable_web_page_preview=True)
            
    else:
        update.effective_message.reply_text('`Usage: /info btc`',parse_mode='markdown')
