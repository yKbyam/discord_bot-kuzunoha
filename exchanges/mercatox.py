# coding:utf-8

import httpcon
import json
from decimal import *
from logging import basicConfig, getLogger, DEBUG, INFO

# ロギング
basicConfig(level=INFO)
logger = getLogger(__name__)

ENDPOINT = 'https://mercatox.com/public/json24full'
TICKER_BTC = 'NANJ_BTC'
TICKER_ETH = 'NANJ_ETH'

KEY_PAIRS = 'pairs'
KEY_LAST = 'last'
KEY_NANJBTC = 'NANJ_BTC'
KEY_NANJETH = 'NANJ_ETH'


def getLastPrice():
    '''
    HitBTCのNANJ/BTCレートを取得する
    取得失敗時は0を返す
    '''
    btc_last = Decimal(0)
    eth_last = Decimal(0)
    response = httpcon.getJsonResponse(ENDPOINT)
    if response is not None and KEY_PAIRS in response:
        pairs = response[KEY_PAIRS]
        btc_last = Decimal(pairs[KEY_NANJBTC][KEY_LAST])
        eth_last = Decimal(pairs[KEY_NANJETH][KEY_LAST])
    return {'btc_last': btc_last, 'eth_last': eth_last, }
