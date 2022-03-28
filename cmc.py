import requests
import json
import sys
import random

from telegram.ext.dispatcher import run_async
from telegram import InlineKeyboardButton, InlineKeyboardMarkup, Update
from telegram.ext import Updater, CommandHandler, CallbackQueryHandler, CallbackContext, Filters


from pricebot.config import *
from pricebot.pa import parse_api_coinmarketcapjson, parse_api_globalinfoapijson


length = len(CMC_API_KEY)
randomIndex = random.randint(0, length - 1)  
cmc = CMC_API_KEY[randomIndex]     
run_async
# job queue to download CoinMarket API all coins list
run_async
def download_api_coinslists_handler(context):
    """
    the handler for download the lists of coins from API agregators by job_queue of telegram.ext

    :param  bot: a telegram bot main object
    :type   bot: Bot

    :param  job: job.context is a name of the site-agregator, which has been send from job_queue.run_repeating... method
    :type   job: Job
    """

    

    response = requests.get(COINMARKET_API_URL_COINLIST.format(cmc))

    # extract a json from response to a class 'dict' or 'list'
    response_dict_list = response.json()

    if response.status_code == requests.codes.ok:

        # check if one of the APIs response is an error
        if 'status' in response_dict_list and response_dict_list['status']['error_code'] != 0:

            error_msg = response_dict_list['status']['error_message']
            
        else:
           
            with open(FILE_JSON_COINMARKET, 'w') as outfile:
                json.dump(response_dict_list, outfile)
                print('Success save it to %s', FILE_JSON_COINMARKET)

            # save a json to variable
            if context.job.context == 'coinmarketcap':
                jsonfiles.update_cmc_json(response_dict_list)

    else:
        print('%s API has not been response successfully', context.job.context)


# job queue to download CoinMarket API Global Data
run_async
def download_api_global_handler(context):
    """
    the handler for download global Coin Market Cap API Info by job_queue of telegram.ext
    """

    print('Start a request to CoinMarketCap API')

    response = requests.get(COINMARKET_API_URL_GLOBAL.format(cmc))

    # extract a json from response to a class 'dict' or 'list'
    response_dict_list = response.json()

    if response.status_code == requests.codes.ok:

        print('Success download a global CoinMarketCap JSON API')

        with open(FILE_JSON_GLOBALINFOAPI, 'w') as outfile:
            json.dump(response_dict_list, outfile)
            print('Success save it to %s', FILE_JSON_GLOBALINFOAPI)

        jsonfiles.update_globalcmc_json(response_dict_list)

    else:
        print('CoinMarketCap JSON API /global not responses successfully')
