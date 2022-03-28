import requests
import json
from gase import get_gas_data


import requests
import json
from bs4 import BeautifulSoup
from requests import Session

import logging
import time
import os
import cloudscraper
from pycoingecko import CoinGeckoAPI

import datetime
import requests
import telegram

import re
from numerize import numerize
from telegram.ext import *
from telegram import *
from decimal import *


from pricebot.ads import get_current_add as myads
from telegram.ext.dispatcher import run_async

import cryptonator
from telegram import Update
from emoji import emojize
import locale
import humanize
from telegram.ext import Updater, CommandHandler, CallbackQueryHandler, CallbackContext, Filters

from telegram import Update
from telegram import InlineKeyboardButton, InlineKeyboardMarkup
from pricebot.pa import parse_api_coinmarketcapjson, parse_api_globalinfoapijson

from p import p1, p2
from calc import cv3
from cnv import cv4
cg = CoinGeckoAPI()




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

def price(update,context):
    text = update.message.text
    chat_id = update.effective_chat.id
    testy = text.split()
    if len(testy) == 2:
        coin = testy[1].lower()
        p1(context,chat_id,coin)
        return
    elif len(testy) >= 3:
        coin1 = testy[1].lower()
        coin2 = testy[2].lower()
        p2(context,chat_id,coin1,coin2)
        return
    else:
        melo = "Command Usage\n/p < coin symbol >\n/p <coin symbol> <currency>"
        context.bot.send_message(chat_id= chat_id,text = melo)
        return
        
        


def calculator(update,context) -> None:
    chat_id = update.effective_chat.id
    te = update.message.text.split()
    if len(te) == 2:
        ar = eval(context.args[0])
        if ar > 0.0001:
            ar = "{:,.7f}".format(float(ar))
        else:
            ar = "{:,.12f}".format(float(ar))
        context.bot.send_message(chat_id = chat_id,text= f"<b>{ar}</b>", parse_mode="html")
    elif len(te) ==3:
        coin = te[2]
        amount = te[1]
        try:
            bnv = float(amount)
            cv3(context,chat_id,bnv,coin.lower())
            return
        except ValueError:
            try:
                solo = float(coin)
                cv3(context,chat_id,solo,amount.lower())
                return
            except ValueError:
                context.bot.send_message(chat_id=chat_id,text="Command Usage\n/cnv 20 bnb")
                return
    elif len(te) == 4:
        coin1 = te[2].lower()
        coin2 = te[3].lower()
        amount = te[1]
        try:
            nn = float(amount)
            cv4(context,chat_id,nn,coin1,coin2)
        except ValueError:
            context.bot.send_message(chat_id=chat_id,text="Command Usage\n/cnv 200 bnb trx ")
            return
    else:
        context.bot.send_message(chat_id=chat_id,text="Command Usage\n/cnv 200 bnb trx ")
    
  

       
            
def refresh(update,context):
    query : CallbackQuery = update.callback_query
    chat_id = update.effective_chat.id
    ch = update.callback_query.data.split()
    if len(ch) ==1:
        if query.data == "Shortcodes":
            msgi = f'*Afrikaans af - Albanian sq - Amharic am - Arabic ar -\nArmenian hy - Azerbaijani az - Basque eu - Belarusian be\n -Bengali bn - Bosnian bs - Bulgarian bg - Catalan ca\nCebuano ceb - Chinese (Simplified) zh-CN or zh - Chinese (Traditional) zh-TW - Corsican co\nCroatian hr- Czech cs - Danish da - Dutch nl\nEnglish en - Esperanto eo - Estonian et - Finnish fi\nFrench fr - Frisian fy- Galician gl - Georgian ka\nGerman de - Greek el - Gujarati gu - Haitian Creole ht\nHausa ha - Hawaiian haw - Hebrew he or iw - Hindi hi\nHmong hmn - Hungarian hu - Icelandic is - Igbo ig\nIndonesian id - Irish ga - Italian it - Japanese ja\nJavanese jv - Kannada kn - Kazakh kk - Khmer km\nKinyarwanda rw - Korean ko - Kurdish ku - Kyrgyz ky\nLao lo - Latvian lv - Lithuanian lt - Luxembourgish lb\nMacedonian mk -Malagasy mg - Malay ms -Malayalam ml\nMaltese mt - Maori mi - Marathi mr - Mongolian mn\nMyanmar (Burmese) my - Nepali ne - Norwegian no - Nyanja (Chichewa) ny\nOdia (Oriya) or - Pashto ps - Persian fa - Polish pl\nPortuguese (Portugal, Brazil) pt - Punjabi pa - Romanian ro - Russian ru\nSamoan sm - Scots Gaelic gd - Serbian sr - Sesotho st\nShona sn - Sindhi sd - Sinhala (Sinhalese) si - Slovak sk\nSlovenian sl - Somali so - Spanish es - Sundanese su\nSwahili sw - Swedish sv - Tagalog (Filipino) tl - Tajik tg\nTamil ta - Tatar tt - Telugu te - Thai th\nTurkish tr - Turkmen tk - Ukrainian uk - Urdu ur\nUyghur ug - Uzbek uz - Vietnamese vi - Welsh cy\nXhosa xh - Yiddish yi - Yoruba yo - Zulu zu*\n{myads()}'
            query.edit_message_text(text=msgi,parse_mode='markdown',disable_web_page_preview=True)
        elif query.data == 'gas':
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
            mas = f"*Eth Gas Price:*\n🚲 *Safe*: `{gas_data['safe_gas']}gwei ${s}`\n🚜 *Average*: `{gas_data['propose_gas']}gwei ${av}`\n🚀 *Fast*: `{gas_data['fast_gas']}gwei ${fa}`\n{myads()}"
            kemap = [[InlineKeyboardButton("Refresh 🔂", callback_data=f'gas')]]
            rely_markto = InlineKeyboardMarkup(kemap)
            query.edit_message_text(text=mas,reply_markup=rely_markto,parse_mode='markdown',disable_web_page_preview=True)
    if len(ch) ==2:
        context.bot.answer_callback_query(callback_query_id=query.id, text='Refreshing Please Wait', show_alert=False)
        coin_id  = update.callback_query.data.split()[1] 
        usr_msg_text = update.callback_query.data.split()[1]
        
        if query.data == f'cmc {usr_msg_text}':
            usr_msg_text = usr_msg_text.upper()
            
            text_response = parse_api_coinmarketcapjson(usr_msg_text)
            kema = [[InlineKeyboardButton("Refresh 🔂", callback_data=f'cmc {usr_msg_text}')]]
            reply_maro = InlineKeyboardMarkup(kema)
            if text_response:
                query.edit_message_text(text = text_response,reply_markup=reply_maro, parse_mode="Markdown",disable_web_page_preview=True)
        if query.data == f"cg {coin_id}":
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
            query.edit_message_text(text=msg,reply_markup=reply_markto,parse_mode='markdown',disable_web_page_preview=True)      
    elif len(ch) == 3:
        context.bot.answer_callback_query(callback_query_id=query.id, text='Updating Please Wait', show_alert=False)
        coins_ids  = update.callback_query.data.split()[1] 
        curren = update.callback_query.data.split()[2]
        amount  = update.callback_query.data.split()[1] 
        ticker = update.callback_query.data.split()[2].lower()
        cvb = update.callback_query.data.split()[2]
        cvbs = update.callback_query.data.split()[2]
        amount  = update.callback_query.data.split()[1] 
        cvs = update.callback_query.data.split()[1]
        keke  = update.callback_query.data.split()[2]
        cvss = update.callback_query.data.split()[2]
        kekes  = update.callback_query.data.split()[1]
        if query.data == f'cg {coins_ids} {curren}':
            csst = cg.get_coins_markets(vs_currency=curren, ids=coins_ids,price_change_percentage='1h,24h,7d')
            names = csst[0]['id'].upper()
            symbols = csst[0]['symbol'].upper()
            prices = csst[0]['current_price']
            pms = '0.0000000'
            if prices == None:
                prices = float(pms)
            else:
                prices = float(prices)
            if prices > 0.001:
                prices = '{0:,.5f}'.format(float(prices))
            else:
                prices = '{0:,.8f}'.format(float(prices))
            highs = csst[0]['high_24h']
            if highs == None:
                highs = float(pms)
            else:
                highs = float(highs)
            if highs > 0.001:
                highs = '{0:,.4f}'.format(float(highs))
            else:
                highs = '{0:,.6f}'.format(float(highs))
            lows = csst[0]['low_24h']
            if lows == None:
                lows = float(pms)
            else:
                lows = float(lows)
            if lows > 0.001:
                lows = '{0:,.4f}'.format(float(lows))
            else:
                lows = '{0:,.6f}'.format(float(lows))
        
            rate1hs_float =csst[0]['price_change_percentage_1h_in_currency']
            tme = '0.000'
            if rate1hs_float == None:
                rate1hs_float = float(tme)
            else:
                rate1h_float = float(rate1hs_float)
            rate1hs_emoji = parse_price_change(rate1hs_float)
            rate1hs =csst[0]['price_change_percentage_1h_in_currency']
            if rate1hs == None:
                rate1hs = float(tme)
            else:
                rate1hs = '{0:,.2f}'.format(float(rate1hs))

                    # 24 hours price change with emoji
                
            rate24hs_float =csst[0]['price_change_percentage_24h_in_currency']
            if rate24hs_float == None:
                rate24hs_float = float(tme)
            else:
                rate24hs_float = float(rate24hs_float)
            rate24hs_emoji = parse_price_change(rate24hs_float)
            rate24hs =csst[0]['price_change_percentage_24h_in_currency']
            if rate24hs == None:
                rate24hs = float(tme)
            else:
                rate24hs = '{0:,.2f}'.format(float(rate24hs))

                    # 7 days price change with emoji
                
            rate7ds_float =csst[0]['price_change_percentage_7d_in_currency']
            if rate7ds_float == None:
                rate7ds_float = float(tme)
            else:
                rate7ds_float = float(rate7ds_float)
            rate7ds_emoji = parse_price_change(rate7ds_float)
            rate7ds =csst[0]['price_change_percentage_7d_in_currency']
            if rate7ds == None:
                rate7ds = float(tme)
            else:
                rate7ds = '{0:,.2f}'.format(float(rate7ds))
            ranks = csst[0]['market_cap_rank']
            rankss = humanize.ordinal(ranks)
            vols = "{:,}".format(int(csst[0]["total_volume"]))
            mcaps = "{:,}".format(int(csst[0]["market_cap"]))
            mnk = int(csst[0]["total_volume"])
            aka = numerize.numerize(mnk)
            mnb = int(csst[0]["market_cap"])
            aa = numerize.numerize(mnb)
            msgss = f"🔵 *{names} ({symbols})*\n" \
                   f"🍀 *Price:* `{prices} {curren.upper()}`\n\n" \
                   f"Ξ *24HR HIGH||LOW CHANGES*\n" \
                   f"🟢 *High:* {highs} {curren.upper()}\n" \
                   f"🔴 *Low:* {lows} {curren.upper()}\n\n" \
                   f"*PRICE CHANGES (%)*\n" \
                   f"▫️ *1H:*   {rate1hs}%  {rate1hs_emoji}\n" \
                   f"▫️ *24H:*  {rate24hs}%  {rate24hs_emoji}\n" \
                   f"▫️ *7D:*   {rate7ds}%  {rate7ds_emoji}\n\n" \
                   f"🏆 *Rank:* {rankss}\n" \
                   f"📊 *Vol:* ${aka} {curren.upper()}\n" \
                   f"⚜️ *Cap:* ${aa} {curren.upper()}\n" \
                   f"{myads()}"
            keys = [[InlineKeyboardButton("Refresh 🔂", callback_data=f'cg {coins_ids} {curren}')]]
            reply_marks = InlineKeyboardMarkup(keys)
            query.edit_message_text(text=msgss,reply_markup=reply_marks,parse_mode='markdown',disable_web_page_preview=True)
        
            
        if query.data == f'calccg {amount} {cvb}':
            asp = cg.get_coin_by_id(id=cvb)
            id = asp['id']
            symbol = asp['symbol'].upper()
            curr1 = asp['market_data']['current_price']['usd']
            p = "{:,.8f}".format(float(curr1))
            price = float(curr1)
            amount_now = float(amount)*price
            amount_no = "{:,.8f}".format(float(amount_now))
            msgo = f'*🔹Calculating {amount} {symbol}*\n`1️⃣ {symbol} ~ ${p}\n🔹 {amount} `*{symbol}* `~ ${amount_no}`\n{myads()}'
            rkey = [[InlineKeyboardButton("Refresh 🔂", callback_data=f'calccg {amount} {cvb}')]]
            reply_mark = InlineKeyboardMarkup(rkey)
            query.edit_message_text(text=msgo,reply_markup=reply_mark,parse_mode='markdown',disable_web_page_preview=True)
            
        if query.data == f'Reload {amount} {cvbs}':
            vmc = requests.get("https://min-api.cryptocompare.com/data/price?fsym="+cvbs+"&tsyms=USD&api_key=96d339f34a488c0b83d9fc41f24369acf88a76ec5c074b396275819966e78f33").json()['USD']
            no_pric = float(vmc)
            if no_pric > 0.0001:
                no_pric = "{:,.4f}".format(float(no_pric))
            else:
                no_pric = "{:,.8f}".format(float(no_pric))
            calcus = float(vmc)*float(amount)
            if calcus > 0.0001:
                calcus = "{:,.4f}".format(float(calcus))
            else:
                calcus = "{:,.8f}".format(float(calcus))
            msgf = f'*🔹Converted {amount} {cvbs}*\n`1️⃣ {cvbs} ~ ${no_pric}\n🔹{amount} `*{cvbs}* `~ ${calcus}`\n{myads()}'
            rkeyss = [[InlineKeyboardButton("Refresh 🔂", callback_data=f'Reload {amount} {cvbs}')]]
            reply_markss = InlineKeyboardMarkup(rkeyss)
            query.edit_message_text(msgf,reply_markup=reply_markss,parse_mode='markdown',disable_web_page_preview=True)
            
        if query.data == f'Reloads {cvs} {keke}':
            mctu = cryptonator.get_exchange_rate(""+keke+"", "usd")
            amo = float(cvbs)*float(mctu)
            amount_no = "{:,.8f}".format(float(amo))
            amx = "{:,.8f}".format(float(mctu))
            amoun = "{:,.8f}".format(float(amount))
            rkey = [[InlineKeyboardButton("Refresh 🔂", callback_data=f'Reloads {cvs} {keke}')]]
            reply_mark = InlineKeyboardMarkup(rkey)
            msgo = f'*🔹Calculating {cvs} {keke}*\n`1️⃣ {keke} ~ ${amx}\n🔹{cvs} `*{keke}* `~ ${amount_no}`\n{myads()}'
            
            query.edit_message_text(text=msgo,reply_markup=reply_mark,parse_mode='markdown',disable_web_page_preview=True)
            
        
                
    elif len(ch) == 4:
        context.bot.answer_callback_query(callback_query_id=query.id, text='Reloading Please Wait 📚', show_alert=False)
        te  = update.callback_query.data.split()
        amount = te[1]
        num = amount
        ticker = te[2]
        target = te[3]
        cvb = te[2].lower()
        taa = target.upper()
        tis = ticker.upper()
        if query.data == f'Updatecg {amount} {ticker} {target}':
            asp = cg.get_coin_by_id(id=cvb)
            id = asp['id']
            symbol = asp['symbol'].upper()
            curr1 = asp['market_data']['current_price'][''+target+'']
            p = "{:,.8f}".format(float(curr1))
            price = float(curr1)
            amount_now = num*price
            amount_no = "{:,.8f}".format(float(amount_now))
            msg = f'*🔹Converting {amount} {symbol} - {target.upper()}*\n`1️⃣{symbol} ~ {p} {target.upper()}\n🔹{amount} `*{symbol}* `~ {amount_no} {target.upper()}`\n{myads()}'
            rkey = [[InlineKeyboardButton("Refresh 🔂", callback_data=f'Updatecg {amount} {cvb} {target}')]]
            reply_mark = InlineKeyboardMarkup(rkey)
            query.edit_message_text(text=msg,reply_markup=reply_mark,parse_mode='markdown',disable_web_page_preview=True)
        if query.data == f"Updatecn {amount} {ticker} {target}":
            cvc = cryptonator.get_exchange_rate(ticker, target)
            bcv = "{:,.8f}".format(float(cvc))
            bn = float(cvc)*float(num)
            bcvc = "{:,.8f}".format(float(bn))
            msg = f'*🔹Calculating {amount} {ticker.upper()} - {target.upper()}*\n`1️⃣{ticker.upper()} ~ {bcv} {target.upper()}\n🔹{amount} `*{ticker.upper()}* `~ {bcvc} {target.upper()}`\n{myads()}'
            rkeys = [[InlineKeyboardButton("Refresh 🔂", callback_data=f'Updatecn {amount} {ticker} {target}')]]
            reply_marks = InlineKeyboardMarkup(rkeys)
            query.edit_message_text(text=msg,reply_markup=reply_marks,parse_mode='markdown',disable_web_page_preview=True)
        if query.data == f"Updatecc {amount} {ticker} {target}":
            vm = requests.get("https://min-api.cryptocompare.com/data/price?fsym="+tis+"&tsyms="+taa+"&api_key=96d339f34a488c0b83d9fc41f24369acf88a76ec5c074b396275819966e78f33").json()[''+taa+'']
            now_price = "{:,.8f}".format(float(vm))
            calcu = float(vm)*float(num)
            now_fm = "{:,.8f}".format(float(calcu))
            msgf = f'*🔹Converted {amount} {ticker.upper()} - {target.upper()}*\n`1️⃣{ticker.upper()} ~ {now_price} {target.upper()}\n🔹{amount} `*{ticker.upper()}* `~ {now_fm} {target.upper()}`\n{myads()}'
            rkeyss = [[InlineKeyboardButton("Refresh 🔂", callback_data=f'Updatecc {amount} {ticker} {target}')]]
            reply_markss = InlineKeyboardMarkup(rkeyss)
            query.edit_message_text(text=msgf,reply_markup=reply_markss,parse_mode='markdown',disable_web_page_preview=True)
        
