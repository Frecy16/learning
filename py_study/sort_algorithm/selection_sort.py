#!/usr/bin/env python
# -*- coding: utf-8 -*-


def selectionSort(arr):
    for i in range(len(arr) - 1):
        minIndex = i  # 记录最小数的索引
        for j in range(i + 1, len(arr)):
            if arr[j] < arr[minIndex]:
                minIndex = j
        arr[i], arr[minIndex] = arr[minIndex], arr[i]
    return arr


ori_arr = [2, 15, 5, 9, 7, 6, 4, 12, 5, 4, 2, 64, 5, 6, 4, 2, 3, 54, 45, 4, 44]
selectionSort(ori_arr)
print("排序后的数组：", ori_arr)
