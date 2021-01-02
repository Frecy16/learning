from test_apipo.api.wework import WeWork
import pytest


# pytest testcase -s   # cd 进入要执行的用例所在目录，用命令执行
class TestWework:
    def test_get_token(self):
        print(WeWork().test_getmember("3431108"))

    def test_get_users(self):
        print(WeWork().test_get_users(3, 0))

    def test_create(self):
        print(WeWork().test_create("angler2", "15800001002", "安琪"))

    def test_get_member(self):
        print(WeWork().test_getmember("angler2"))

    def test_update(self):
        print(WeWork().test_update("angler2", "安琦", 4))

    def test_delete(self):
        print(WeWork().test_delete("angler2"))

    def test_dict(self):
        a = {"kk": 10, "ff": 20}

        def tmp(kk, ff):
            print(kk, ff)

        tmp(**a)
