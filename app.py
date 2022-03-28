import requests
from telegram.ext import Updater
from telegram.ext import CommandHandler
from telegram import InlineKeyboardButton, InlineKeyboardMarkup, Update
from telegram.ext import Updater, CommandHandler, CallbackQueryHandler, CallbackContext, Filters

from pricebot.handlers import start, help,list,broadcast,add_users
from pricebot.config import TOKEN_BOT
#from moregads.commands import graph,price

from pricebot.parse_apis import cap,ico
from pricebot.cryptoapi import balance

from pcs import pcs

from meme import meme
from quotes import quote_message
from pricebot.ads import see_all_adds, new_ad,del_ad,get_current_add
from track import top
from trending import send_trending
from gase import get_gas_data,defi,send_market,send_ath,finance_platforms,send_coin_social,send_atl,joke,fng
from list import new_listing
from candle import candle
from simplecc import cc

from menu import menu
from info import info
from txn import details
from test import alert as blow
from testedbit import trans
from news import news
from pycoingecko import CoinGeckoAPI
#from busy import price as prix,refresh
from price import price,refresh,calculator
from cmc import  download_api_coinslists_handler, download_api_global_handler
from telegram.ext import *
from telegram import *

cg = CoinGeckoAPI()
from requests.exceptions import RequestException




TIME_INTERVAL = 3600

def gas(update, context):
    print("Request received: Ethereum gas price")
    # Make API call to get Ethereum gas data.
    gas_data = get_gas_data()
    coin_info = cg.get_coins_markets(vs_currency='usd', ids='ethereum')
    cu = float(coin_info[0]['current_price'])
    safe = float(gas_data['safe_gas'])/21000
    sa = safe*cu/2
    s  = '{0:,.0f}'.format(float(sa))
    aver = float(gas_data['propose_gas'])/21000
    ave = aver*cu/2
    av  = '{0:,.0f}'.format(float(ave))
    fast = float(gas_data['fast_gas'])/21000
    fas = fast*cu/2
    fa  = '{0:,.0f}'.format(float(fas))
    mas = f"*Eth Gas Price:*\n🚲 *Safe*: `{gas_data['safe_gas']}gwei ${s}`\n🚜 *Average*: `{gas_data['propose_gas']}gwei ${av}`\n🚀 *Fast*: `{gas_data['fast_gas']}gwei ${fa}`\n{get_current_add()}"
    keymap = [[InlineKeyboardButton("Refresh 🔂", callback_data=f'gas')]]
    reply_markto = InlineKeyboardMarkup(keymap)
    update.message.reply_text(mas,reply_markup=reply_markto,parse_mode='markdown',disable_web_page_preview=True)
def main():
    

    # create an object "bot"
    updater = Updater(token="5164891388:AAHPUnJkVIwo9ELCcntgxr73krhxTx2jsq4", use_context=True)
    dispatcher = updater.dispatcher
    dp = updater.dispatcher

    # bot's error handler
   

    # bot's command handlers
    
    start_handler = CommandHandler('start', start)
    dispatcher.add_handler(start_handler)
    
    help_handler = CommandHandler('help', help)
    dispatcher.add_handler(help_handler)

    cap_handler = CommandHandler('cap', cap)
    dispatcher.add_handler(cap_handler)
    
    b_handler = CommandHandler('b', balance)
    dispatcher.add_handler(b_handler)
    
    dispatcher.add_handler(CommandHandler("top", top))
    dispatcher.add_handler(CommandHandler("joke", joke))
    dispatcher.add_handler(CommandHandler("cv", calculator))
    dispatcher.add_handler(CommandHandler("new_ad", new_ad, pass_args=True, pass_user_data=True))
    dispatcher.add_handler(CommandHandler("del_ad", del_ad, pass_args=True, pass_user_data=True))
    dispatcher.add_handler(CommandHandler("get_ads", see_all_adds))
    dispatcher.add_handler(CommandHandler("tr", send_trending))
    dispatcher.add_handler(CommandHandler('trending', send_trending))
    dispatcher.add_handler(CommandHandler("gas", gas))
    dispatcher.add_handler(CommandHandler("defi", defi))
    dispatcher.add_handler(CommandHandler("market", send_market))
    dispatcher.add_handler(CommandHandler('ath', send_ath))
    dispatcher.add_handler(CommandHandler('ico', ico))
    dispatcher.add_handler(CommandHandler('meme', meme))
    updater.dispatcher.add_handler(CommandHandler('finance', finance_platforms))
    updater.dispatcher.add_handler(CommandHandler('social', send_coin_social))
    updater.dispatcher.add_handler(CommandHandler('atl', send_atl))
    dispatcher.add_handler(CommandHandler('quote', quote_message))
    dispatcher.add_handler(CommandHandler('listing', new_listing))
    dispatcher.add_handler(CommandHandler('c', candle))
    updater.dispatcher.add_handler(CommandHandler('info', info))
    updater.dispatcher.add_handler(CommandHandler('fng', fng))
    updater.dispatcher.add_handler(CommandHandler('tx', details))
    updater.dispatcher.add_handler(CommandHandler('cc', cc))
    updater.dispatcher.add_handler(CommandHandler('alert', blow))
    updater.dispatcher.add_handler(CommandHandler('balance', balance))
    updater.dispatcher.add_handler(CommandHandler('news', news))
    updater.dispatcher.add_handler(CommandHandler('menu', menu))
   
    updater.dispatcher.add_handler(CallbackQueryHandler(refresh))
    
    dispatcher.add_handler(CommandHandler("conv", calculator))
    dispatcher.add_handler(CommandHandler("convert", calculator))
    dispatcher.add_handler(CommandHandler("cnv", calculator))
    dispatcher.add_handler(CommandHandler("calc", calculator))
    dispatcher.add_handler(CommandHandler("trans", trans))
    #dispatcher.add_handler(CommandHandler("price", priced))
    dispatcher.add_handler(CommandHandler("p", price))
    updater.dispatcher.add_handler(CommandHandler('broadcast', broadcast))
    #updater.dispatcher.add_handler(CommandHandler('start', start))
    updater.dispatcher.add_handler(CommandHandler('add', add_users))
    updater.dispatcher.add_handler(CommandHandler('list', list))
    updater.dispatcher.add_handler(CommandHandler('pcs', pcs))
    
    
   
   
    job_queue = updater.job_queue
    job_queue.run_repeating(download_api_global_handler, TIME_INTERVAL, 5)
    job_queue.run_repeating(download_api_coinslists_handler, TIME_INTERVAL, 10, context='coinmarketcap')
   
    updater.start_polling()
    updater.idle()



if __name__ == '__main__':
    main()
