"""
pygame 常用模块：

pygame.cdrom: 访问光驱
pygame.cursors: 加载光驱
pygame.display: 访问显示设备
pygame.draw: 绘制形状、线和点
pygame.event: 管理事件
pygame.font: 使用字体
pygame.image: 加载和存储图片
pygame.joystick: 使用游戏手柄或者类似的东西
pygame.key: 读取键盘按键
pygame.mixer: 声音
pygame.mouse: 鼠标
pygame.movie: 播放视频
pygame.music: 播放音频
pygame.overlay: 访问高级视频叠加
pygame.rect: 管理矩形区域
pygame.sndarray: 操作声音数据
pygame.sprite: 操作移动图像
pygame.surface: 管理图像和屏幕
pygame.surfarray: 管理点阵图像数据
pygame.time: 管理时间和帧信息
pygame.transform: 缩放和移动图像
"""
# _*_ coding:utf-8 _*_
import pygame
import sys

# print(pygame.version)
pygame.init()  # 初始化pygame
size = width, height = 320, 240  # 设置窗口
screen = pygame.display.set_mode(size)  # 显示窗口

# 执行死循环，确保窗口一直显示
while True:
    # 检查事件
    for event in pygame.event.get():  # 遍历所有事件
        if event.type == pygame.QUIT:  # 如果单击关闭窗口，则退出
            sys.exit()

# pygame.quit()  # 退出pygame
