import requests
import json

import datetime
import time
from matplotlib.dates import date2num
import datetime
import os
import matplotlib

from matplotlib import pyplot
from matplotlib.dates import date2num
from pricebot.ads import get_current_add as myads

from matplotlib import ticker
import matplotlib.dates as mdates
from mplfinance.original_flavor import candlestick_ohlc
from time import sleep
from random import random
import telegram
from telegram import bot,ChatAction



def get_history(coin,interval=None, limit=None, aggregate=3):
    interval_string = 'histominute'
    base = "https://min-api.cryptocompare.com/data/{}?fsym={}&tsym=USD&limit={}&aggregate={}&e=CCCAGG"
    string = base.format(interval_string, coin.upper(), limit, aggregate)
    response = requests.get(string).json()
    return response



def build_graph(ohlc, title=''):
    pyplot.style.use('fivethirtyeight')
    fig = pyplot.figure()
    ax1 = fig.add_subplot(111)
     
    for i in ohlc:
        i['time'] = date2num(datetime.datetime.fromtimestamp(i['time']))
    candel_width = (2/3) * (ohlc[1]['time'] - ohlc[0]['time'])
    data = []
    for i in ohlc:
        sub_lst = i['time'], i['open'], i['high'], i['low'], i['close']
        data.append(sub_lst)
    candlestick_ohlc(ax1, data, width=candel_width, colorup='g', colordown='r')
    ax1.xaxis.set_major_formatter(mdates.DateFormatter('%d-%m %H:%M'))
    ax1.xaxis.set_major_locator(ticker.MaxNLocator(10))
    ax1.grid(True)
    ty = ax1.text(0.5, 0.5, 'CoinTendBot', horizontalalignment='center',
         verticalalignment='center', transform=ax1.transAxes,color='blue',fontsize=45,rotation=45)
    ty.set_alpha(.3)
    ax1.set_xlabel('Date')
    ax1.set_ylabel('Price')
    ax1.set_title(title)
    ax1.autoscale_view()
    fig.tight_layout()
    fig.autofmt_xdate()
    #pyplot.show()  # no need to call show on server
    savefig='phto.png'
    polo = fig.savefig(savefig)
    pyplot.close()  # important to free memory
    
    return polo

def cc(update,context):
    chat_id = update.effective_chat.id
    toke = update.message.text.split()
    if len(toke) <=1:
        update.message.reply_text('`Usage: /cc btc`',parse_mode='markdown')
    else:
        coin = toke[1]
        interval = '1d'
        limit = 600
        interval_string = 'minute'
        aggregate = 10
        response = get_history(coin,aggregate=aggregate, limit=limit, interval=interval_string)
        if 'Response' in response and response['Response'] == 'Error': 
            text = "<b>Error!</b>"
            text += "\n{}".format(response['Message']) if 'Message' in response else ''
            print(text)
            update.message.reply_text('`Data not found`',parse_mode='markdown')
   
        data = response['Data']
        cut_data = []
        for i in data:
            if interval == '1d' and i['time'] < (time.time() - 60*60*24):  # stats blocked 1 day
                continue
            if interval == '1w' and i['time'] < (time.time() - 60*60*24*7):  # stats blocked 1w
                continue
            cut_data.append(i)
        caption = "{} - USD. Time : 24hrs".format(coin.upper())
        pic = build_graph(cut_data, title=caption)
        
        filename = 'phto.png' 
        context.bot.send_chat_action(chat_id=update.message.chat_id , 
                action = telegram.ChatAction.UPLOAD_PHOTO)
        sleep(random() * 1 + 1.)
        context.bot.send_photo(chat_id=chat_id, photo=open(filename,'rb'),caption= myads(),parse_mode='markdown')
        os.remove(filename)
    
