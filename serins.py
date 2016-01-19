#!/usr/bin/env python
# encoding: utf-8

import logging
import asyncio
import os
import yaml
from hbmqtt.broker import Broker

# 日志文件配置
def init_log():
    console_file = logging.FileHandler('application.log')
    console_file.setLevel(logging.DEBUG)
    file_formatter = logging.Formatter('[%(asctime)s] :: %(levelname)s :: %(name)s :: %(message)s')
    console_file.setFormatter(file_formatter)
    logging.getLogger('').addHandler(console_file)


# 导入配置文件
stream = open('/home/ubuntu/Iot-Project/server/config.yaml','r')
yaml_conf = yaml.load(stream)
broker = Broker(yaml_conf)

@asyncio.coroutine
def test_coro():
    #broker = Broker()
    yield from broker.start()

if __name__ == '__main__':
    formatter = "[%(asctime)s] :: %(levelname)s :: %(name)s :: %(message)s"
    logging.basicConfig(level=logging.INFO, format=formatter)
    init_log()
    asyncio.get_event_loop().run_until_complete(test_coro())
    asyncio.get_event_loop().run_forever()
