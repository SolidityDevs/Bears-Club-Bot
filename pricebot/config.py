import os

# the token of your bot
TOKEN_BOT = '1646343192:AAFnHiT7h8orI8rAu3ai91kWR3sOZDOjrpM'
#TOKEN_BOT = '1963442105:AAFgfD5kTxMsvqUp0hpW3y9c-ZGMAyZwuFI'


# do APIs requests with pause
TIME_INTERVAL = 3600

# new pro API CoinMarketCap Key
CMC_API_KEY = ["bf9bade8-89d2-4674-b45e-8414404f9d7a", "328056e6-bb95-4f20-8032-f1b50dc68f5c", "c60fca24-cdfc-4845-8494-134b95d547f3"]
COINMARKET_API_URL_GLOBAL = 'https://pro-api.coinmarketcap.com/v1/global-metrics/quotes/latest' \
                            '?CMC_PRO_API_KEY={}'
COINMARKET_API_URL_COINLIST = 'https://pro-api.coinmarketcap.com/v1/cryptocurrency/listings/latest?start=1&limit=5000' \
                              '&CMC_PRO_API_KEY={}'

FILE_JSON_COINMARKET = os.path.dirname(os.path.realpath(__file__)) + '/coinmarketcoins.json'
FILE_JSON_GLOBALINFOAPI = os.path.dirname(os.path.realpath(__file__)) + '/globalinfoapi.json'


class JSONFiles:
    def __init__(self):
        self.coinmarketcapjson = {}
        self.globalinfoapijson = {}

    def update_cmc_json(self, json1):

        assert isinstance(json1, dict)
        self.coinmarketcapjson = json1
        return json1

    def update_globalcmc_json(self, json2):
        assert isinstance(json2, dict)
        self.globalinfoapijson = json2
        return json2


# the object of class JSONFiles for save json API coins lists
jsonfiles = JSONFiles()


