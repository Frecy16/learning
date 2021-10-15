# 控件：就是经常使用的按钮、文本、输入框、单选框等
"""
StaticText文本类：用于在屏幕上绘制纯文本
使用 wx.StaticText 类能够改变文本的对齐方式、字体和颜色等，其语法格式：
wx.StaticText(parent, id, label, pos wx.DefaultPosition, size=wx.DefaultSize,
    style=0, name='staticText')

参数说明：
    parent: 父窗口插件。
    id: 标识符，使用-1可以自动创建一个唯一的标识
    label: 显示在静态控件中的文本内容。
    pos: 一个wx.Point 或一个Python元组，它是窗口部件的位置。
    size: 要给wx.Size 或一个Python元组，它是窗口部件的尺寸。
    style: 样式标记。
    name: 对象的名称。

wx.Font类设置字体
wx.Font(pointSize, family, style, weight, underline=False, facename='',
    encoding=wx.FONTENCODING_DEFAULT)

参数说明：
    pointSize: 字体的整数尺寸，单位为磅。
    family: 用于快速指定一个字体而无须知道该字体实际的名字。
    style: 指明字体是否倾斜。
    weight: 指明字体的醒目程度。
    underline: 仅在Windows系统下有效，如果取值为True，则加下划线；False为无下划线。
    faceName: 指定字体名。
    encoding: 允许在几个编码中选择一个，大多数情况剋使用默认编码。
"""
import wx


class MyFrame(wx.Frame):
    def __init__(self, parent, id):
        wx.Frame.__init__(self, parent, id, title='创建StaticText类',
                          pos=(600, 300), size=(500, 400))
        panel = wx.Panel(self)  # 创建画板
        # 创建标题，并设置字体
        title = wx.StaticText(panel, label='Python之禅——Tim Peters', pos=(100, 20))
        font = wx.Font(16, wx.DEFAULT, wx.FONTSTYLE_NORMAL, wx.NORMAL)
        title.SetFont(font)
        # 创建文本
        wx.StaticText(panel, label='优美胜于丑陋', pos=(50, 50))
        wx.StaticText(panel, label='明了胜于晦涩', pos=(50, 70))
        wx.StaticText(panel, label='简洁胜于复杂', pos=(50, 90))
        wx.StaticText(panel, label='复杂胜于凌乱', pos=(50, 110))
        wx.StaticText(panel, label='扁平胜于嵌套', pos=(50, 130))
        wx.StaticText(panel, label='间隔胜于紧凑', pos=(50, 150))
        wx.StaticText(panel, label='可读性很重要', pos=(50, 170))
        wx.StaticText(panel, label='即使假借特例的实用性之名，也不可违背这些规则', pos=(50, 190))
        wx.StaticText(panel, label='不要包容所有错误，除非你确定需要这样做', pos=(50, 210))
        wx.StaticText(panel, label='当存在多种可能，不要尝试去猜测', pos=(50, 230))
        wx.StaticText(panel, label='而是尽量找一种，最好是唯一一种明显的解决方案', pos=(50, 250))
        wx.StaticText(panel, label='虽然这并不容易，因为你并不是 Python 之父', pos=(50, 270))
        wx.StaticText(panel, label='做也许好过不做，但不假思索就动手还不如不做', pos=(50, 290))
        wx.StaticText(panel, label='如果你无法向人描述你的方案，那肯定不是一个好方案：反之亦然', pos=(50, 310))
        wx.StaticText(panel, label='命名空间是一种绝妙的理念，我们应当多加利用', pos=(50, 330))


if __name__ == '__main__':
    app = wx.App()  # 初始化应用
    frame = MyFrame(parent=None, id=-1)  # 实例MyFrame类，并传递参数
    frame.Show()  # 显示窗口
    app.MainLoop()  # 调用MainLoop()主循环方法
