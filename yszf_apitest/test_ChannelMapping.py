# -*-coding:utf-8-*-
import requests

URL = "http://orgmerc.ysepay.com:8080"


class Test_channelmap():
    def test_queryMapping(self):
        header = {
            "Content-Type": "application/json"
        }
        body = {
            "channelNo": "hncib",
            "agtId": "80169471118MNKH",
            "areaCode": "1234",
            "areaName": "地区映射测试",
            "startTime": "",
            "endTime": ""
        }
        r = requests.post(URL + "/bccManager/areaMapping/queryMappings", headers=header, data=body)
        print(r.json())
        assert r.status_code == 200
