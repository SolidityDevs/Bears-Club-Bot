import requests
from bs4 import BeautifulSoup
from requests import Session
import random
from pricebot.ads import get_current_add as ad
from telegram import Update
import telegram
from telegram import bot,ChatAction
from telegram.ext import Updater, CommandHandler, CallbackQueryHandler, CallbackContext, Filters


def memes():
    page_no = 1
    tenpages = []
    for i in range(10):
        url = "https://imgflip.com/tag/memes?page=" + str(page_no)
        r = requests.get(url)
        soup = BeautifulSoup(r.text,"html.parser")
        for d in (soup.find('div', attrs={"id":"page" , "class":"base clearfix"}).find('div', attrs={"id":"base-left"}).find_all("div" , attrs={"class":"base-unit clearfix"})):
            p = (d.find("div" , attrs = {"class":"base-img-wrap-wrap"}).find('img'))
            try:
                tenpages.append("https:" + str(p['src']))
            except:
                pass
        page_no += 1
        print(tenpages)
    return(random.choice(tenpages))
def meme(update,context):
    urls = memes()
    chat_id = update.effective_chat.id
    context.bot.send_chat_action(chat_id=update.message.chat_id , 
                action = telegram.ChatAction.UPLOAD_PHOTO)
    context.bot.send_photo(chat_id=chat_id, photo=urls,caption=''+ad()+'',parse_mode='markdown')
    
