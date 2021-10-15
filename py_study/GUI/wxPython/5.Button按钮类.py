# 按钮时 GUI 界面中应用最为广泛的控件，它常用于捕获用户生成的单击事件，其最明显的一个用途时出发绑定到一个处理函数。
# wxPython 类库提供不同类型的按钮，其中最简单、常用的是wx.Button类。
"""
wx.Button 类的构造函数：
wx.Button(parent, id, label, pos, size=wxDefaultSize, style=0, validator, name='button')

wx.Button 类的参数与 wx.TextCtrl 类的参数基本相同，其中参数 label 是显示在按钮上的文本
"""
import wx


class MyFrame(wx.Frame):
    def __init__(self, parent):
        wx.Frame.__init__(self, parent, title='创建TextCtrl类', pos=(600, 300), size=(500, 400))
        # 创建面板
        panel = wx.Panel(self)
        self.title = wx.StaticText(panel, label='登      录', pos=(200, 20))
        self.label_user = wx.StaticText(panel, label='用户名:', pos=(50, 50))
        self.text_user = wx.TextCtrl(panel, pos=(100, 50), size=(235, 25), style=wx.TE_LEFT)
        self.label_pwd = wx.StaticText(panel, label='密  码:', pos=(50, 100))
        self.text_pwd = wx.TextCtrl(panel, pos=(100, 100), size=(235, 25))
        # 创建“确定”和“取消”按钮
        self.bt_confirm = wx.Button(panel, label='确定', pos=(105, 150))
        self.bt_cancel = wx.Button(panel, label='取消', pos=(195, 150))


if __name__ == "__main__":
    app = wx.App()
    flame = MyFrame(parent=None)
    flame.Show()
    app.MainLoop()
