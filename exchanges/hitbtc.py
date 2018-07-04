# coding:utf-8

import httpcon
import json
from decimal import *
from logging import basicConfig, getLogger, DEBUG, INFO

# ロギング
basicConfig(level=INFO)
logger = getLogger(__name__)

ENDPOINT = 'https://api.hitbtc.com/api/2/'
TICKER = 'public/ticker/'
# 'https://api.hitbtc.com/api/2/public/ticker/NANJBTC'
ORDERBOOK = 'public/orderbook/'
# 'https://api.hitbtc.com/api/2/public/orderbook/NANJBTC'
SYMBOL = 'NANJBTC'
KEY_LAST = 'last'

def getLastPrice():
    '''
    HitBTCのNANJ/BTCレートを取得する
    取得失敗時は0を返す
    '''
    lastprice = Decimal(0)
    apiurl = ENDPOINT + TICKER + SYMBOL
    logger.debug('getLastPrice() apiurl:{0}'.format(apiurl))
    response = httpcon.getJsonResponse(apiurl)
    if response is not None and KEY_LAST in response:
        lastprice = Decimal(response[KEY_LAST])
        # HitBTCは小数点以下9桁(xx.x sat)なので注意
        logger.debug('getLastPrice() lastprice:{:.8f}'.format(lastprice))
    return lastprice
