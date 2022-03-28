from bs4 import BeautifulSoup
from requests import Session
from telegram.ext import Updater
from pycoingecko import CoinGeckoAPI
from pricebot.ads import get_current_add as myads
cg = CoinGeckoAPI() 

def get_latest_token_from_coingecko():
    coin_gecko_request = Session()
    coin_gecko_response = coin_gecko_request.get("https://www.coingecko.com/en/coins/recently_added").text
    soup = BeautifulSoup(coin_gecko_response, "lxml")
    latest_token_url = soup.find(name="a", class_="d-lg-none").get("href")
    latest_token = latest_token_url.split("/")[-1]
    return latest_token

def check_binance_new_listings():
    binance_request = Session()
    binance_response = binance_request.get("https://www.binance.com/en/support/announcement/c-48?navId=48").text
    soup = BeautifulSoup(binance_response, "lxml")
    latest_news = soup.find(name="a", class_="css-1ej4hfo").text
    return latest_news



def new_listing(update, context):
    latest_token = get_latest_token_from_coingecko()
    binance = check_binance_new_listings()
    msg = f'`New Coin Listing:\n\n🐸Coingecko: {latest_token}\n🔹Binance: {binance}`\n{myads()}'
    update.effective_message.reply_text(msg,parse_mode='markdown',disable_web_page_preview=True)
