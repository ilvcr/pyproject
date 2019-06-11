# -*- coding: utf-8 -*-

# @Time    : 2019-01-09 10:24
# @Author  : 小贰
# @FileName: zabbix_2_api.py
# @function: zabbix api for python 3.x

import json
import time
from urllib import request, parse


class zabbix_api:
    def __init__(self,url,user,passwd):
        self.url = url
        self.user = user
        self.passwd = passwd
        self.header = {"Content-Type": "application/json"}

    def user_login(self):
        data = {
            "jsonrpc": "2.0",
            "method": "user.login",
            "params": {
                "user": self.user,
                "password": self.passwd
            },
            "id": 0
        }
        # 由于API接收的是json字符串，故需要转化一下
        data = json.dumps(data).encode('utf-8')
        # 对请求进行包装
        req = request.Request(self.url, headers=self.header, data=data)
        try:
            # 打开包装过的url
            result = request.urlopen(req)
        except Exception as e:
            print("Auth Failed, Please Check Your Name And Password:", e)
        else:
            response = result.read()
            # 上面获取的是bytes类型数据，故需要decode转化成字符串
            page = response.decode('utf-8')
            # 将此json字符串转化为python字典
            page = json.loads(page)
            self.authID = page['result']
            result.close()
            return self.authID
    def main(self,method,params):
        data = {
            "jsonrpc": "2.0",
            "method": method,
            "params": params,
            "auth": self.user_login(),
            "id": 1
        }
        data = json.dumps(data).encode("utf-8")
        req = request.Request(self.url, headers=self.header, data=data)

        try:
            result = request.urlopen(req)
        except Exception as e:
            print('Error code: ', e)
        else:
            response = result.read()
            # 上面获取的是bytes类型数据，故需要decode转化成字符串
            page = json.dumps(json.loads(response.decode('utf-8')),indent=4,ensure_ascii=False)

            return page

def get_problem(url,user,passwd):
    zabbix = zabbix_api(url,user,passwd)
    method = "host.get"
    params = {
        "output": ["hostid",""],
    }
    result = zabbix.main(method, params)
    host_list = json.loads(result)["result"]

    data_list = []
    for i in host_list:
        id = i["hostid"]

        method = "hostinterface.get"
        params = {
            "output": ["ip"],
            "hostids":id,
        }

        result = zabbix.main(method, params)
        ip = json.loads(result)["result"][0]["ip"]

        method = "trigger.get"
        params = {
            "output": [
                    "description",
                    "lastchange",
                    "priority",
                ],
            "hostids":id,
            "filter": {
                "value": 1,
                "status": 0
            },
        }
        result = zabbix.main(method,params)
        result = json.loads(result)["result"]
        if result:
            for j in result:
                timeArray = time.localtime(int(j["lastchange"]))
                date_str = time.strftime("%Y-%m-%d %H:%M:%S", timeArray)
                data_list.append((date_str,ip,j["description"],j["priority"]))
    return data_list

if __name__ == "__main__":
    url = 'http://115.231.100.246:18080/zabbix/api_jsonrpc.php'
    user = "admin"
    passwd = "zabbix"
    ret = get_problem(url,user,passwd)
    print(ret)