from pricebot.ads import get_current_add as myads

from pycoingecko import CoinGeckoAPI
from emoji import emojize
import locale
import humanize

import json
import requests
from telegram import Update
from telegram.ext import Updater, CommandHandler, CallbackQueryHandler, CallbackContext, Filters
cg = CoinGeckoAPI()
coin_list = requests.get("https://api.coingecko.com/api/v3/coins/list").json()
from pycoingecko import CoinGeckoAPI
import requests





def parse_price_change(percent):
    emoji = ''

    if percent > 1 and percent <= 3.0:
        emoji = emojize(' :new_moon_face:', use_aliases=True)
        
    elif percent >= 3 and percent <= 5.0:
        emoji = emojize(' :partying_face:', use_aliases=True)
        
    elif percent >= 5 and percent <= 11.0:
        emoji = emojize(':slightly_smiling_face:', use_aliases=True)
        
    elif percent >= 11 and percent <= 16.0:
        emoji = emojize(' :bear:', use_aliases=True)
        
    elif percent >= 16 and percent <= 20.0:
        emoji = emojize(' :rocket:', use_aliases=True)
        
    elif percent >= 20 and percent <= 50.0:
        emoji = emojize(' :full_moon_face:', use_aliases=True)
        
    elif percent >= 50 and percent <= 100.0:
        emoji = emojize(' :joy:', use_aliases=True)
        
    elif percent > 100:
        emoji = emojize(' :fire:', use_aliases=True)
        
    elif percent > 0.1 and percent <= 1:
        emoji = emojize(' :wink:', use_aliases=True)
        
    elif percent >= 0 and percent <= 0.1:
        emoji = emojize(' :smirk:', use_aliases=True)
        
    elif percent <= -1 and percent <= -2:
        emoji = emojize(' :weary_face:', use_aliases=True)
        
    elif percent <= -2 and percent <= -3:
        emoji = emojize(' :white_frowning_face:', use_aliases=True)
        
    elif percent <= -3 and percent <= -4:
        emoji = emojize(' :grimacing_face:', use_aliases=True)
        
    elif percent <= -4 and percent <= -5:
        emoji = emojize(' :unamused_face:', use_aliases=True)
        
    elif percent <= -5 and percent <= -6:
        emoji = emojize(' :sneezing_face:', use_aliases=True)
        
    elif percent <= -6 and percent <= -7:
        emoji = emojize(' :small_red_triangle_down:', use_aliases=True)
        
    elif percent <= -7 and percent <= -8:
        emoji = emojize(' :frowning:', use_aliases=True)
        
    elif percent <= -8 and percent <= -9:
        emoji = emojize(' :hushed:', use_aliases=True)
        
    elif percent <= -9 and percent <= -10:
        emoji = emojize(' :sleepy_face:', use_aliases=True)
        
    elif percent <= -10 and percent <= -13:
        emoji = emojize(' :face_with_thermometer:', use_aliases=True)
        
    elif percent <= -13 and percent <= -15:
        emoji = emojize(' :drooling_face:', use_aliases=True)
        
    elif percent <= -15 and percent <= -20:
        emoji = emojize(' :zipper__mouth_face:', use_aliases=True)
        
    elif percent <= -20 and percent <= -100:
        emoji = emojize(' :sweat_drops:', use_aliases=True)
        
    elif percent <= -100:
        emoji = emojize(' :red_triangle_pointed_down:', use_aliases=True)
        
    elif percent < -0:
        emoji = emojize(' :fearful_face:', use_aliases=True)
    

    return emoji






        
        
def cap(update, context):
    text = update.message.text.split()
    if len(text) >= 2:
        user_input = text[1]
        for coin in coin_list:
            if coin['symbol'] == user_input:
                coin_id = coin['id']
                ds = cg.get_coins_markets(vs_currency='usd', ids=coin_id,price_change_percentage='1h,24h,7d,30d')
                ast = cg.get_coin_by_id(id=coin_id)
                ngn = "₦{:,}".format(int(ast["market_data"]["market_cap"]["ngn"]))
                eur = "€{:,}".format(int(ast["market_data"]["market_cap"]["eur"]))
                gbp = "£{:,}".format(int(ast["market_data"]["market_cap"]["gbp"]))
                btc = "₿{:,}".format(int(ast["market_data"]["market_cap"]["btc"]))
                name = ds[0]['id'].upper()
                symbol = ds[0]['symbol'].upper()
                price = ds[0]['current_price']
                if price > 0.001:
                    price = '{0:,.5f}'.format(float(price))
                else:
                    price = '{0:,.6f}'.format(float(price))
                high = ds[0]['high_24h']
                if high > 0.001:
                    high = '{0:,.4f}'.format(float(high))
                else:
                    high = '{0:,.6f}'.format(float(high))
                low = ds[0]['low_24h']
                if low > 0.001:
                    low = '{0:,.4f}'.format(float(low))
                else:
                    low = '{0:,.6f}'.format(float(low))
        
                if ds[0]['price_change_percentage_1h_in_currency']:
                    rate1h_float = float(ds[0]['price_change_percentage_1h_in_currency'])
                    rate1h_emoji = parse_price_change(rate1h_float)
                    rate1h = locale.format('%.2f', rate1h_float, True)

                # 24 hours price change with emoji
                if ds[0]['price_change_percentage_24h_in_currency']:
                    rate24h_float = float(ds[0]['price_change_percentage_24h_in_currency'])
                    rate24h_emoji = parse_price_change(rate24h_float)
                    rate24h = locale.format('%.2f', rate24h_float, True)

                # 7 days price change with emoji
                if ds[0]['price_change_percentage_7d_in_currency']:
                    rate7d_float = float(ds[0]['price_change_percentage_7d_in_currency'])
                    rate7d_emoji = parse_price_change(rate7d_float)
                    rate7d = locale.format('%.2f', rate7d_float, True)
                    
                    #30 days price change
                if ds[0]['price_change_percentage_30d_in_currency']:
                    rate30d_float = float(ds[0]['price_change_percentage_30d_in_currency'])
                    rate30d_emoji = parse_price_change(rate30d_float)
                    rate30d = locale.format('%.2f', rate30d_float, True)
                rank = ds[0]['market_cap_rank']
                ranks = humanize.ordinal(rank)
                ath = ds[0]['ath']
                if ath > 0.01:
                    ath = '{0:,.2f}'.format(float(ath))
                else:
                    ath = '{0:,.5f}'.format(float(ath))
                atl = ds[0]['atl']
                if atl > 0.01:
                    atl = '{0:,.2f}'.format(float(atl))
                else:
                    atl = '{0:,.5f}'.format(float(atl))
                supply = ds[0]['total_supply']
                if supply is None:
                    supply = 'N/A'
                else:
                    supply = '{:,}'.format(float(ds[0]['total_supply']))
                cir_supply = '{:,}'.format(float(ds[0]['circulating_supply']))
                vol = "${:,}".format(int(ds[0]["total_volume"]))
                mcap = "${:,}".format(int(ds[0]["market_cap"]))
                msg = f"`{name} ({symbol})\n`" \
                      f"`Price: ${price}\n`" \
                      f"`ΞH|L: ${high}|${low}\n`" \
                      f"`ΞATH|ATL: ${ath}|${atl}\n`" \
                      f"`Price Change:\n`" \
                      f"`1H: {rate1h}  {rate1h_emoji}\n`" \
                      f"`24H: {rate24h}  {rate24h_emoji}\n`" \
                      f"`7D: {rate7d}  {rate7d_emoji}\n`" \
                      f"`30D: {rate30d}  {rate30d_emoji}\n\n`" \
                      f"`Vol: {vol}\n`" \
                      f"`Market Cap:\n`" \
                      f"`{mcap}\n`" \
                      f"`{gbp}\n`" \
                      f"`{eur}\n`" \
                      f"`{ngn}\n`" \
                      f"`{btc}\n`" \
                      f"`Rank: {ranks}\n\n`" \
                      f"`Supply Info:\n`" \
                      f"`Total Supply: {supply}\n`" \
                      f"`Circulating Supply: {cir_supply}`\n" \
                      f"{myads()}"
                update.message.reply_text(msg,parse_mode='markdown',disable_web_page_preview=True)
                
    else:
        update.message.reply_text('Usage: /cap btt')
        
def ico(update, context):
    text = update.message.text.split()
    if len(text) >= 2:
        user_input = text[1]
        yts = user_input.upper()
        ytss = user_input.upper()
        if user_input == 'trx':
           coinss = cg.get_coin_by_id(id='tron')
           if coinss["ico_data"]["ico_start_date"]:
               starts =coinss["ico_data"]["ico_start_date"][:10]
           else:
               starts = "None"
           if coinss["ico_data"]["ico_end_date"]:
               ends =coinss["ico_data"]["ico_end_date"][:10]
           else:
               ends = "None"
           raiseds = "${:,}".format(float(coinss['ico_data']['total_raised']))
           pub_sales = coinss['ico_data']['quote_public_sale_amount']
           kycs = coinss['ico_data']['kyc_required']
           msgs = f"`ICO data for {ytss}\n\n`" \
                  f"`Start:    {starts}\n`" \
                  f"`End:      {ends}\n`" \
                  f"`Raised:   {raiseds}\n`" \
                  f"`Pub_Sale: 1 {ytss} for {pub_sales} USD\n`" \
                  f"`KYC:      {'Yes'if kycs == True else 'No'}`\n" \
                  f"{myads()}"
           update.message.reply_text(msgs,parse_mode='markdown',disable_web_page_preview=True)
        else:
            for coin in coin_list:
                if coin['symbol'] == user_input:
                    coin_id = coin['id']
                    coins = cg.get_coin_by_id(id=coin_id)
                    if 'ico_data' not in coins:
                        update.effective_message.reply_text('`ICO INFO NOT FOUND`',parse_mode='markdown')
                    else:
                        if coins["ico_data"]["ico_start_date"]:
                            start =coins["ico_data"]["ico_start_date"][:10]
                        else:
                            start = "None"
                        if coins["ico_data"]["ico_end_date"]:
                            end =coins["ico_data"]["ico_end_date"][:10]
                        else:
                            end = "None"
                        raised = coins ['ico_data']['total_raised']
                        if raised is None:
                            raised = 'N/A'
                        else:
                            raised = "${:,}".format(float(coins['ico_data']['total_raised']))
                        pub_sale = coins['ico_data']['quote_public_sale_amount']
                        kyc = coins['ico_data']['kyc_required']
                        curt = coins['ico_data']['total_raised_currency']
                        if curt is None:
                            curt = 'N/A'
                        else:
                            curt = curt
                        msg = f"`ICO data for {yts}\n\n`" \
                              f"`Start:    {start}\n`" \
                              f"`End:      {end}\n`" \
                              f"`Raised:   {raised}\n`" \
                              f"`Pub_Sale: 1 {yts} for {pub_sale} {curt}\n`" \
                              f"`KYC:      {'Yes'if kyc == True else 'No'}`\n" \
                              f"{myads()}"
                        update.message.reply_text(msg,parse_mode='markdown',disable_web_page_preview=True)
    else:
        update.message.reply_text("Usage: /ico btc")

