# coding:utf-8

from logging import basicConfig, getLogger, DEBUG, INFO
from datetime import datetime, date, timedelta
import json
import requests

# ロギング
basicConfig(level=INFO)
_logger = getLogger(__name__)

# 日付
_today = datetime.today()
today = datetime.strftime(_today, '%Y-%m-%d')
_yesterday = _today - timedelta(days=1)
yesterday = datetime.strftime(_yesterday, '%Y-%m-%d')


FIAT = ["AUD", "BRL", "CAD", "CHF", "CLP", "CNY", "CZK", "DKK", "EUR", "GBP", "HKD", "HUF", "IDR", "ILS", "INR",
        "JPY", "KRW", "MXN", "MYR", "NOK", "NZD", "PHP", "PKR", "PLN", "RUB", "SEK", "SGD", "THB", "TRY", "TWD", "ZAR"]


def ticker():


if __name__ == '__main__':
