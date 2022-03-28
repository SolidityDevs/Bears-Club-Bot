import cryptonator
from telegram import Update
from emoji import emojize
import locale
from pycoingecko import CoinGeckoAPI

import humanize
from telegram.ext import Updater, CommandHandler, CallbackQueryHandler, CallbackContext, Filters
import requests
import json
import re
from numerize import numerize
from telegram.ext import *
from telegram import *
from decimal import *

from pricebot.ads import get_current_add as myads
from telegram import Update
cg = CoinGeckoAPI()


response = requests.get("https://api.coingecko.com/api/v3/coins/list").json()

def cv4(context,chat_id,amount,coin1,coin2):
    try:
        for coin in response:
            if coin['symbol'] == coin1 or coin['id']==coin1:
                cvb = coin['id']
                asp = cg.get_coin_by_id(id=cvb)
                id = asp['id']
                symbol = asp['symbol'].upper()
                try:
                    curr1 = asp['market_data']['current_price'][''+coin2+'']
                    p = "{:,.8f}".format(float(curr1))
                    price = float(curr1)
                    amount_now = amount*price
                    amount_no = "{:,.8f}".format(float(amount_now))
                    msg = f'*🔹Converting {amount} {symbol} - {coin2.upper()}*\n`1️⃣{symbol} ~ {p} {coin2.upper()}\n🔹{amount} `*{symbol}* `~ {amount_no} {coin2.upper()}`\n{myads()}'
                    rkey = [[InlineKeyboardButton("Refresh 🔂", callback_data=f'Updatecg {amount} {cvb} {coin2}')]]
                    reply_mark = InlineKeyboardMarkup(rkey)
                    context.bot.send_message(chat_id,msg,reply_markup=reply_mark,parse_mode='markdown',disable_web_page_preview=True)
                    break
                except KeyError:
                    try:
                        cvc = cryptonator.get_exchange_rate(coin1, coin2)
                        bcv = "{:,.8f}".format(float(cvc))
                        bn = float(cvc)*float(amount)
                        bcvc = "{:,.8f}".format(float(bn))
                        msg = f'*🔹Calculating {amount} {coin1.upper()} - {coin2.upper()}*\n`1️⃣{coin1.upper()} ~ {bcv} {coin2.upper()}\n🔹{amount} `*{coin1.upper()}* `~ {bcvc} {coin2.upper()}`\n{myads()}'
                        rkeys = [[InlineKeyboardButton("Refresh 🔂", callback_data=f'Updatecn {amount} {coin1} {coin2}')]]
                        reply_marks = InlineKeyboardMarkup(rkeys)
                        context.bot.send_message(chat_id,msg,reply_markup=reply_marks,parse_mode='markdown',disable_web_page_preview=True)
                        return
                    except Exception:
                        try:
                            vm = requests.get("https://min-api.cryptocompare.com/data/price?fsym="+coin1+"&tsyms="+coin2.upper()+"&api_key=96d339f34a488c0b83d9fc41f24369acf88a76ec5c074b396275819966e78f33").json()[''+coin2.upper()+'']
                            now_price = "{:,.8f}".format(float(vm))
                            calcu = float(vm)*float(amount)
                            now_fm = "{:,.8f}".format(float(calcu))
                            msgf = f'*🔹Converted {amount} {coin1.upper()} - {coin2.upper()}*\n`1️⃣{coin1.upper()} ~ {now_price} {coin2.upper()}\n🔹{amount} `*{coin1.upper()}* `~ {now_fm} {coin2.upper()}`\n{myads()}'
                            rkeyss = [[InlineKeyboardButton("Refresh 🔂", callback_data=f'Updatecc {amount} {coin1} {coin2}')]]
                            reply_markss = InlineKeyboardMarkup(rkeyss)
                            context.bot.send_message(chat_id,msgf,reply_markup=reply_markss,parse_mode='markdown',disable_web_page_preview=True)
                            return
                        except Exception:
                            context.bot.send_message(chat_id,'`coin1 not found`',parse_mode='markdown')
                            return
        else:
            try:
                cvc = cryptonator.get_exchange_rate(coin1, coin2)
                bcv = "{:,.8f}".format(float(cvc))
                bn = float(cvc)*float(amount)
                bcvc = "{:,.8f}".format(float(bn))
                msg = f'*🔹Calculating {amount} {coin1.upper()} - {coin2.upper()}*\n`1️⃣{coin1.upper()} ~ {bcv} {coin2.upper()}\n🔹{amount} `*{coin1.upper()}* `~ {bcvc} {coin2.upper()}`\n{myads()}'
                rkeys = [[InlineKeyboardButton("Refresh 🔂", callback_data=f'Updatecn {amount} {coin1} {coin2}')]]
                reply_marks = InlineKeyboardMarkup(rkeys)
                context.bot.send_message(chat_id,msg,reply_markup=reply_marks,parse_mode='markdown',disable_web_page_preview=True)
                return
            except Exception:
                try:
                    vm = requests.get("https://min-api.cryptocompare.com/data/price?fsym="+coin1.upper()+"&tsyms="+coin2.upper()+"&api_key=96d339f34a488c0b83d9fc41f24369acf88a76ec5c074b396275819966e78f33").json()[''+coin2.upper()+'']
                    now_price = "{:,.8f}".format(float(vm))
                    calcu = float(vm)*float(amount)
                    now_fm = "{:,.8f}".format(float(calcu))
                    msgf = f'*🔹Converted {amount} {coin1.upper()} - {coin2.upper()}*\n`1️⃣{coin1.upper()} ~ {now_price} {coin2.upper()}\n🔹{amount} `*{coin1.upper()}* `~ {now_fm} {coin2.upper()}`\n{myads()}'
                    rkeyss = [[InlineKeyboardButton("Refresh 🔂", callback_data=f'Updatecc {amount} {coin1} {coin2}')]]
                    reply_markss = InlineKeyboardMarkup(rkeyss)
                    context.bot.send_message(chat_id,msgf,reply_markup=reply_markss,parse_mode='markdown',disable_web_page_preview=True)
                    return
                except Exception:
                    context.bot.send_message(chat_id,'`Ticker not found`',parse_mode='markdown')
                    return
    except requests.exceptions.HTTPError:
        try:
            cvc = cryptonator.get_exchange_rate(coin1, coin2)
            bcv = "{:,.8f}".format(float(cvc))
            bn = float(cvc)*float(amount)
            bcvc = "{:,.8f}".format(float(bn))
            msg = f'*🔹Calculating {amount} {coin1.upper()} - {coin2.upper()}*\n`1️⃣{coin1.upper()} ~ {bcv} {coin2.upper()}\n🔹{amount} `*{coin1.upper()}* `~ {bcvc} {coin2.upper()}`\n{myads()}'
            rkeys = [[InlineKeyboardButton("Refresh 🔂", callback_data=f'Updatecn {amount} {coin1} {coin2}')]]
            reply_marks = InlineKeyboardMarkup(rkeys)
            context.bot.send_message(chat_id,msg,reply_markup=reply_marks,parse_mode='markdown',disable_web_page_preview=True)
            return
        except Exception:
            try:
                vm = requests.get("https://min-api.cryptocompare.com/data/price?fsym="+coin1.upper()+"&tsyms="+coin2.upper()+"&api_key=96d339f34a488c0b83d9fc41f24369acf88a76ec5c074b396275819966e78f33").json()[''+coin2.upper()+'']
                now_price = "{:,.8f}".format(float(vm))
                calcu = float(vm)*float(amount)
                now_fm = "{:,.8f}".format(float(calcu))
                msgf = f'*🔹Converted {amount} {coin1.upper()} - {coin2.upper()}*\n`1️⃣{coin1.upper()} ~ {now_price} {coin2.upper()}\n🔹{amount} `*{coin1.upper()}* `~ {now_fm} {coin2.upper()}`\n{myads()}'
                rkeyss = [[InlineKeyboardButton("Refresh 🔂", callback_data=f'Updatecc {amount} {coin1} {coin2}')]]
                reply_markss = InlineKeyboardMarkup(rkeyss)
                context.bot.send_message(chat_id,msgf,reply_markup=reply_markss,parse_mode='markdown',disable_web_page_preview=True)
                return
            except Exception:
                context.bot.send_message(chat_id,'`Ticker not found`',parse_mode='markdown')
                return