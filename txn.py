import requests
import json
from telegram.ext.dispatcher import run_async
from telegram.ext import Updater
from decimal import *


def details(update, context):
    text = update.message.text.split()
    if len(text) == 3:
        chain = text[1]
        target = text[2]
        if chain == 'trx' or chain == 'TRX' or chain == 'tron' or chain == 'TRON':
            url = "https://apilist.tronscan.org/api/transaction-info"
            payload = {"hash":
            target,
            }
            re = requests.get(url, params=payload)

            try:
                item = json.loads(re.text)["contractData"]
            except KeyError:
                print('Wrong Txn Hash')
                update.effective_message.reply_text('`Wrong Txn Hash`',parse_mode='markdown')
            if item == None:
                print('0')
                update.effective_message.reply_text('0')
            else:
                try:
                    send = item["owner_address"]
                    receive = item["to_address"]
                    type = 'TRC10 Transfer'
                    name = item["tokenInfo"]["tokenName"]
                    symbol = item["tokenInfo"]["tokenAbbr"]
                    mont = int(item["amount"])/100000/(int(item["tokenInfo"]["tokenDecimal"]))
                    be = '{:.7f}'.format(float(mont))
                    ms = f'`Sender: {send}\nReceiver: {receive}\nTransfer Type: {type}\nToken: {name}\nTicker: {symbol}\nAmount: {be} {symbol}`'
                    print(ms)
                    update.effective_message.reply_text(ms,parse_mode='markdown')
                except KeyError:
                    try:
                       item = json.loads(re.text)["trc20TransferInfo"][0]
                       if item == None:
                           print("0")
                       else:
                           se = item["from_address"]
                           to = item["to_address"]
                           ty = 'TRC20 Transfer'
                           token =item["name"]
                           sym = item["symbol"]
                           Am = int(item["amount_str"])/100000/(int(item["decimal"]))
                           Amo = '{:.7f}'.format(float(mont))
                           mv = f'Sender: {se}\nReceiver: {to}\nTransfer Type: {ty}\nToken: {token}\nTicker: {sym}\nAmount: {Amo} {sym}`'
                           print(mv)
                           update.effective_message.reply_text(mv,parse_mode='markdown')
                    except KeyError:
                        item = json.loads(re.text)["contractData"]
                        if item == None:
                            print("0")
                            update.effective_message.reply_text('Empty Txn')
                        else:
                            try:
                               From = item["owner_address"]
                               t_o = item["to_address"]
                               ransferype = 'TRX Transfer'
                               Token_name = 'Tron'
                               Symbol = 'TRX'
                               mount = int(item["amount"])/1000000
                               Amount = round(mount,5)
                               mk = f'`Sender: {From}\nReceiver: {t_o}\nTransfer Type: {ransferype}\nToken: {Token_name}\nTicker: {Symbol}\nAmount: {Amount} {Symbol}`'
                               print(mk)
                               update.effective_message.reply_text(mk,parse_mode='markdown')
                            except KeyError:
                               print('Wrong Txn Hash')
                               update.effective_message.reply_text('Wrong Txn')
                               
    else:
        update.effective_message.reply_text('Wrong format try:\n/tx <chain> <txn hash>',parse_mode='markdown')

    

