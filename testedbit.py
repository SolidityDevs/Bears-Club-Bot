from telegram import Update
from telegram.ext import Updater, CommandHandler, CallbackQueryHandler, CallbackContext, Filters
from telegram import InlineKeyboardButton, InlineKeyboardMarkup
from pricebot.ads import get_current_add as myads

from googletrans import Translator
translator = Translator()

key = [[InlineKeyboardButton("Find short codes", callback_data=f'Shortcodes')]]
reply_mark = InlineKeyboardMarkup(key)
                    

def trans(update: Update, context: CallbackContext):
    user = update.message.text.split()
    chat_id = update.message.from_user.id
    wooo = update.message.text
    reply_to_message = update.message.reply_to_message
    
    if reply_to_message == None:
        if len(user) > 2:
            lang = user[1]
            words = wooo[9:]
            try:
                aars = translator.translate(words,dest=lang).text
                msg = f"*Text:* {words}\n*Translated*: {aars}\n{myads()}"
                context.bot.send_message(chat_id,msg,reply_markup=reply_mark,parse_mode='markdown',disable_web_page_preview=True)
            except ValueError:
                context.bot.send_message(chat_id,"Add Language Short Code")
                
            
        else:
           context.bot.send_message(chat_id,'*Usage:\n/trans <your text>\n/trans <text> <language short code>*',parse_mode='markdown')
    else:
        texts = reply_to_message.text
        if len(user) == 1:
            arx = translator.translate(texts,dest='en').text
            bms = f"*User Message:* {texts}\n*Translation:* {arx}\n{myads()}"
            context.bot.send_message(chat_id,bms,reply_markup=reply_mark,parse_mode='markdown',disable_web_page_preview=True)
        elif len(user) ==2:
            lan = user[1]
            aar = translator.translate(texts,dest=lan).text
            apod = f"*User Message:* {texts}\n*Translation:* {aar}\n{myads()}"
            context.bot.send_message(chat_id,apod,parse_mode='markdown',disable_web_page_preview=True)
        else:
            context.bot.send_message(chat_id,'*Usage:\nReply to user\n/trans\n/trans <language short code>*',parse_mode='markdown')
