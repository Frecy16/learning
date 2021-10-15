# 使用文本或按钮等控件通过pos参数布置在panel画板上，虽然容易理解，但过程麻烦，且位置是绝对位置，调整窗口大小后，界面会变得不美观
# 在 wxPython中，有一种更智能的布局方式——sizer（尺寸器），它是用于自动布局一组窗口控件的算法。
# sizer被附加到一个容器中，通常是一个框架或面板。在父容器中创建的子窗口控件必须被分别添加到sizer中。当sizer 被附加到容器时，
# 它随后就可以管理它所包含的子布局
"""
wxPython 提供了5个 sizer：
BoxSizer: 在一条水平或垂直线上的窗口部件的布局。当尺寸改变时，控制窗口部件的行为上很灵活。通常用于嵌套的样式。可用于几乎任何类型的布局。
GridSizer: 一个十分基础的网格布局。当要放置的窗口部件都是同样的尺寸且整齐地放入一个规则的网格中时可以使用它。
FlexGridSizer: 对GridSizer 稍微做了些改变，当窗口部件有不同的尺寸时，可以有更好的结果。
GridBagSizer: GridSizer系列中最灵活的成员，是的网格中的窗口部件可以更随意地放置。
StaticBoxSizer: 一个标准的Box Sizer. 带有标题和环线。
"""
"""
Add() 方法的语法格式如下：
Box.Add(control, proportion, flag, border)

参数说明：
    control: 要添加的控件。
    proportion: 添加的控件在定义的定位方式上方向占据的控件比例。
    flag: 与border参数结合使用指定边距宽度，包括如下选项：
        wx.LEFT: 左边距。
        wx.RIGHT: 右边距。
        wx.BOTTOM: 底边距。
        wx.TOP: 上边距。
        wx.ALL: 上下左右 4 个边距。
        可以通过"|"操作符来联合使用这些标志，比如"wx.LEFT|wx.BOTTOM".
        flag 参数还可以与 proportion 参数结合，指定控件本身的对齐(排列) 方式，包括以下方选项：
        wx.ALIGN_LEFT: 左边对齐
        wx.ALIGN_RIGHT: 右边对齐。
        wx.ALIGN_TOP: 顶部对齐。
        wx.ALIGN_BOTTOM: 底边对齐。
        wx.ALIGN_CENTER_VERTICAL: 垂直对齐。
        wx.ALIGN_CENTER_HORIZONTAL: 水平对齐。
        wx.ALIGN_CENTER: 居中对齐。
        wx.EXPAND: 添加控件将占有sizer 定位方向上所有可用的空间。
    border: 控制所添加控件的边距，就是在部件之间添加一些像素的空白。
"""
# _*_ coding:utf8 _*_
import wx


class MyFrame(wx.Frame):
    def __init__(self, parent, id):
        wx.Frame.__init__(self, parent, id, title='用户登录', pos=(600, 300), size=(500, 400))
        # 创建面板
        panel = wx.Panel(self)
        self.title = wx.StaticText(panel, label="登      录", pos=(50, 50))
        # 添加容器，容器中的控件按钟祥排列
        vsizer = wx.BoxSizer(wx.VERTICAL)  # 创建一个wx.BoxSizer, wx.HORIZONTAL 垂直，wx.VERTICAL 水平
        # 使用 Add() 方法将控件加入sizer
        vsizer.Add(self.title, proportion=0, flag=wx.BOTTOM | wx.TOP | wx.ALIGN_CENTER, border=15)
        panel.SetSizer(vsizer)  # 使用SetSizer() 设定尺寸器


if __name__ == '__main__':
    app = wx.App()
    flame = MyFrame(parent=None, id=-1)
    flame.Show()
    app.MainLoop()
