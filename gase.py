import requests
import json
import os
from pricebot.ads import get_current_add as ad
from pycoingecko import CoinGeckoAPI
cg = CoinGeckoAPI()

def get_gas_data():
    try:
        query_url = f"https://api.etherscan.io/api?module=gastracker&action=gasoracle&apikey=9FEU5MTPSETCP42VF7MAQJ1MUKEPEQKYVB"
        gas_response = requests.get(query_url)
        gas_price = json.loads(gas_response.text)
        results = gas_price['result']
        gas_dict = {
            "last_block": results['LastBlock'],
            "safe_gas": f"{results['SafeGasPrice']} ",
            "propose_gas": f"{results['ProposeGasPrice']} ",
            "fast_gas": f"{results['FastGasPrice']} "

        }
        return gas_dict

    # Handle api call failures
    except Exception as e:
        print(e, flush=True)
        gas_dict = {
            "last_block": "Data Unavailable",
            "safe_gas": "Data Unavailable",
            "propose_gas": "Data Unavailable",
            "fast_gas": "Data Unavailable"

        }
        return gas_dict
    
def defi(update, context):
    defi = cg.get_global_decentralized_finance_defi()
    defi_market_cap = defi['defi_market_cap']
    eth_market_cap = defi['eth_market_cap']
    trading_volume_24h = defi['trading_volume_24h']
    defi_dominance = defi['defi_dominance']
    top_coin_name = defi['top_coin_name']
    top_coin_defi_dominance = defi['top_coin_defi_dominance']
    full_info ="`Defi MCap`: $" + '{0:,.2f}'.format(float(defi_market_cap)) + "\n" + \
               "`Eth  MCap`: $" + '{0:,.2f}'.format(float(eth_market_cap)) + "\n" + \
               "`Defi Trade Vol`: $" + '{0:,.2f}'.format(float(trading_volume_24h)) + "\n" + \
               "`DeFi Dominance`: " + '{0:,.2f}'.format(float(defi_dominance)) + "%" + "\n" + \
               "`Top Defi`: " + str(top_coin_name) + "\n" + \
               "`Top Defi Dominance`: " + '{0:,.2f}'.format(float(top_coin_defi_dominance)) + "%"
    update.effective_message.reply_text(full_info,parse_mode='markdown')
    
    
coin_list = cg.get_coins_list()
def send_market(update, context):
    zu = update.message.text.split()
    coin_market = []
    if len(zu) != 2:
        update.effective_message.reply_text("Usage: /market btc")
    else:
        user_input = zu[1]
        print(user_input)
        for coin in coin_list:
            if coin['symbol'] == user_input:
                coinID = coin['id']
                coinSymbol = coin['symbol']
                coinInfo = cg.get_coin_ticker_by_id(id=coinID)
                n = 0
                while n < 12:
                    try:
                        if coinInfo['tickers'][n]['trade_url'] is None:
                            pass
                        else:
                            base = coinInfo['tickers'][n]['base']
                            target = coinInfo['tickers'][n]['target']
                            market = coinInfo['tickers'][n]['market']['name']
                            trade_url = coinInfo['tickers'][n]['trade_url']
                            pair = str(base) + "/" + str(target)
                            try:
                                birja = str("Exchange: ") + str(market) + "\n"
                            except Exception:
                                birja = str("") + "\n"
                            try:
                                wkvili = str("Pair: ") + '[' + pair + ']('+ trade_url + ')' + "\n"
                            except Exception:
                                wkvili = str("") + "\n"

                        info = birja + wkvili
                        coin_market.append(info)
                        n += 1
                        full_info = '\n'.join(map(str, coin_market))
                    except Exception:
                        break
                full_info = full_info
                update.effective_message.reply_text(str(coinID.title()) + " (" + str(coinSymbol.upper()) + ")" + "\n" + "`--------------------`" + "\n" + full_info +""+ad()+"", disable_web_page_preview=True, parse_mode='Markdown')
                coin_market.clear()
                break
        else:
            update.effective_message.reply_text("Data not found")
            
            
def send_ath(update, context):
    zu = update.message.text.split()
    if len(zu) < 2:
        update.effective_message.reply_text("Usage: /ath eth")
    else:
        user_input = zu[1]
        for coin in coin_list:
            if coin['symbol'] == user_input:
                coin_id = coin['id']
                print(coin_id)
                coin_info = cg.get_coins_markets(vs_currency='usd', ids=coin_id)
                symbol = coin_info[0]['symbol']
                name = coin_info[0]['name']
                current_price = coin_info[0]['current_price']
                ath = coin_info[0]['ath']
                if ath > 0.01:
                    ath = '{0:,.2f}'.format(float(ath))
                else:
                    ath = '{0:,.8f}'.format(float(ath))

                ath_date = coin_info[0]['ath_date']
                info = "🧩 " + str(name) + " (" + str(symbol.upper()) + ") " + "\n" + \
                        "`---------------------`" + "\n" + \
                        "`Ath Price: $" + str(ath) + "`\n" + \
                        "`Ath Date: " + str(ath_date[:10]) + "`\n" + \
                        "`Current Price: $" + '{0:,.2f}'.format(float(current_price)) + "`\n"
                update.effective_message.reply_text(info, parse_mode='Markdown')
                break
            
        else:
            update.effective_message.reply_text("Coin not found")
            
def send_atl(update, context):
    zu = update.message.text.split()
    if len(zu) < 2:
        update.effective_message.reply_text("Usage: /atl eth")
    else:
        user_input = zu[1]
        for coin in coin_list:
            if coin['symbol'] == user_input:
                coin_id = coin['id']
                print(coin_id)
                coin_info = cg.get_coins_markets(vs_currency='usd', ids=coin_id)
                symbol = coin_info[0]['symbol']
                name = coin_info[0]['name']
                current_price = coin_info[0]['current_price']
                atl = coin_info[0]['atl']
                if atl > 0.01:
                    atl = '{0:,.2f}'.format(float(atl))
                else:
                    atl = '{0:,.8f}'.format(float(atl))

                atl_date = coin_info[0]['atl_date']
                info = "🧩 " + str(name) + " (" + str(symbol.upper()) + ") " + "\n" + \
                        "`---------------------`" + "\n" + \
                        "`Atl Price: $" + str(atl) + "`\n" + \
                        "`Atl Date: " + str(atl_date[:10]) + "`\n" + \
                        "`Current Price: $" + '{0:,.2f}'.format(float(current_price)) + "`\n"
                update.effective_message.reply_text(info, parse_mode='Markdown')
                break
            
        else:
            update.effective_message.reply_text("Coin not found")

       
def send_coin_social(update, context):
    text =  update.message.text.split()
    if len(text) != 2:
        update.effective_message.reply_text('Usage: /social <coin>')
    else:
        user_input = text[1]
        for coin in coin_list:
            if coin['symbol'] == user_input:
                coinID = coin['id']
                coinSymbol = coin['symbol']
                coinInfo = cg.get_coin_by_id(id=coinID)
                if coinInfo['links']['homepage'][0] is None:
                    homepage = "None"
                else:
                    homepage = "[🌐 Homepage ](" + coinInfo['links']['homepage'][0]+")"
                if coinInfo['links']['twitter_screen_name'] is None:
                    twitter = "None"
                else:
                    twitters = coinInfo['links']['twitter_screen_name']
                    twitter = '🐦 [ Twitter ](https://twitter.com/' + twitters + ')'
                    
                        
                if coinInfo['links']['facebook_username'] is None:
                    facebook = "None"
                else:
                    facebook = coinInfo['links']['facebook_username']
                    facebook = '👌 [ Facebook](https://facebook.com/' + facebook + ')'
                    
                    
                if coinInfo['links']['telegram_channel_identifier'] is None:
                    telegram = "Not found"
                else:
                    telegram = "🔹 [Telegram](https://t.me/" + coinInfo['links']['telegram_channel_identifier']+")"
                    full_info = homepage + "\n" + \
                                twitter + "\n" + \
                                telegram + "\n" + \
                                facebook + "\n"
                try:
                    update.effective_message.reply_text(str(coinID.title()) + " (" + str(coinSymbol.upper()) + ")" + "\n" + "`----------------------`" + "\n" + \
                                full_info, disable_web_page_preview=True, parse_mode='Markdown')
                except Exception:
                    update.message.reply_text("" + str(user_input.upper()) + "not found")
                   
        
def finance_platforms(update, context):
    fi = cg.get_finance_platforms(per_page=10)
    platform_list = []
    platform_list.clear()
    n = -1
    while n < 10:
        n += 1
        try:
            name_link = '[' + fi[n]['name'] + '](' + fi[n]['website_url'] + ')'
            category = fi[n]['category']
            if category == "CeFi Platform":
                category = " - CeFi"
            else:
                category = " - DeFi"
                fi_info = "🔸 " + str(name_link) + " " + str(category)
                platform_list.append(fi_info)
        except Exception:
            fi_info = "Error!"
            full_info = "Finance Platforms" + "\n" + "`------------------------`" + "\n" + '\n'.join(map(str, platform_list))
            update.effective_message.reply_text(full_info, disable_web_page_preview=True, parse_mode='Markdown')
def joke(update,context):
    tyu = requests.get("https://v2.jokeapi.dev/joke/Any").json()
    if tyu['type'] == 'single':
        joke = tyu['joke']
        mk = f'`{joke}`\n{ad()}'
        print(joke)
        update.message.reply_text(mk,parse_mode='markdown',disable_web_page_preview=True)
    elif tyu['type'] == 'twopart':
        setup = tyu["setup"]
        joke = tyu["delivery"]
        ms = f'`{setup} ~ {joke}`\n{ad()}'
        print(ms)
        update.message.reply_text(ms,parse_mode='markdown',disable_web_page_preview=True)
    else:
        print(tyu)
        mj = f'Try later!`\n{ad()}'
        update.message.reply_text(mj,parse_mode='markdown',disable_web_page_preview=True)
    
def fng(update, context):
    user = update.message.chat_id
    file = open("fearAndGreed.png", "wb")
    file.write(requests.get("https://alternative.me/crypto/fear-and-greed-index.png").content)
    context.bot.send_photo(chat_id=user, photo=open("fearAndGreed.png", "rb"))
    file.close()
    os.remove('fearAndGreed.png')
