from __future__ import absolute_import, unicode_literals
import json
import redis
from tools import zabbix_api
from AnsbOps.celery import app
from AnsbOps.settings import REDIS_HOST,REDIS_PORT


@app.task
def get_zabbix_groblem(ZABBIX_URL, ZABBIX_USER, ZABBIX_PASS):
    zabbix_problem = zabbix_api.get_problem(ZABBIX_URL, ZABBIX_USER, ZABBIX_PASS)
    data = json.dumps(zabbix_problem,ensure_ascii=False,indent=True)
    rd = redis.Redis(host=REDIS_HOST,port=REDIS_PORT)
    rd.set("zabbix_problem", data)
    return data
