# coding:utf-8

import requests
import ccxt
# import ccxt.async as ccxt  # link against the asynchronous version of ccxt

import json
from logging import basicConfig, getLogger, DEBUG, INFO
from decimal import *

# ロギング
basicConfig(level=INFO)
logger = getLogger(__name__)


def getJsonResponse(url):
    headers = {'User-Agent': 'bot-748/beta'}
    response = requests.get(url, headers=headers)
    return response.json()


def getStocksExchangeNANJ():
    result = {}
    tickers = getJsonResponse('https://stocks.exchange/api2/ticker')
    for ticker in tickers:
        if (ticker['market_name'] == 'NANJ_BTC'):
            result['NANJ_BTC'] = ticker
        elif (ticker['market_name'] == 'NANJ_USDT'):
            result['NANJ_USDT'] = ticker
    return result


def getUSDT_JPY():
    lastprice = Decimal(0)
    apiurl = 'https://api.coingecko.com/api/v3/coins/tether'
    response = getJsonResponse(apiurl)
    lastprice = Decimal(response['market_data']['current_price']['jpy'])
    return lastprice


def getAvalageBTC_JPY():
    bf = ccxt.bitflyer({
        'apiKey': '',
        'secret': ''
    })
    cc = ccxt.coincheck({
        'apiKey': '',
        'secret': ''
    })
    zf = ccxt.zaif({
        'apiKey': '',
        'secret': ''
    })
    bf_ret = bf.fetch_ticker(symbol='BTC/JPY')
    # logger.info(('bf_ret:\n') + json.dumps(bf_ret, indent=True))
    logger.info('bf:{0}'.format(bf_ret['last']))
    cc_ret = cc.fetch_ticker(symbol='BTC/JPY')
    # logger.info(('cc_ret:\n') + json.dumps(cc_ret, indent=True))
    logger.info('cc:{0}'.format(cc_ret['last']))
    zf_ret = zf.fetch_ticker(symbol='BTC/JPY')
    # logger.info(('zf_ret:\n') + json.dumps(zf_ret, indent=True))
    logger.info('zf:{0}'.format(zf_ret['last']))


if __name__ == '__main__':
    # getAvalageJPY_BTC()
    se_nanj = getStocksExchangeNANJ()
    # logger.info('NANJ_BTC:\n{:.8f}'.format(Decimal(se_nanj['NANJ_BTC']['last'])))
    logger.info('NANJ_USDT:{:.8f}'.format(Decimal(se_nanj['NANJ_USDT']['last'])))
    cg_usdt = getUSDT_JPY()
    logger.info('USDT_JPY:{:.8f}'.format(cg_usdt))
    nanj_usdt_jpy = Decimal(se_nanj['NANJ_USDT']['last']) * cg_usdt
    logger.info('NANJ_USDT_JPY:{:.8f}'.format(nanj_usdt_jpy))
