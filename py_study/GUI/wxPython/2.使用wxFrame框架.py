# 在wxPython中，wx.Frame是所有框架的父类，当创建wx.Frame的子类时，应调用其父类的构造器 wx.Frame.__init__()。
"""
wx.Frame(parent, id=-1, title="", pos=wx.DefaultPosition, size=wx.DefaultSize, style=wx.DEFAULT_FRAME_STYLE,
    name='frame')

参数说明：
    parent: 框架的父窗口，如果是顶级窗口，这个值是None。
    id: 新窗口的 wxPython ID号。通常设为-1，让 wxPython自动生成一个新的ID。
    title: 窗口的标题。
    pos: 一个wx.Point对象，它指定这个新窗口的左上角在屏幕中的位置。在图形用户界面程序中，通常 (0,0) 是显示器的左上角。
    这个默认的 (-1,-1)将让系统决定窗口的位置。
    size: 一个 wx.Size对象，它指定这个窗口的初始尺寸。这个默认的(-1,-1)将让系统决定窗口的初始尺寸。
    style: 指定窗口的类型的常量。可以使用或运算来组合它们。
    name: 框架的内在的名字，可以使用它来寻找这个窗口。
"""

# _*_ coding:utf-8 _*_
import wx


class MyFrame(wx.Frame):
    def __init__(self, parent, id):
        wx.Frame.__init__(self, parent, id, title='创建Frame', pos=(600, 300), size=(500, 400))


if __name__ == '__main__':
    app = wx.App()  # 初始化应用
    frame = MyFrame(parent=None, id=-1)  # 实例MyFrame类，并传递参数
    frame.Show()  # 显示窗口
    app.MainLoop()  # 调用MainLoop()主循环方法
