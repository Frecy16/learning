# -*-coding:utf8-*-
import requests


class TestApi:
    def test_get(self):
        payload = {'name': 'cheny', 'token': 'Abc700cy98UM54pyb'}
        r = requests.get('http://httpbin.testing-studio.com/get', params=payload)
        print(r.headers)
        print(r.json())
        print(r.text)
        print(r.apparent_encoding)
        print(r.cookies)
        assert r.status_code == 200
        assert r.json()['args']['name'] == 'cheny' and r.json()['args']['token'] == 'Abc700cy98UM54pyb'

    def test_post(self):
        headers = {
            "Content-Type": "application/json",
            "charset": "utf-8",
            "req-source": "doclever"
        }
        body = {
            "agtId": "80169471118MNKH",
            "mercCnm": "赣湘木桶饭",
            "orgNo": "12000",
            "addDate": "20201211",
            "mercId": "826440358148339",
            "pageNumber": 1,
            "pageSize": 10,
            "channelNo": "cmbc"

        }
        r = requests.post("http://httpbin.testing-studio.com/post", data=body)
        print(r.json())
        assert r.status_code == 200

    def test_post_file(self):
        files = {'file': open('C:\\Users\\frecy\Desktop\\test.xls', 'rb')}
        r = requests.post("http://httpbin.testing-studio.com/post", files=files)
        print(r.content)
        assert r.status_code == 200

    def test_post_form(self):
        payload = {
            'name': 'cheny',
            'token': 'Abc700cy98UM54pyb'
        }
        r = requests.post("http://httpbin.testing-studio.com/post", data=payload)
        print(r.text)
        assert r.status_code == 200

    def test_cookie(self):
        cookies = dict(cookie="adsdfskldfjsoidfj123")
        r = requests.get("http://httpbin.testing-studio.com/cookies", cookies=cookies)
        print(r.text)
        assert r.status_code == 200
        assert r.json()["cookies"]["cookie"] == "adsdfskldfjsoidfj123"

    def test_headers(self):
        headers = {
            "Content-Type": "application/json",
            "req-source": "doclever"
        }
        r = requests.get("http://httpbin.testing-studio.com/get", headers=headers)
        print(r.headers)
        assert r.status_code == 200


