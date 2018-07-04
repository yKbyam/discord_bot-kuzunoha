# coding:utf-8

import httpcon
import json
from decimal import *
from logging import basicConfig, getLogger, DEBUG, INFO

# ロギング
basicConfig(level=INFO)
logger = getLogger(__name__)

ENDPOINT = 'https://stocks.exchange/api2'
TICKER = '/ticker/'


def getLastPriceBTC():
    '''
    NANJ/BTCペアの最終約定レートを取得する
    取得失敗時は0を返す
    '''
    lastprice = Decimal(0)
    apiurl = ENDPOINT + TICKER
    response = httpcon.getJsonResponse(apiurl)
    if response is not None:
        for ticker in response:
            if (ticker['market_name'] == 'NANJ_BTC'):
                lastprice = Decimal(ticker['last'])
    return lastprice


def getLastPriceUSDT():
    '''
    NANJ/USDTペアの最終約定レートを取得する
    取得失敗時は0を返す
    '''
    lastprice = Decimal(0)
    apiurl = ENDPOINT + TICKER
    response = httpcon.getJsonResponse(apiurl)
    if response is not None:
        for ticker in response:
            if (ticker['market_name'] == 'NANJ_USDT'):
                lastprice = Decimal(ticker['last'])
    return lastprice
