import logging
import time
import os
import cloudscraper
import json
import datetime
import requests
import telegram
import json

from telegram.ext import Updater, CommandHandler

# Enable logging
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO)

logger = logging.getLogger(__name__)
current_ad_idx = 0

ADS_FILE_NAME = 'ads.json'


def get_ads():
    try:
        file = open(ADS_FILE_NAME, 'r')
        #
        ads = json.load(fp=file)
        #
        file.close()

        return ads

    except:
        print("error opening ads.json")

        return {"count": 0, "list": []}


def update_ads(ad_to_add):
    updated_ads = get_ads()

    file = open(ADS_FILE_NAME, 'w')

    updated_ads['list'].append(ad_to_add)
    updated_ads['count'] = len(updated_ads['list'])

    json.dump(updated_ads, file)

    file.close()


def remove_ad(ad_id):
    ads = get_ads()

    file = open(ADS_FILE_NAME, 'w')

    del ads['list'][ad_id]
    ads['count'] = len(ads['list'])

    json.dump(ads, file)

    file.close()


def get_change(current, previous):
    if current == previous:
        return 0
    try:
        return (abs(current - previous) / previous) * 100.0
    except ZeroDivisionError:
        return float('inf')
    

def new_ad(update, context):
    ad = ' '.join(context.args)

    if update.message.from_user.username in ["AmaDevs", "CoinTendAdmin"]:
        update_ads(ad)
        update.message.reply_text(text='New Ads Added 😜.', parse_mode=telegram.ParseMode.HTML)
    else:
        update.message.reply_text(text='Story 😪.', parse_mode=telegram.ParseMode.HTML)


def del_ad(update, context):
    if len(context.args) < 1:
        return

    ad_id = int(context.args[0])

    if update.message.from_user.username in ['CoinTendAdmin', 'AmaDevs']:
        remove_ad(ad_id)
        update.message.reply_text(text='Removed that ads 😃.', parse_mode=telegram.ParseMode.HTML)
    else:
        update.message.reply_text(text='Error 😪.', parse_mode=telegram.ParseMode.HTML)


def see_all_adds(update, context):
    ads = get_ads()

    ads_list = ads['list']

    response = f'Number of ads: <b> {ads["count"]} </b> \n\n'

    idx = 0
    for ad in ads_list:
        response += f"<b>{idx}</b>: {ad}"
        response += '\n\n'
        idx+=1
    if update.message.from_user.username in ['CoinTendAdmin', 'AmaDevs']:
        update.message.reply_text(text=response, parse_mode=telegram.ParseMode.HTML, disable_web_page_preview=True)
        
    else:
        update.message.reply_text(text='Error 😪.', parse_mode=telegram.ParseMode.HTML)


def get_current_add():
    global current_ad_idx

    ads = get_ads()

    if ads['count'] == 0:
        return

    current_add = ads['list'][current_ad_idx]
    current_ad_idx += 1
    current_ad_idx = current_ad_idx % ads['count']

    return current_add