
import cryptonator
from telegram import Update
from emoji import emojize
import locale
from pycoingecko import CoinGeckoAPI
import humanize
from telegram.ext import Updater, CommandHandler, CallbackQueryHandler, CallbackContext, Filters

import re
import json
from numerize import numerize
from telegram.ext import *
from telegram import *
from decimal import *
from pricebot.ads import get_current_add as myads
import requests

from telegram import Update
cg = CoinGeckoAPI()



response = requests.get("https://api.coingecko.com/api/v3/coins/list").json()


def parse_price_change(percent):
    emoji = ''

    if percent > 1 and percent <= 3.0:
        emoji = emojize(' :new_moon_face:', use_aliases=True)
        
    elif percent >= 3 and percent <= 5.0:
        emoji = emojize(' :partying_face:', use_aliases=True)
        
    elif percent >= 5 and percent <= 11.0:
        emoji = emojize(':slightly_smiling_face:', use_aliases=True)
        
    elif percent >= 11 and percent <= 16.0:
        emoji = emojize(' :bear:', use_aliases=True)
        
    elif percent >= 16 and percent <= 20.0:
        emoji = emojize(' :rocket:', use_aliases=True)
        
    elif percent >= 20 and percent <= 50.0:
        emoji = emojize(' :full_moon_face:', use_aliases=True)
        
    elif percent >= 50 and percent <= 100.0:
        emoji = emojize(' :joy:', use_aliases=True)
        
    elif percent > 100:
        emoji = emojize(' :fire:', use_aliases=True)
        
    elif percent > 0.1 and percent <= 1:
        emoji = emojize(' :wink:', use_aliases=True)
        
    elif percent >= 0 and percent <= 0.1:
        emoji = emojize(' :smirk:', use_aliases=True)
        
    elif percent <= -1 and percent <= -2:
        emoji = emojize(' :weary_face:', use_aliases=True)
        
    elif percent <= -2 and percent <= -3:
        emoji = emojize(' :white_frowning_face:', use_aliases=True)
        
    elif percent <= -3 and percent <= -4:
        emoji = emojize(' :grimacing_face:', use_aliases=True)
        
    elif percent <= -4 and percent <= -5:
        emoji = emojize(' :unamused_face:', use_aliases=True)
        
    elif percent <= -5 and percent <= -6:
        emoji = emojize(' :sneezing_face:', use_aliases=True)
        
    elif percent <= -6 and percent <= -7:
        emoji = emojize(' :small_red_triangle_down:', use_aliases=True)
        
    elif percent <= -7 and percent <= -8:
        emoji = emojize(' :frowning:', use_aliases=True)
        
    elif percent <= -8 and percent <= -9:
        emoji = emojize(' :hushed:', use_aliases=True)
        
    elif percent <= -9 and percent <= -10:
        emoji = emojize(' :sleepy_face:', use_aliases=True)
        
    elif percent <= -10 and percent <= -13:
        emoji = emojize(' :face_with_thermometer:', use_aliases=True)
        
    elif percent <= -13 and percent <= -15:
        emoji = emojize(' :drooling_face:', use_aliases=True)
        
    elif percent <= -15 and percent <= -20:
        emoji = emojize(' :zipper__mouth_face:', use_aliases=True)
        
    elif percent <= -20 and percent <= -100:
        emoji = emojize(' :sweat_drops:', use_aliases=True)
        
    elif percent <= -100:
        emoji = emojize(' :red_triangle_pointed_down:', use_aliases=True)
        
    elif percent < -0:
        emoji = emojize(' :fearful_face:', use_aliases=True)
    

    return emoji



def p1(context,chat_id,coin):
    try:
        for c in response:
            if c['symbol'] == coin or c['id']== coin:
                    coin_id = c['id']
                    ds = cg.get_coins_markets(vs_currency='usd', ids=coin_id,price_change_percentage='1h,24h,7d')
                    name = ds[0]['id'].upper()
                    symbol = ds[0]['symbol'].upper()
                    price = ds[0]['current_price']
                    pms = '0.0000000'
                    if price == None:
                        price = float(pms)
                    else:
                        price = float(price)
                    if price > 0.001:
                        price = '{0:,.5f}'.format(float(price))
                    else:
                        price = '{0:,.8f}'.format(float(price))
                    high = ds[0]['high_24h']
                    if high == None:
                        high = float(pms)
                    else:
                        high = float(high)
                    if high > 0.001:
                        high = '{0:,.4f}'.format(float(high))
                    else:
                        high = '{0:,.6f}'.format(float(high))
                    low = ds[0]['low_24h']
                    if low == None:
                        low = float(pms)
                    else:
                        low = float(low)
                    if low > 0.001:
                        low = '{0:,.4f}'.format(float(low))
                    else:
                        low = '{0:,.6f}'.format(float(low))
                    rate1h_float = ds[0]['price_change_percentage_1h_in_currency']
                    tme = '0.000'
                    if rate1h_float == None:
                        rate1h_float = float(tme)
                    else:
                        rate1h_float = float(rate1h_float)
                    rate1h_emoji = parse_price_change(rate1h_float)
                    rate1h = ds[0]['price_change_percentage_1h_in_currency']
                    if rate1h == None:
                        rate1h = float(tme)
                    else:
                        rate1h = '{0:,.2f}'.format(float(rate1h))

                # 24 hours price change with emoji
                
                    rate24h_float = ds[0]['price_change_percentage_24h_in_currency']
                    if rate24h_float == None:
                        rate24h_float = float(tme)
                    else:
                        rate24h_float = float(rate24h_float)
                    rate24h_emoji = parse_price_change(rate24h_float)
                    rate24h = ds[0]['price_change_percentage_24h_in_currency']
                    if rate24h == None:
                        rate24h = float(tme)
                    else:
                        rate24h = '{0:,.2f}'.format(float(rate24h))

                # 7 days price change with emoji
                
                    rate7d_float = ds[0]['price_change_percentage_7d_in_currency']
                    if rate7d_float == None:
                        rate7d_float = float(tme)
                    else:
                        rate7d_float = float(rate7d_float)
                    rate7d_emoji = parse_price_change(rate7d_float)
                    rate7d = ds[0]['price_change_percentage_7d_in_currency']
                    if rate7d == None:
                        rate7d = float(tme)
                    else:
                        rate7d = '{0:,.2f}'.format(float(rate7d))
                    rank = ds[0]['market_cap_rank']
                    
                    ranks = humanize.ordinal(rank)
                    vol = "${:,}".format(int(ds[0]["total_volume"]))
                    vbv = int(ds[0]["total_volume"])
                    a = numerize.numerize(vbv)
                    mcap = "${:,}".format(int(ds[0]["market_cap"]))
                    mnb = int(ds[0]["market_cap"])
                    aa = numerize.numerize(mnb)
                    msg = f"🔵 *{name} ({symbol})*\n" \
                          f"🍀 *Price:* `${price}`\n\n" \
                          f"*Ξ 24HRS HIGH||LOW CHANGES*\n" \
                          f"🟢 *High:* `${high}`\n" \
                          f"🔴 *Low:* `${low}`\n\n" \
                          f"*PRICE CHANGES (%)*\n" \
                          f"▫️ *1H:*  `{rate1h}%`  {rate1h_emoji}\n" \
                          f"▫️ *24H:* `{rate24h}%`  {rate24h_emoji}\n" \
                          f"▫️ *7D:*  `{rate7d}%`  {rate7d_emoji}\n\n" \
                          f"🏆 *Rank:* {ranks}\n" \
                          f"📊 *Vol:* `${a}`\n" \
                          f"⚜️ *Cap:* `${aa}`\n" \
                          f"{myads()}"
                    keymap = [[InlineKeyboardButton("Refresh 🔂", callback_data=f'cg {coin_id}')]]
                    reply_markto = InlineKeyboardMarkup(keymap)
                    context.bot.send_message(chat_id = chat_id,text =  msg,reply_markup=reply_markto, parse_mode="Markdown",disable_web_page_preview=True)
                    break
        else:
            usr_msg_text = user_input.upper()
            text_response = parse_api_coinmarketcapjson(usr_msg_text)
            kemap = [[InlineKeyboardButton("Refresh 🔂", callback_data=f'cmc {usr_msg_text}')]]
            reply_maro = InlineKeyboardMarkup(kemap)
            if text_response:
                context.bot.send_message(chat_id = chat_id,text = text_response,reply_markup=reply_maro, parse_mode="Markdown",disable_web_page_preview=True)
    except requests.exceptions.HTTPError:
        usr_msg_text = user_input.upper()
        text_response = parse_api_coinmarketcapjson(usr_msg_text)
        kemap = [[InlineKeyboardButton("Refresh 🔂", callback_data=f'cmc {usr_msg_text}')]]
        reply_maro = InlineKeyboardMarkup(kemap)
        if text_response:
            context.bot.send_message(chat_id, text_response,reply_markup=reply_maro, parse_mode="Markdown",disable_web_page_preview=True)
            
            

def p2(context,chat_id,coin1,coin2):
    try:
        for coins in response:
            if coins['symbol'] == coin1 or coins['id'] == coin1:
                coins_ids = coins['id']
                try:
                    dss = cg.get_coins_markets(vs_currency=coin2, ids=coins_ids,price_change_percentage='1h,24h,7d')
                    names = dss[0]['id'].upper()
                    symbols = dss[0]['symbol'].upper()
                    prices = dss[0]['current_price']
                    pms = '0.0000000'
                    if prices == None:
                        prices = float(pms)
                    else:
                        prices = float(prices)
                    if prices > 0.001:
                        prices = '{0:,.5f}'.format(float(prices))
                    else:
                        prices = '{0:,.8f}'.format(float(prices))
                    highs = dss[0]['high_24h']
                    if highs == None:
                        highs = float(pms)
                    else:
                        highs = float(highs)
                    if highs > 0.001:
                        highs = '{0:,.4f}'.format(float(highs))
                    else:
                        highs = '{0:,.6f}'.format(float(highs))
                    lows = dss[0]['low_24h']
                    if lows == None:
                        lows = float(pms)
                    else:
                        lows = float(lows)
                    if lows > 0.001:
                        lows = '{0:,.4f}'.format(float(lows))
                    else:
                        lows = '{0:,.6f}'.format(float(lows))
        
                    rate1hs_float =dss[0]['price_change_percentage_1h_in_currency']
                    tme = '0.000'
                    if rate1hs_float == None:
                        rate1hs_float = float(tme)
                    else:
                        rate1h_float = float(rate1hs_float)
                    rate1hs_emoji = parse_price_change(rate1hs_float)
                    rate1hs =dss[0]['price_change_percentage_1h_in_currency']
                    if rate1hs == None:
                        rate1hs = float(tme)
                    else:
                        rate1hs = '{0:,.2f}'.format(float(rate1hs))

                    # 24 hours price change with emoji
                
                    rate24hs_float =dss[0]['price_change_percentage_24h_in_currency']
                    if rate24hs_float == None:
                        rate24hs_float = float(tme)
                    else:
                        rate24hs_float = float(rate24hs_float)
                    rate24hs_emoji = parse_price_change(rate24hs_float)
                    rate24hs =dss[0]['price_change_percentage_24h_in_currency']
                    if rate24hs == None:
                        rate24hs = float(tme)
                    else:
                        rate24hs = '{0:,.2f}'.format(float(rate24hs))

                    # 7 days price change with emoji
                
                    rate7ds_float =dss[0]['price_change_percentage_7d_in_currency']
                    if rate7ds_float == None:
                        ate7ds_float = float(tme)
                    else:
                        rate7ds_float = float(rate7ds_float)
                    rate7ds_emoji = parse_price_change(rate7ds_float)
                    rate7ds =dss[0]['price_change_percentage_7d_in_currency']
                    if rate7ds == None:
                        rate7ds = float(tme)
                    else:
                        rate7ds = '{0:,.2f}'.format(float(rate7ds))
                    ranks = dss[0]['market_cap_rank']
                    rankss = humanize.ordinal(ranks)
                    vols = "{:,}".format(int(dss[0]["total_volume"]))
                    vbc = int(dss[0]["total_volume"])
                    aav = numerize.numerize(vbc)
                    mcaps = "{:,}".format(int(dss[0]["market_cap"]))
                    mcs = int(dss[0]["market_cap"])
                    aa = numerize.numerize(mcs)
                    curren = coin2
                    
                    #aam = numerize.numerize(mcaps)
                    msgs = f"🔵 *{names} ({symbols})*\n" \
                           f"🍀 *Price:* `{prices} {coin2.upper()}`\n\n" \
                           f"Ξ *24HR HIGH||LOW CHANGES*\n" \
                           f"🟢 *High:* {highs} {coin2.upper()}\n" \
                           f"🔴 *Low:* {lows} {coin2.upper()}\n\n" \
                           f"*PRICE CHANGES (%)*\n" \
                           f"▫️ *1H:*   {rate1hs}%  {rate1hs_emoji}\n" \
                           f"▫️ *24H:*  {rate24hs}%  {rate24hs_emoji}\n" \
                           f"▫️ *7D:*   {rate7ds}%  {rate7ds_emoji}\n\n" \
                           f"🏆 *Rank:* {rankss}\n" \
                           f"📊 *Vol:* ${aav} {coin2.upper()}\n" \
                           f"⚜️ *Cap:* ${aa} {coin2.upper()}\n" \
                           f"{myads()}"
                    key = [[InlineKeyboardButton("Refresh 🔂", callback_data=f'cg {coins_ids} {curren}')]]
                    reply_mark = InlineKeyboardMarkup(key)
                    context.bot.send_message(chat_id = chat_id,text = msgs,reply_markup=reply_mark, parse_mode="Markdown",disable_web_page_preview=True)
                    break
                except ValueError:
                    context.bot.send_message(chat_id= chat_id,text = "Quote Currency Not Found")
                    return
                    
        else:
            context.bot.send_message(chat_id= chat_id,text = "Base Currency Not Found")
    except requests.exceptions.HTTPError:
        context.bot.send_message(chat_id= chat_id,text = "Api Response (-10%)\nTRY LATER")
 