# coding:utf-8

from datetime import datetime, date, timedelta
from logging import basicConfig, getLogger, DEBUG, INFO
import json
# import requests
import operator
import httpcon
# import datetime


# ロギング
basicConfig(level=INFO)
_logger = getLogger(__name__)


# 日付
# _today = date.today()
# today = datetime.strftime(_today, '%Y-%m-%d')
# _yesterday = _today - timedelta(days=1)
# yesterday = datetime.strftime(_yesterday, '%d-%m-%Y')


# エンドポイント
_endpoint = 'https://api.coingecko.com/api/v3'


INCOME_DISTRIBUTING_LIST = ['bitcoin',
                            'ethereum',
                            'litecoin',
                            'binancecoin',
                            'ripple',
                            'bitmark',
                            '0x',
                            'game',
                            'icon',
                            'omisego',
                            'zilliqa',
                            'ethereum-classic',
                            'zip',
                            'fcoin-token',
                            'tether',
                            'bitcoin-cash',
                            'aeternity']


# def getJsonResponse(url):
#     headers = {'User-Agent': 'bot-748/beta'}
#     response = requests.get(url, headers=headers)
#     _logger.info('getJsonResponse() response:{0}'.format(response))
#     return response.json()
#
#
# def printDict2Json(response_dict):
#     response_format_json = json.dumps(response_dict, indent=4,
#                                       separators=(',', ': '))
#     print(response_format_json)


def getTicker(id, date):
    apiurl = _endpoint + ('/coins/%s/history?id="%s"&date=%s') % (id, id, date)
    _logger.info('ticker() apiurl:{0}'.format(apiurl))
    ticker = httpcon.getJsonResponse(apiurl)
    name = ticker['name']
    symbol = ticker['symbol'].upper()
    status = ''
    message = ''
    try:
        price = ticker['market_data']['current_price']['jpy']
        status = 'OK'
    except KeyError:
        price = 0
        status = 'NG'
        message = '通貨データが存在しない'
    except TypeError:
        price = 0
        status = 'NG'
        message = '価格データが存在しない'
    coin = Coin(name, symbol, price, status, message)
    return coin


class Coin():
    def __init__(self, name, symbol, price, status, message):
         self.name = name
         self.symbol = symbol
         self.price = price
         self.status = status
         self.message = message


def getFCoinDividendPrice(date):
    price = []
    for currency in INCOME_DISTRIBUTING_LIST:
        coin = getTicker(currency, date)
        price.append(coin)
    price.sort(key=operator.attrgetter('symbol'))
    return price


def fcoindivid(inputdate):
    date = datetime.strptime(inputdate, '%Y-%m-%d')
    fdate = "{0:%d-%m-%Y}".format(date)
    dividend = getFCoinDividendPrice(fdate)
    reply = inputdate + 'のFCoin配当銘柄の価格'
    reply += '\n```'
    for coin in dividend:
        reply += ('\n%s,%s,%s') % (coin.symbol, coin.price, coin.status)
    reply += '\n```'
    return reply


# if __name__ == '__main__':
#     inputdate = '2018-06-29'
#     date = datetime.strptime(inputdate, '%Y-%m-%d')
#     fdate = "{0:%d-%m-%Y}".format(date)
#     dividend = getFCoinDividendPrice(fdate)
#     message = inputdate + ' のFCoin配当銘柄の価格'
#     for coin in dividend:
#         message += ('\n%s,%s,%s') % (coin.symbol, coin.price, coin.status)
#     _logger.info(message)