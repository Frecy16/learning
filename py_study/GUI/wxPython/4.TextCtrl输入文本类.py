# wx.StaticText 类只能显示静态文本，但有时需要交互，就需要使用输入文本类wx.TextCtrl
# wx.TextCtrl 允许输入单行或多行文本，可以作为密码输入空间，掩饰所按下的按键
"""
wx.TextCtrl 类的构造函数语法格式如下：
wx.TextCtrl(parent, id, value='', pos=wx.DefaultPosition, size=wx.DefaultSize,
    style=0, validator=wx.DefaultValidator, name=wx.TextCtrlNameStr)

参数说明：
    parent,id,pos,size,style和name 与 wx.StaticText构造函数相同。
    style: 单行 wx.TextCtrl的样式，取值及说明如下：
        wx.TE_CENTER: 控件中的文本剧中。
        wx.TE_LEFT: 控件中的文本左对齐，默认行为。
        wx.TE_NOHIDESEL: 文本始终高亮显示，只适用于 Windows。
        wx.TE_PASSWORD: 不显示所键入的文本呢，以星号（*）代替显示。
        wx.TE_PROCESS_ENTER: 如果使用该参数，那么当用户在控件内按下<Enter>键时，一个文本输入事件将被触发；否则，
        按键事件内在的由该文本控件或该对话框管理。
        wx.TE_PROCESS_TAB: 如果指定了这个样式，那么通常的字符事件在 <Tab>键按下时创建（一般意味着一个制表符将被插入文本）；否则
        <Tab>键由对话框来管理，通常是控件间的切换。
        wx.TE_READONLY: 文本控件为只读，用户不能修改其中的文本。
        wx.TE_RIGHT: 控件中的文本右对齐。
    value: 显示在该控件中的初始文本。
    validator: 常用于过滤数据以确保只能键入要接收的数据。
"""
import wx


class MyFrame(wx.Frame):
    def __init__(self, parent):
        wx.Frame.__init__(self, parent, title='创建TextCtrl类', pos=(600, 300), size=(500, 400))
        # 创建面板
        panel = wx.Panel(self)
        # 创建文本和输入狂
        self.title = wx.StaticText(panel, label='登  录', pos=(200, 20))
        self.label_user = wx.StaticText(panel, label='用户名', pos=(50, 50))
        self.text_user = wx.TextCtrl(panel, pos=(100, 50), size=(235, 25), style=wx.TE_LEFT)
        self.label_pwd = wx.StaticText(panel, label='密 码', pos=(50, 90))
        self.text_password = wx.TextCtrl(panel, pos=(100, 90), size=(235, 25), style=wx.TE_PASSWORD)


if __name__ == '__main__':
    app = wx.App()
    frame = MyFrame(parent=None)
    frame.Show()
    app.MainLoop()
