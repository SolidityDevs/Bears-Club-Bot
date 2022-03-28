import cloudscraper
import cryptonator
import datetime

import requests
import telegram
import re

from numerize import numerize
from telegram.ext import *
from telegram import *


import json
import time
import telegram

from bs4 import BeautifulSoup
from requests import Session
import logging

import os
from decimal import *


scraper = cloudscraper.create_scraper()

def pcs(update,context):
    text = update.message.text
    chat_id = update.effective_chat.id
    testy = text.split()
    if len(testy) == 2:
        ca = testy[1]
        dates = "%Y-%m-%d %H:%M:%S"
        query = """
        query
        {
          ethereum(network: bsc) {
            dexTrades(
            exchangeName: {in:["Pancake","Pancake v2"]},
            baseCurrency: {is: "%s"}
            quoteCurrency: {is: "0xbb4cdb9cbd36b01bd1cbaebf2de08d9173bc095c"}
            options: {desc: ["block.height", "transaction.index"], limit: 1}
            ) {
            block {
                height
                timestamp {
                time(format: "%s")
                }
            }
            transaction {
                index
            }
            baseCurrency {
                symbol
            }
            quoteCurrency {
                symbol
            }
            quotePrice
           }
          }
        }
        """ % (ca, dates)

        d = {'query': query, 'variables': {}}
        payload = json.dumps(d)
        url = "https://graphql.bitquery.io"
        headers = {
            'X-API-KEY': 'BQYxBh0DXYCwroM9PKnGS2tZXWDZhNEx',
            'Content-Type': 'application/json'
        }
        di = requests.request("POST", url, headers=headers, data=payload).json()['data']['ethereum']['dexTrades']
         # Price of coin in BNB
        price = di[0]['quotePrice']
        # Coin Symbol
        symbol = di[0]['baseCurrency']['symbol']
        # Quoting and cut out some zero from price bnb
        price_bnb = '{0:.9f}'.format(float(price))
        # Getting current price of bnb
        bnb = cryptonator.get_exchange_rate("bnb", "usd")
    
        # Geting price of coin in usd
        p_usd = '{0:.15f}'.format(float(price))
        pr_usd = float(p_usd)*float(bnb)
        pr = pr_usd
        if pr > 0.01:
            pr = '{0:,.6f}'.format(float(pr))
        else:
            pr = '{0:,.9f}'.format(float(pr))
    #------------------------------------
    #------------------------------------
    #Now let's scrap some data from bscscan.com webpage
        headers = {'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.9; rv:32.0) Gecko/20100101 Firefox/32.0'}
        URL = f"https://bscscan.com/token/{ca}"
        cotractpage = requests.get(URL,headers=headers)
        soupa = BeautifulSoup(cotractpage.content, 'lxml')
    #Getting token holders for the contract provided
        tokenholders = soupa.find(id='ContentPlaceHolder1_tr_tokenHolders').get_text()
        tokenholdersa = "Holders ➜ " + ((((tokenholders.strip()).strip("Holders:")).strip()).strip(" a ")).strip()
    #Now let's grt the coin name from bscscan.com
        name = soupa.find('span', class_='text-secondary small').get_text()
    #Getting total supply of the coin
        total_supply = soupa.find('div', class_='col-md-8').get_text().split('(')[0].strip()   # <--- we want only first part of the string
    #now let get only digits/interger from the strings
        result = ''.join([i for i in total_supply if  i.isdigit()])
        supply_now = numerize.numerize(float(int(result)))
    #--------------------------------------------------
    #--------------------------------------------------
    #Now bscscan done let's calculate the marketcap
        mc = float(pr_usd)*float(result)
        mcap = "${:,.4f}".format(float(mc))
    # MCap to bnb
        mctu = cryptonator.get_exchange_rate("usd", "bnb")
        mc_bn = float(mctu)*float(mc)
        mcap_bnb = numerize.numerize(float(int(mc_bn)))
    #---------------------------------------
    #Getting all data ready for printing
        bsss = "${:,.4f}".format(float(bnb))
        all_msg = f"<b>{name} ({symbol})</b>\n" \
                  f"1 <b>{symbol}</b> ➜ $<b>{pr}</b>\n" \
                  f"1 <b>{symbol}</b> ➜ <b>{price_bnb} BNB</b>\n" \
                  f"<b>BNB Price</b> ➜ <b>{bsss}</b>\n" \
                  f"---------------------------------------------\n" \
                  f"---------------------------------------------\n" \
                  f"<b>Total Supply</b> ➜ <b>{supply_now} {symbol}</b>\n" \
                  f"<b>{tokenholdersa}</b>\n" \
                  f"<b>MC ➜ {mcap} ({mcap_bnb}) BNB</b>\n" \
                  f"<a href='https://t.me/Amadevs'>Need custom bots?</a>"
        rkey = [[InlineKeyboardButton("Chart", url=f'https://poocoin.app/tokens/{ca}'),InlineKeyboardButton("Buy",url=f"https://poocoin.app/swap/?outputCurrency={ca}")]]
        reply_mark = InlineKeyboardMarkup(rkey)
        context.bot.send_message(chat_id=chat_id,text=all_msg,parse_mode='html',reply_markup=reply_mark,disable_web_page_preview=True)
    else:
        context.bot.send_message(chat_id=chat_id,text="Usage: /pcs < Contract Address >\n/pcs 0xa.......",parse_mode='markdown')
  

       
