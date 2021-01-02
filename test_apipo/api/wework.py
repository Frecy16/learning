from test_apipo.api.baseapi import BaseApi, openfile
from test_apipo.api.util import Util


class WeWork(BaseApi):
    def __init__(self):
        self.token = Util().get_token()
        self.params["token"] = self.token

    def test_create(self, userid, mobile, name="释琪", department=None):
        """
        创建成员
        url: https://qyapi.weixin.qq.com/cgi-bin/user/create?access_token=ACCESS_TOKEN
        """
        if department is None:
            department = "4"
        self.params["userid"] = userid
        self.params["name"] = name
        self.params["mobile"] = mobile
        self.params["department"] = department
        # with open("../api/wework.yaml",'r', encoding="utf-8") as f:
        #     data = yaml.load(f, Loader=yaml.FullLoader)
        # print(data["create"])
        data = openfile()
        return self.send(data["create"])

    def test_get_users(self, department_id=1, fetch_child=1):
        # data = {
        #     "method": "get",
        #     "url": f"https://qyapi.weixin.qq.com/cgi-bin/user/simplelist?access_token={self.token}"
        #            f"&department_id={department_id}&fetch_child={fetch_child} "
        # }
        self.params["department_id"] = department_id
        self.params["fetch_child"] = fetch_child
        data = openfile()
        return self.send(data["getusers"])

    def test_getmember(self, userid):
        """
        获取成员信息
        https://qyapi.weixin.qq.com/cgi-bin/user/get?access_token=ACCESS_TOKEN&userid=USERID
        """
        # data = {
        #     "method": "get",
        #     "url": f"https://qyapi.weixin.qq.com/cgi-bin/user/get?access_token={self.token}&userid={userid}"
        # }
        self.params["userid"] = userid
        data = openfile()
        return self.send(data["getmember"])

    def test_update(self, userid, name="安琪", department=None):
        """
        更新成员信息
        https://qyapi.weixin.qq.com/cgi-bin/user/update?access_token=ACCESS_TOKEN
        """
        if department is None:
            department = "4"
        self.params["userid"] = userid
        self.params["name"] = name
        self.params["department"] = department
        data = openfile()
        return self.send(data["update"])

    def test_delete(self, userid):
        """
        删除成员
        https://qyapi.weixin.qq.com/cgi-bin/user/delete?access_token=ACCESS_TOKEN&userid=USERID
        """
        self.params["userid"] = userid
        data = openfile()
        return self.send(data["delete"])
