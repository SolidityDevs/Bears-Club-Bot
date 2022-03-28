import requests
import json
import sys

from telegram.ext.dispatcher import run_async
from telegram import InlineKeyboardButton, InlineKeyboardMarkup, Update
from telegram.ext import Updater, CommandHandler, CallbackQueryHandler, CallbackContext, Filters



from telegram.ext import *
from telegram import *
import telegram

admin = 1185692914
users = []
cmsg = f'*Bot Commands And Usage:*\n/p <coin> - get price of a coin\n/cap <coin> - get full details of coin\n/pcs <token symbol> or <contract address> - get price\n/news - get news \n/alert <coin> (< or >) <amount> - get alert for a coin\n/fng - frear and greed market sentiment\n/info <coin> - get coin description\n/c <coin> - to view candle chart of a coin\n/cc <coin> - get simple chat for a coin\n/listing - get new listed or to be listed token\n/cv <amount> <coin> <currency> - calculate quantity of a coin\n/ico <coin>- get ico details of a coin\n/meme - get memes\n/joke - get random joke\n/defi - get data defi coins\n/gas - get eth gas price\n/top - get top ten coins by volume\n/market <coin> - see exchange listed\n/ath <coin> - get all time high price\n/atl <coin> - get all time low price\n/social <coin> - get all social links platform\n/finance - get staking platforms\n/quote - get motivational quotes\n/tr - get top 7 trending coins/token\n/cap <coin> - get full details of a coin\n/ath <coin> - get ath details'

def start(update,context):
    """Sends a message with inline buttons attached."""
    msv = update.message.text.split()
    if len (msv) == 2:
        hel = msv[1]
        if hel == 'help':
            update.effective_message.reply_text(cmsg,parse_mode ='markdown')
    elif len(msv) == 1:
        keyboard = [[InlineKeyboardButton("Add Me To Your Group", url='https://t.me/cointendbot?startgroup=start')]]
        reply_markup = InlineKeyboardMarkup(keyboard)
        user = update.effective_chat.id
        usert = update.effective_user
        msd = f'*Hi {usert.first_name} *👋\nI am CoinTend Bot\n`I  help you to get crypto price\nCreate simple chart\nGet useful crypto data\!`\nSee all useful commands and how they work with /help button\!\n\n[Channel](https://t.me/cointend) | [Promotion & Issues](https://t.me/cointendadmin) | [News Channel](https://t.mecointendnews)'

        update.effective_message.reply_text(msd,parse_mode= 'markdown', reply_markup=reply_markup,disable_web_page_preview=True)
        if user not in users:# if the id isn't already in the users list
            users.append(user)
        
        # A way to use the list
def broadcast(update, context):
    user = update.effective_chat.id
    msg = update.message.text
    msg = msg.replace('/broadcast', '')
    if user == admin: # only if YOU start the command the message will be sent
        try:
            for id in users: # for every user that has start the bot
                msf = f'<b>Global Message From CoinTend 🦜</b>\n\n{msg}'
                context.bot.send_message(chat_id=id,text=msf,parse_mode='html',disable_web_page_preview=True)
        except telegram.error.Unauthorized:
            print('User has blocked the bot, so he/she cannot receive messages.')
               
            
def add_users(update,context):
    new = update.message.text.split()[1]
    user = update.effective_chat.id
    if user == admin:
        if new not in users: # if the id isn't already in the users list
            users.append(new)
            update.message.reply_text('Added id: '+new,parse_mode='markdown')
        
        
    



# Every time you are going to restart the bot polling the content of the users list will be deleated so...


def list(update,context):
    user = update.effective_chat.id
    if user == admin:
        context.bot.send_message(chat_id=admin, text=users) 


# /help command

def help(update: Update, context: CallbackContext) -> None:
    """Displays info on how to use the bot."""
   
    update.effective_message.reply_text(cmsg, parse_mode= 'markdown')




