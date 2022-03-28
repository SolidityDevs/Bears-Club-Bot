
import cryptonator
from telegram import Update
from emoji import emojize
import locale

import humanize
from telegram.ext import Updater, CommandHandler, CallbackQueryHandler, CallbackContext, Filters

import re
from numerize import numerize
from telegram.ext import *
from telegram import *
from decimal import *
import requests
import json
from pricebot.ads import get_current_add as myads
from pycoingecko import CoinGeckoAPI

from telegram import Update
cg = CoinGeckoAPI()


response = requests.get("https://api.coingecko.com/api/v3/coins/list").json()
     


def cv3(context,chat_id,amount,coins):
    try:
        for coin in response:
            if coin['symbol'] == coins or coin['id'] == coins:
                cvs = coin['id']
                asp = cg.get_coin_by_id(id=cvs)
                id = asp['id']
                symbol = asp['symbol'].upper()
                curr1 = asp['market_data']['current_price']['usd']
                p = "{:,.8f}".format(float(curr1))
                price = float(curr1)
                amount_now = amount*price
                keke = amount
                ps = "{:,}".format(float(amount))
                amount_no = "{:,.8f}".format(float(amount_now))
                msgs = f'*🔹Calculating {ps} {symbol}*\n`1️⃣ {symbol} ~ ${p}\n🔹 {amount} `*{symbol}* `~ ${amount_no}`\n{myads()}'
                rkey = [[InlineKeyboardButton("Refresh 🔂", callback_data=f'calccg {cvs} {keke}')]]
                reply_mark = InlineKeyboardMarkup(rkey)
                context.bot.send_message(chat_id, msgs,reply_markup=reply_mark, parse_mode="Markdown",disable_web_page_preview=True)
                break
        else:
            try:
                mctu = cryptonator.get_exchange_rate(""+coins+"", "usd")
                amo = float(amount)*float(mctu)
                amount_no = "{:,.8f}".format(float(amo))
                amx = "{:,.8f}".format(float(mctu))
                amoun = "{:,.8f}".format(float(amount))
                rkey = [[InlineKeyboardButton("Refresh 🔂", callback_data=f'Reloads {cvs} {keke}')]]
                reply_mark = InlineKeyboardMarkup(rkey)
                msgs = f'*🔹Calculating {amoun} {coins.upper()}*\n`1️⃣ {coins.upper()} ~ ${amx}\n🔹 {amoun} `*{coins.upper()}* `~ ${amount_no}`\n{myads()}'
                context.bot.send_message(chat_id, msgs,reply_markup=reply_mark, parse_mode="Markdown",disable_web_page_preview=True)
                return
            except Exception:
                try:
                    vmc = requests.get("https://min-api.cryptocompare.com/data/price?fsym="+coins+"&tsyms=USD&api_key=96d339f34a488c0b83d9fc41f24369acf88a76ec5c074b396275819966e78f33").json()['USD']
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
                    cvbs = coins
                    msgf = f'*🔹Converted {amount} {coins}*\n`1️⃣ {coins} ~ ${no_pric}\n🔹{amount} `*{coins}* `~ ${calcus}`\n{myads()}'
                    rkeyss = [[InlineKeyboardButton("Refresh 🔂", callback_data=f'Reload {amount} {cvbs}')]]
                    reply_markss = InlineKeyboardMarkup(rkeyss)
                    context.bot.send_message(chat_id, msgf,reply_markup=reply_markss, parse_mode="Markdown",disable_web_page_preview=True)
                    return
                except Exception:
                    context.bot.send_message(chat_id,'No Data Available',parse_mode='markdown')
                    return
    except requests.exceptions.HTTPError:
        try:
            mctu = cryptonator.get_exchange_rate(""+coins+"", "usd")
            amo = float(amount)*float(mctu)
            amount_no = "{:,.8f}".format(float(amo))
            amx = "{:,.8f}".format(float(mctu))
            amoun = "{:,.8f}".format(float(amount))
            rkey = [[InlineKeyboardButton("Refresh 🔂", callback_data=f'Reloads {cvs} {keke}')]]
            reply_mark = InlineKeyboardMarkup(rkey)
            msgs = f'*🔹Calculating {amoun} {coins.upper()}*\n`1️⃣ {coins.upper()} ~ ${amx}\n🔹 {amoun} `*{coins.upper()}* `~ ${amount_no}`\n{myads()}'
            context.bot.send_message(chat_id, msgs,reply_markup=reply_mark, parse_mode="Markdown",disable_web_page_preview=True)
            return
        except Exception:
            try:
                vmc = requests.get("https://min-api.cryptocompare.com/data/price?fsym="+coins+"&tsyms=USD&api_key=96d339f34a488c0b83d9fc41f24369acf88a76ec5c074b396275819966e78f33").json()['USD']
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
                cvbs = coins
                msgf = f'*🔹Converted {amount} {coins}*\n`1️⃣ {coins} ~ ${no_pric}\n🔹{amount} `*{coins}* `~ ${calcus}`\n{myads()}'
                rkeyss = [[InlineKeyboardButton("Refresh 🔂", callback_data=f'Reload {amount} {cvbs}')]]
                reply_markss = InlineKeyboardMarkup(rkeyss)
                context.bot.send_message(chat_id, msgf,reply_markup=reply_markss, parse_mode="Markdown",disable_web_page_preview=True)
                return
            except Exception:
                context.bot.send_message(chat_id,'No Data Available',parse_mode='markdown')
                return
            