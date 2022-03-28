import json
import codecs
import requests
from bs4 import BeautifulSoup, SoupStrainer
from pycoingecko import CoinGeckoAPI
cg = CoinGeckoAPI()
from telegram.ext.dispatcher import run_async
from telegram.ext import Updater
from decimal import *

api = 'WWT9SAA5DC77ZKK5Z23Y2CJSI542SAXN2M'









import logging
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                                    level=logging.INFO)





def balance(update, context):
    zu = update.message.text.split()
    if len(zu) == 3:
        chain = zu[1]
        add = zu[2]
        if chain == 'Doge' or chain == 'doge' or chain == 'DOGE':
            get = requests.get('https://api.blockcypher.com/v1/doge/main/addrs/'+add+'/full?limit=99999')
            dd = cg.get_price(ids='dogecoin', vs_currencies='usd')
            ad = float(dd['dogecoin']['usd'])
            ge = get.json()
            bal = ge['balance']/100000000
            be = '{:.8f}'.format(float(bal))
            usr = ge['unconfirmed_balance']/100000000
            un = '{:.8f}'.format(float(usr))
            Us = usr*ad
            if Us > 0.1:
                Us = '{0:,.3f}'.format(float(Us))
            else:
                Us = '{0:,.5f}'.format(float(Us))
            us = ad*bal
            if us > 0.1:
                us = '{0:,.3f}'.format(float(us))
            else:
                us = '{0:,.5f}'.format(float(us))
            ms =f'♻️*Balance:* `{be}` *DOGE* `(${us})`\n🔸*Unconfirmed:* `{un}` *DOGE* `(${Us})`'
            update.effective_message.reply_text(ms,parse_mode='markdown')
            
        elif chain == 'btc' or chain == 'Btc' or chain == 'BTC':
            get = requests.get('https://api.blockcypher.com/v1/btc/main/addrs/'+add+'/full?limit=99999')
            dd = cg.get_price(ids='bitcoin', vs_currencies='usd')
            ad = float(dd['bitcoin']['usd'])
            ge = get.json()
            bal = ge['balance']/100000000
            be = '{:.8f}'.format(float(bal))
            usr = ge['unconfirmed_balance']/100000000
            un = '{:.8f}'.format(float(usr))
            Us = usr*ad
            if Us > 0.1:
                Us = '{0:,.3f}'.format(float(Us))
            else:
                Us = '{0:,.5f}'.format(float(Us))
            us = ad*bal
            if us > 0.1:
                us = '{0:,.3f}'.format(float(us))
            else:
                us = '{0:,.5f}'.format(float(us))
            ms =f'♻️*Balance:* `{be}` *BTC* `(${us})`\n🔸*Unconfirmed:* `{un}` *BTC* `(${Us})`'
            update.effective_message.reply_text(ms,parse_mode='markdown')
            
            
        elif chain == 'ltc' or chain == 'LTC' or chain == 'Ltc':
            get = requests.get('https://api.blockcypher.com/v1/ltc/main/addrs/'+add+'/full?limit=99999')
            dd = cg.get_price(ids='litecoin', vs_currencies='usd')
            ad = float(dd['litecoin']['usd'])
            ge = get.json()
            bal = ge['balance']/100000000
            be = '{:.8f}'.format(float(bal))
            usr = ge['unconfirmed_balance']/100000000
            un = '{:.8f}'.format(float(usr))
            Us = usr*ad
            if Us > 0.1:
                Us = '{0:,.3f}'.format(float(Us))
            else:
                Us = '{0:,.5f}'.format(float(Us))
            us = ad*bal
            if us > 0.1:
                us = '{0:,.3f}'.format(float(us))
            else:
                us = '{0:,.5f}'.format(float(us))
            ms =f'♻️*Balance:* `{be}` *LTC* `(${us})`\n🔸*Unconfirmed:* `{un}` *LTC* `(${Us})`'
            update.effective_message.reply_text(ms,parse_mode='markdown')
            
            
            
        elif chain == 'Eth' or chain == 'ETH' or chain == 'eth':
            get = requests.get('https://api.blockcypher.com/v1/eth/main/addrs/'+add+'/full?limit=99999')
            dd = cg.get_price(ids='ethereum', vs_currencies='usd')
            ad = float(dd['ethereum']['usd'])
            ge = get.json()
            bal = ge['balance']/100000000
            be = '{:.8f}'.format(float(bal))
            usr = ge['unconfirmed_balance']/100000000
            un = '{:.8f}'.format(float(usr))
            Us = usr*ad
            if Us > 0.1:
                Us = '{0:,.3f}'.format(float(Us))
            else:
                Us = '{0:,.5f}'.format(float(Us))
            us = ad*bal
            if us > 0.1:
                us = '{0:,.3f}'.format(float(us))
            else:
                us = '{0:,.5f}'.format(float(us))
            ms =f'♻️*Balance:* `{be}` *ETH* `(${us})`\n🔸*Unconfirmed:* `{un}` *ETH* `(${Us})`'
            update.effective_message.reply_text(ms,parse_mode='markdown')
            
        elif chain == 'trx' or chain == 'TRX' or chain == 'Trx' or chain == 'tron' or chain == 'trc' or chain == 'TRC' or chain == 'TRON':
            target = add
            dd = cg.get_price(ids='tron', vs_currencies='usd')
            ad = float(dd['tron']['usd'])
            print(target)
            url = "https://apilist.tronscan.org/api/account"
            payload = {
              "address": target,
             }
            res = requests.get(url, params=payload)
            trc20token_balances = json.loads(res.text)["balances"]
            if trc20token_balances == None:
                update.effective_message.reply_text("0")
            else:
                for item in trc20token_balances:
                    if item["tokenName"] == "trx":
                        aa = str(float(item["amount"]))
                        ads = float(item['amount'])
                        us = ad*ads
                        if us > 0.1:
                            us = '{0:,.3f}'.format(float(us))
                        else:
                            us = '{0:,.5f}'.format(float(us))
                        msg = f'`Balance: {aa} TRX (${us})`'
                        update.effective_message.reply_text(msg,parse_mode='markdown')
                        
        elif chain == 'bnb' or chain == 'BNB':
            targ = add
            r = requests.get('https://api.bscscan.com/api?module=account&action=balance&address='+targ+'&tag=latest&apikey='+api+'').json()
            bnbbx = int(r['result'])/1000000000000000000
            bb = round(bnbbx,5)
            dd = cg.get_price(ids='binancecoin', vs_currencies='usd')
            ad = float(dd['binancecoin']['usd'])
            Us = ad*bb
            if Us > 0.1:
                Us = '{0:,.3f}'.format(float(Us))
            else:
                Us = '{0:,.5f}'.format(float(Us))
            ms = f'`🧢 Balance: {bb} BNB (${Us})`'
            update.effective_message.reply_text(ms,parse_mode='markdown')
           
    else:
        update.effective_message.reply_text('Usage: /b <chain> <address>')
