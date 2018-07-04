# coding:utf-8

# 環境起動
# source ./bin/activate

import os
import re
import discord
import coingecko
from logging import basicConfig, getLogger, DEBUG, INFO

# ロギング
basicConfig(level=INFO)
logger = getLogger(__name__)

# discode Bot token
TOKEN = os.environ["BOT_TOKEN"]

# discode client
client = discord.Client()


# 日付正規表現２
date_yyyymmdd = re.compile('(\d{4})-(\d{1,2})-(\d{1,2})')


@client.event
async def on_ready():
    logger.info('------------------------')
    logger.info('Logged in as')
    logger.info('NAME:{0}'.format(client.user.name))
    logger.info('ID:{0}'.format(client.user.id))
    logger.info('------------------------')


@client.event
async def on_message(message):
    if client.user != message.author:
        if message.content.startswith("お馬さん"):
            await client.send_message(message.author, 'お馬さんパッカパッカ！')
        elif message.content.startswith('.fcoin'):
            inputdate = date_yyyymmdd.search(message.content)
            if inputdate is None:
                reply = 'ヒント .fcoin YYYY-mm-dd'
            else:
                reply = coingecko.fcoindivid(inputdate.group())
            await client.send_message(message.channel, reply)


# -- main -----------------------------------------------------------------------


if __name__ == '__main__':
    # botの実行
    client.run(TOKEN)
