import requests

def get_top_coins(count):
    crypto_coins = requests.get(f"https://min-api.cryptocompare.com/data/top/mktcapfull?limit={count}&tsym=USD").json()["Data"]
    coins = [{} for i in range(int(count))]
    for i in range(len(crypto_coins)):
        data = {
            "ticker": crypto_coins[i]["CoinInfo"]["Name"],
            "name": crypto_coins[i]["CoinInfo"]["FullName"],
            "price": crypto_coins[i]["DISPLAY"]["USD"]["PRICE"],
            "market_cap": crypto_coins[i]["DISPLAY"]["USD"]["MKTCAP"],
            "volume_day": crypto_coins[i]["DISPLAY"]["USD"]["VOLUMEDAYTO"],
            "day_open": crypto_coins[i]["DISPLAY"]["USD"]["OPENDAY"],
            "day_high": crypto_coins[i]["DISPLAY"]["USD"]["HIGHDAY"],
            "day_low": crypto_coins[i]["DISPLAY"]["USD"]["LOWDAY"]
        }
        coins[i] = data

    return coins