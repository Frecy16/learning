# -*-coding:utf8-*-
from jsonpath import jsonpath
import requests
import pystache
from hamcrest import *

URL = 'http://httpbin.testing-studio.com'
class TestApi:
    # url = 'http://httpbin.testing-studio.com'
    def test_get(self):
        payload = {'name': 'cheny', 'token': 'Abc700cy98UM54pyb'}
        r = requests.get(URL + '/get', params=payload)
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
        r = requests.post(URL + "/post", data=body)
        print(r.json())
        assert r.status_code == 200

    def test_post_file(self):
        files = {'file': open(r'C:\Users\frecy\Desktop\test.xls', 'rb')}
        r = requests.post(URL + "/post", files=files)
        print(r.content)
        assert r.status_code == 200

    def test_post_form(self):
        payload = {
            'name': 'cheny',
            'token': 'Abc700cy98UM54pyb'
        }
        r = requests.post(URL + "/post", data=payload)
        print(r.text)
        assert r.status_code == 200

    def test_cookie(self):
        cookies = dict(cookie="adsdfskldfjsoidfj123")
        r = requests.get(URL + "/cookies", cookies=cookies)
        print(r.text)
        assert r.status_code == 200
        assert r.json()["cookies"]["cookie"] == "adsdfskldfjsoidfj123"

    def test_headers(self):
        headers = {
            "Content-Type": "application/json",
            "req-source": "doclever"
        }
        r = requests.get(URL + "/get", headers=headers)
        print(r.headers)
        assert r.status_code == 200

    def test_post_json(self):
        payload = {"lever": 1, "name": "cheny"}
        r = requests.post(URL + '/post', json=payload)
        print(r.json())
        assert r.status_code == 200
        assert r.json()["json"]["lever"] == 1

    def test_xml(self):
        xml = """<?xml version='1.0' encoding='urf-8'?>
        <a>*</a>"""
        headers = {"Content-Type": "application/xml"}
        r = requests.post('http://httpbin.org/post', data=xml, headers=headers).text
        print(r)

    def test_mustache(self):
        r = pystache.render(
            'Hi {{person}}',
            {'person': 'cheny'}
        )
        print(r)
        assert r == 'Hi cheny'

    def test_jsonpath(self):
        r = requests.get('https://ceshiren.com/latest.json')
        print(r.json())
        assert r.status_code == 200
        # print(jsonpath(r.json(), '$..name'))
        assert jsonpath(r.json(), '$..name')[1] == '思寒'

    def test_hamcrest(self):
        r = requests.get('https://ceshiren.com/latest.json')
        print(r.json())
        assert_that(r.status_code, equal_to(200))
        assert_that(r.json()['users'][1]['username'], equal_to('seveniruby'))
