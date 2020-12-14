#!/usr/bin/env pyhton
# -*- coding: utf-8 -*-
# 测试文件
from pythoncode.calc import Calculator


class TestCalculator():
    cal = Calculator()

    def test_add(self):
        assert 2 == self.cal.add(1, 1)

    def test_power(self):
        assert 4 == self.cal.power(2)

    def test_sqrt(self):
        assert 3 == self.cal.sqrt(9)

    def test_cube(self):
        assert 27 == self.cal.cube(3)
