import requests


class Util:
    def get_token(self):
        requests_params = {
            "corpid": "ww1d0df80a9ad528de",
            "corpsecret": "8nQMZi5-VPcw1UjYPcOLQWA0g-VdLHNV5531pbIPrkk"
        }
        r = requests.get("https://qyapi.weixin.qq.com/cgi-bin/gettoken", params=requests_params)
        return r.json()["access_token"]
