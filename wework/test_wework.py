# import json
# import random
import re

import pytest
import requests


def test_create_data():
    """
    1、列表生成器
    2、生成器
    3、迭代器
    """
    data = [("weixiao" + str(x),
             "魏潇" + str(x),
             "152%08d" % x) for x in range(20)]
    print(data)
    return data


class Testwework:
    @pytest.fixture(scope="session")
    def token(self):
        requests_params = {
            "corpid": "ww1d0df80a9ad528de",
            "corpsecret": "8nQMZi5-VPcw1UjYPcOLQWA0g-VdLHNV5531pbIPrkk"
        }
        r = requests.get("https://qyapi.weixin.qq.com/cgi-bin/gettoken", params=requests_params)
        return r.json()["access_token"]

    def get_token(self):
        """
        获取 token
        企业id:ww1d0df80a9ad528de
        通信录api secret:8nQMZi5-VPcw1UjYPcOLQWA0g-VdLHNV5531pbIPrkk
        url : https://qyapi.weixin.qq.com/cgi-bin/gettoken?corpid=ID&corpsecret=SECRET
        """
        payload = {
            "corpid": "ww1d0df80a9ad528de",
            "corpsecret": "8nQMZi5-VPcw1UjYPcOLQWA0g-VdLHNV5531pbIPrkk"
        }
        r = requests.get("https://qyapi.weixin.qq.com/cgi-bin/gettoken", params=payload)
        # print(r.json())
        return r.json()["access_token"]

    def test_create(self, token, userid, mobile, name="释琪", department=None):
        """
        创建成员
        url: https://qyapi.weixin.qq.com/cgi-bin/user/create?access_token=ACCESS_TOKEN
        """
        # access_token = self.get_token()
        if department is None:
            department = [4]
        body = {
            "userid": userid,
            "name": name,
            "mobile": mobile,
            "department": department,
        }
        # req_body = json.dumps(body) #字典转json   json.loads() json转字典
        r = requests.post(f"https://qyapi.weixin.qq.com/cgi-bin/user/create?access_token={token}",
                          json=body)
        print(r.json())
        return r.json()

    def test_get_users(self, token):
        # access_token = self.get_token()
        r = requests.get(f"https://qyapi.weixin.qq.com/cgi-bin/user/simplelist?access_token={token}\
        &department_id=1&fetch_child=1")
        # print(r.json())
        print(r.json()["userlist"])

    def test_getmermber(self, token, userid):
        """
        获取成员信息
        https://qyapi.weixin.qq.com/cgi-bin/user/get?access_token=ACCESS_TOKEN&userid=USERID
        """
        # access_token = self.get_token()
        # userid = self.test_get_user(token)
        # payload = {"userid":"wangzhen"}
        r = requests.get(f"https://qyapi.weixin.qq.com/cgi-bin/user/get?access_token={token}&userid={userid}")
        return r.json()

    def test_update(self, token, userid, name="安琪", department=None, **kwargs):
        """
        更新成员信息
        https://qyapi.weixin.qq.com/cgi-bin/user/update?access_token=ACCESS_TOKEN
        """
        # access_token = self.get_token()
        if department is None:
            department = [3]
        body = {
            "userid": userid,
            "name": name,
            "department": department,
            "order": [1],
            **kwargs
        }
        r = requests.post(f"https://qyapi.weixin.qq.com/cgi-bin/user/update?access_token={token}", json=body)
        return r.json()

    def test_delete(self, token, userid):
        """
        删除成员
        https://qyapi.weixin.qq.com/cgi-bin/user/delete?access_token=ACCESS_TOKEN&userid=USERID
        """
        # access_token = self.get_token()
        # self.test_create(token)
        r = requests.get(f"https://qyapi.weixin.qq.com/cgi-bin/user/delete?access_token={token}&userid={userid}")
        return r.json()

    @pytest.mark.parametrize("userid,name,mobile", test_create_data())
    def test_wework_crud(self, token, userid, mobile, name):
        """
        整体测试
        """
        # userid = "kenan123"
        # name = "释琪"
        # mobile = "15800000009"
        try:
            assert "created" == self.test_create(token, userid, mobile, name)["errmsg"]
        except AssertionError as e:
            if "mobile existed" in e.__str__():
                re_userid = re.findall(":(.*)'$", e.__str__())[0]
                self.test_delete(token, re_userid)
                assert "created" == self.test_create(token, userid, mobile, name)["errmsg"]
        assert name == self.test_getmermber(token, userid)["name"]
        assert "updated" == self.test_update(token, userid, name="安琪")["errmsg"]
        assert "安琪" == self.test_getmermber(token, userid)["name"]
        assert "deleted" == self.test_delete(token, userid)["errmsg"]
        assert 60111 == self.test_getmermber(token, userid)["errcode"]
        # self.test_get_users(token)
