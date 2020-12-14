#!/usr/bin/env pyhton
# -*- coding: utf-8 -*-
# 被测文件
# 实现计算器
class Calculator:
    def add(self, a, b):
        return a + b

    def div(self, a, b):
        return a / b

    def minus(self, a, b):
        return a - b

    def multiply(self, a, b):
        return a * b

    def power(self, a):
        return a ** 2

    def sqrt(self, a):
        if a < 0:
            print("ERROR")
            return -1
        else:
            return a ** 0.5

    def cube(self, a):
        return a ** 3
