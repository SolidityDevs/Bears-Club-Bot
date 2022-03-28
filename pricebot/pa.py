import logging
from logging.handlers import TimedRotatingFileHandler

import locale
import re

from emoji import emojize
import telegram
import humanize
from pricebot.config import *
from pricebot.ads import get_current_add as myads


# start logging - print it to console for test cases
# logging.basicConfig(level=logging.INFO,
#                     format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
# module_logger = logging.getLogger(__name__)


# # start logging to the file with log rotation at midnight
formatter = logging.Formatter('%(asctime)s %(name)s %(levelname)s %(message)s')
handler = TimedRotatingFileHandler(os.path.dirname(os.path.realpath(__file__)) + '/../pricebot.log',
                                   when='midnight',
                                   backupCount=10)
handler.setFormatter(formatter)
module_logger = logging.getLogger(__name__)
module_logger.addHandler(handler)
module_logger.setLevel(logging.INFO)
# # end of log section

try:
    locale.setlocale(locale.LC_NUMERIC, 'es_ES.utf8')
except Exception as e:
    if hasattr(e, 'message'):
        ex_msg = e.message
    else:
        ex_msg = e

    module_logger.error('locale.setlocale EXCEPTION %s', ex_msg)

#my_link = "<a href='{get_current_link()}'>{get_current_add()}</a>",parse_mode=telegram.ParseMode.HTML, disable_web_page_preview=True


def parse_api_coinmarketcapjson(message_ticker):
    """
    the function to parse JSON file for a request ticker

    :param  message_ticker: a message with a ticker from user's request
    :type   message_ticker: str
    """

    # list of all conis from coinmarketcapjson from single class "jsonfiles" of config.py
    coinmarketcapjson = jsonfiles.coinmarketcapjson

    msg_parse_api = ''

    # temporaly version: when we don't use downloaded API file, but
    # are reading coinslist from a local json file (maybe earlier downloaded manually)
    #
    # if os.path.isfile(FILE_JSON_COINMARKET):
    #     Read configuration
        # with open(FILE_JSON_COINMARKET) as coinmarketcapjson:
        #     try:
        #         import json
        #         coinmarketcapjson = json.load(coinmarketcapjson)
        #     except:
        #         module_logger.error('api.coinmarketcap.com! bad json file to read: %s', coinmarketcapjson)
        #         msg_parse_api += error_information()

    if not coinmarketcapjson:

        module_logger.error('api.coinmarketcap.com! Error message: there is no coinmarketcap json file')
        msg_parse_api += error_information()

        # TODO send a message to the admin (a chat, a group, a channel)

    elif coinmarketcapjson:

        # find the ticker (by name or symbol of the coin) and parsing of json file to show data
        for ticker in coinmarketcapjson['data']:

            if ticker['name'].upper() == message_ticker or \
                    ticker['symbol'].upper() == message_ticker:

                price_usd = '$?'
                price_btc = ''
                rate1h = '?'
                rate1h_emoji = ''
                rate24h = '?'
                rate24h_emoji = ''
                rate7d = '?'
                rate7d_emoji = ''
                cmc_rank = '?'
                marketcap = '$'
                volume_24h = '$'
                high = '$'
                low = '$'
            

                # to put a header of the message
                msg_parse_api += msg_title_parse_api(str(ticker['name']), str(ticker['symbol']))

                # current price
                if ticker['quote']['USD']['price']:
                    price_usd_float = float(ticker['quote']['USD']['price'])

                    # for cut paddind zeros at the end of the price
                    if price_usd_float > 0.001:
                        #price_usd = '$' + str(locale.format("%.2f", price_usd_float, True))
                        price_usd =  "${0:,.5f}".format(float(price_usd_float))
                    else:
                        #price_usd = '$' + str(locale.format("%.3f", price_usd_float, True)).rstrip('0')
                        price_usd = "${0:,.8f}".format(float(price_usd_float))

                # 1 hour price change with emoji
                if ticker['quote']['USD']['percent_change_1h']:
                    rate1h_float = float(ticker['quote']['USD']['percent_change_1h'])
                    rate1h_emoji = parse_price_change(rate1h_float)
                    rate1h = locale.format('%.2f', rate1h_float, True)

                # 24 hours price change with emoji
                if ticker['quote']['USD']['percent_change_24h']:
                    rate24h_float = float(ticker['quote']['USD']['percent_change_24h'])
                    rate24h_emoji = parse_price_change(rate24h_float)
                    rate24h = locale.format('%.2f', rate24h_float, True)

                # 7 days price change with emoji
                if ticker['quote']['USD']['percent_change_7d']:
                    rate7d_float = float(ticker['quote']['USD']['percent_change_7d'])
                    rate7d_emoji = parse_price_change(rate7d_float)
                    rate7d = locale.format('%.2f', rate7d_float, True)

                # current cmc rank
                if ticker['cmc_rank']:
                    cmc_rank = ticker['cmc_rank']
                    cmc_rank = humanize.ordinal(cmc_rank)

                # current market cap
                if ticker['quote']['USD']['market_cap']:
                    marketcap = float(ticker['quote']['USD']['market_cap'])
                    marketcap = "${:,}".format(float(marketcap))

                # current cmc volume
                if ticker['quote']['USD']['volume_24h']:
                    volume_24h = float(ticker['quote']['USD']['volume_24h'])
                    volume_24h = "${:,}".format(float(volume_24h))
                

                msg_parse_api += f"\n*🍀Price:* `{price_usd}`\n\n" \
                                 f"`Ξ Changes`\n" \
                                 f"`▫️  1H:  {rate1h}%    {rate1h_emoji}\n`" \
                                 f"`▫️  24H: {rate24h}%   {rate24h_emoji}\n`" \
                                 f"`▫️  7D:  {rate7d}%    {rate7d_emoji}\n\n`" \
                                 f"`🏆 Rank: {cmc_rank}` \n" \
                                 f"`📊 Vol:  {volume_24h}`  \n" \
                                 f"`⚜️ Cap:  {marketcap}`  \n" \
                                 f"{myads()}\n"

        if msg_parse_api == '':
            msg_parse_api += error_ticker()

    else:
        module_logger.error('api.coinmarketcap.com! Error in def parse_api_coinmarketcapjson')
        msg_parse_api += error_information()

        # TODO send a message to the admin (a chat, a group, a channel)

    return   msg_parse_api 


def parse_api_globalinfoapijson():
    """
    the function to parse global API info
    """

    globalinfoapijson = jsonfiles.globalinfoapijson

    text, msg_parse_api = '', ''

    # temporaly version: when we don't use downloaded API file, but
    # are reading coinslist from a local json file (maybe earlier downloaded manually)
    #
    # if os.path.isfile(FILE_JSON_GLOBALINFOAPI):
        # Read configuration
        # with open(FILE_JSON_GLOBALINFOAPI) as globalinfoapijson:
        #     try:
        #         import json
        #         globalinfoapijson = json.load(globalinfoapijson)
        #     except:
        #         module_logger.error('api.coinmarketcap.com! bad json file to read: %s', globalinfoapijson)
        #         msg_parse_api += error_information()

    if not globalinfoapijson:

        module_logger.error('api.coinmarketcap.com! Error message: there is no globalinfoapijson json file')
        msg_parse_api += error_information()

        # TODO send a message to the admin (a chat, a group, a channel)

    elif globalinfoapijson:

        marketcap = globalinfoapijson['data']['quote']['USD']['total_market_cap']
        vol24h = globalinfoapijson['data']['quote']['USD']['total_volume_24h']
        btc_dominance = globalinfoapijson['data']['btc_dominance']

        text = emojize(':chart_with_upwards_trend: *CoinMarketCap Info*'
                   + '\nMarket Cap: *$' + sep(marketcap) + '*'
                   + '\n24h Vol: *$' + sep(vol24h) + '*'
                   + '\nBTC Dominance: *{}'.format(btc_dominance) + '%*', use_aliases=True)

    return text


# compare percent and add an emoji adequate
def parse_price_change(percent):
    emoji = ''

    if percent > 20:
        emoji = emojize(' :rocket:', use_aliases=True)

    elif percent <= -20.0:
        emoji = emojize(' :sos:', use_aliases=True)

    elif percent < 0:
        emoji = emojize(' :small_red_triangle_down:', use_aliases=True)

    elif percent > 0:
        emoji = emojize(' :white_check_mark:', use_aliases=True)

    return emoji


# to add a title, info of the API parsing with name and ticker of the coin
def msg_title_parse_api(ticker_name, ticker_symbol):
    # is a strange case of token with *, which telegram markdown is provoking an error
    if ticker_symbol.find('*') >= 0:
        ticker_symbol = re.sub(r'[\*]+', '', ticker_symbol)

    # re.sub(...) is to cut all symbols
    msg_parse_api = '*🔵' + re.sub(r'[^\S\n\t]+', '', ticker_name).strip()  \
                    +   ' ( ' + ticker_symbol + ')*'
    return msg_parse_api


# add a message with info of request problem
def error_information():
    error_text = '\nTry again later!\n'
    return error_text


# add a message if there is no ticket
def error_ticker():
    error_text = '\n*Ticker not found*\n'+myads()
    return error_text


# the short function for format number
def sep(s, thou=".", dec=","):
    integer, decimal = str(s).split(".")
    integer = re.sub(r"\B(?=(?:\d{3})+$)", thou, integer)
    # return integer + dec + decimal
    return integer
