# coding:utf-8

import urllib
import requests
import json
from logging import basicConfig, getLogger, DEBUG, INFO

# ロギング
basicConfig(level=INFO)
logger = getLogger(__name__)


DOMAIN = 'https://s3-ap-northeast-1.amazonaws.com/'
PATH_1 = 'bot748-resources/images/'


def getJsonResponse(url):
    headers = {'User-Agent': 'bot-748/beta'}
    response = requests.get(url, headers=headers)
    json_response = response.json()
    # logger.debug('getJsonResponse() result:{0}'.format(printDict2Json(json_response)))
    return json_response


def printDict2Json(response_dict):
    response_format_json = json.dumps(response_dict, indent=4, separators=(',', ': '))
    print(response_format_json)


def downloadImage(filename, savename=None):
    urlstr = DOMAIN + PATH_1 + filename
    logger.debug('downloadImage() urlstr:' + urlstr)
    if savename is None:
        urllib.request.urlretrieve(urlstr, filename)
    else:
        urllib.request.urlretrieve(urlstr, savename)
