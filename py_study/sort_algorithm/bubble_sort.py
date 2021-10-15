#!/usr/bin/env pip的使用.md
# -*- coding: utf-8 -*-

def bubbleSort(arr):
    # 遍历所有数组元素
    for i in range(len(arr)):
        flag = True
        for j in range(0, len(arr) - i - 1):

            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                flag = False
        if flag:
            break


ori_arr = [2, 15, 5, 9, 7, 6, 4, 12, 5, 4, 2, 64, 5, 6, 4, 2, 3, 54, 45, 4, 44]
bubbleSort(ori_arr)
print("排序后的数组：", ori_arr)
