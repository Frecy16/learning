# -*- coding:utf-8 -*-
# GUI 是 Graphical User Interface 图形用户界面的缩写，是与程序交互的一种不同的方式
# GUI的程序3要素：输入、处理和输出
"""
wxPython: Python语言的一套优秀的GUI图形库，可以很方便地创建完整的、功能健全的GUI用户界面
Kivy: 是一个开源工具包能够让使用相同源代码创建的程序跨平台运行，主要关注创新型用户界面开发，如多点触摸应用程序
Flexx: 纯Python工具包，用来创建图形化界面应用程序，可使用Web技术进行界面的渲染
PyQt: 是Qt 库的Python版本，支持跨平台
Tkinter: 也叫Tk接口，是Tk图形用户界面工具包标准的Python接口，一个轻量级的跨平台图形用户界面开发工具
Pywin32: Windows Python32 允许像VC一样的形式来使用Python开发win32应用
PyGTK: 可以用 Python轻松创建具有图形用户界面的程序
pyui4win: 一个开源的采用自绘技术的界面库
"""
import wx


class App(wx.App):
    # 初始化方法
    def OnInit(self):
        frame = wx.Frame(parent=None, title='Hello wxPython')  # 创建窗口
        frame.Show()  # 显示窗口
        return True  # 返回值


if __name__ == "__main__":
    app = App()  # 创建App类的实例
    app.MainLoop()  # 调用 App类的MainLoop()主循环方法
