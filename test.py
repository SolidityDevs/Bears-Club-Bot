from pycoingecko import CoinGeckoAPI

import requests
import json
import os

import telegram
import _thread as thread
import os


import time
from telegram.ext import *
from telegram import *

cg = CoinGeckoAPI()
coin_list = requests.get("https://api.coingecko.com/api/v3/coins/list").json()

MAX_ALERT_LIMIT = 10000
alerts_count = 0
def get_prices(coin):
    cc = cg.get_coins_markets(vs_currency='usd', ids=coin.lower())
    cr = cc[0]['current_price']
    data = {
        "ticker": coin,
        "price": cr
    }
    
    
    
    return data

def thread_poller(chat_id,context,alert):
    # Time in seconds to delay thread
    global alerts_count
    DELAY = 30
    while True:
        
        coin,isAbove,threshold_price = alert
        data = get_prices(coin)
        currentPrice = float(data["price"]) #
        currently = data['price']
        if currently > 0.001:
                currently = '{0:,.2f}'.format(float(currently))
        else:
            currently = '{0:,.3f}'.format(float(currently))
        target = threshold_price
        if target> 0.001:
                target= '{0:,.2f}'.format(float(target))
        else:
            target= '{0:,.3f}'.format(float(target))
        if isAbove:
            if currentPrice > threshold_price:
                message = f"📊 *Alert*\n`{data['ticker'].upper()}  is above ${target}\nCurrent price: ${currently}\nAlert has been removed`"
                context.bot.send_message(chat_id=chat_id,text=message,parse_mode='markdown')
                alerts_count -= 1
                break
        elif currentPrice < threshold_price:
            message = f"📊 *Alert*\n`{data['ticker'].upper()}  is below ${target}\nCurrent price: ${currently}\nAlert has been removed`"
            context.bot.send_message(chat_id=chat_id,text=message,parse_mode='markdown')
            alerts_count -= 1
            break

        time.sleep(DELAY)
        
        
def alert(update,context):
    global alerts_count
    chat_id = update.effective_chat.id
    text = update.message.text.split()
    if len(text) <= 3:
        update.message.reply_text('`Usage: /alert btc > 50000`',parse_mode='markdown')
    elif len(text) >= 5:
        update.message.reply_text('`Usage: /alert btc > 50000`',parse_mode='markdown')
    else:
        try:
            if text[2] == ">":
                isAbove = True
            elif text[2] == "<":
                isAbove = False
            else:
                raise ValueError
        
            threshold_price = float(text[3])
            coinss = text[1].lower()
            for coin in coin_list:
                if coin['symbol'] == coinss or coin['id'] == coinss:
                    coin_id = coin['id']
                    datss = cg.get_coins_markets(vs_currency='usd', ids=coin_id)
                    dats = datss[0]['current_price']
                    currp = float(dats)
                    curr = '{0:,.3f}'.format(float(currp))
                
                    targ = text[3]
                    tar = '{0:,.2f}'.format(float(targ))
            
                    token = text[1].upper()

                    alert=(coin_id.lower(),isAbove,threshold_price)
                    if alerts_count + 1 < MAX_ALERT_LIMIT:
                        alerts_count += 1
                        msg = f'✅ `Alert set for:\n{token} at ${tar}\nCurrent Price: ${curr} `'
                        context.bot.send_message(chat_id= chat_id, text=msg,parse_mode='markdown')
                        thread.start_new_thread(thread_poller,(chat_id,context,alert))
                        break
                    else:
                        context.bot.send_message(chat_id= chat_id, text= "`Please try again later`",parse_mode='markdown')
        except Exception as e:
            print(e)
            context.bot.send_message(chat_id=chat_id,text="`Invalid input\n/alert btc > 1500`",parse_mode='markdown')
