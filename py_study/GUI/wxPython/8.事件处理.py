# 事件：用户执行的动作就叫做事件(event),比如单击按钮，就是一个单击事件。
# 事件处理：完成布局以后，当单击”确定“和”取消“按钮，检验输入并输出相应的提示信息。
# 绑定事件：当发生一个事件，需要让程序注意这些事件并且做出反应。可以将函数绑定到所涉及事件可能发生的控件上。当发生
# 事件时，函数就会被调用，利用控件的 Bind() 方法可以将事件。
"""
bt_confirm.Bind(wx.EVT_BUTTON, OnclickSubmit)

参数说明：
    wx.EVT_BUTTON: 事件类型为按钮类型，在wxPython中有许多 wx.EVT_ 开头的事件类型，
        类型 wx.EVT_MOTION 产生于用户移动鼠标；类型 wx.ENTER_WINDOW 和 wx.LEAVE_WINDOW 产生与当鼠标进入或离开一个窗口控件；
        类型 wx.EVT_MOUSEWHEEL 被绑定到鼠标滚轮的活动。
    OnclickSubmit: 方法名。事件发生时执行该方法
"""
import wx


class MyFrame(wx.Frame):
    def OnclickSubmit(self, event):
        """ 单击 “确定” 按钮， 执行方法"""
        # message = ""
        username = self.text_user.GetValue()  # 获取输入的用户名
        password = self.text_pwd.GetValue()  # 获取输入的密码
        if username == "" or password == "":  # 判断用户名或密码是否为空
            message = '请输入用户或密码'
        elif username == 'mr' and password == 'mrsoft':  # 用户名或密码正确
            message = '登录成功'
        else:
            message = '用户名或密码错误'  # 用户名或密码错误
        wx.MessageBox(message)  # 弹出提示框

    def OnclickCancel(self, event):
        """ 单击 “取消” 按钮，执行方法 """
        self.text_user.SetValue("")  # 清空输入的用户名
        self.text_pwd.SetValue("")  # 清空输入的密码

    def __init__(self, parent, id):
        wx.Frame.__init__(self, parent, id, title='用户登录', pos=(600, 300), size=(450, 350))
        # 创建面板
        panel = wx.Panel(self)

        # 创建”确定“ 和”取消“按钮，并绑定事件
        self.bt_confirm = wx.Button(panel, label='确定')
        self.bt_confirm.Bind(wx.EVT_BUTTON, self.OnclickSubmit)
        self.bt_cancel = wx.Button(panel, label='取消')
        self.bt_cancel.Bind(wx.EVT_BUTTON, self.OnclickCancel)
        # 创建文本，左对齐
        self.title = wx.StaticText(panel, label='登      录')
        self.label_user = wx.StaticText(panel, label='用户名:')
        self.text_user = wx.TextCtrl(panel, style=wx.TE_LEFT)
        self.label_pwd = wx.StaticText(panel, label='密   码:')
        self.text_pwd = wx.TextCtrl(panel, style=wx.TE_PASSWORD)
        # 添加容器，容器中控件横向排列
        hsizer_user = wx.BoxSizer(wx.HORIZONTAL)
        hsizer_user.Add(self.label_user, proportion=0, flag=wx.ALL, border=5)
        hsizer_user.Add(self.text_user, proportion=1, flag=wx.ALL, border=5)

        hsizer_pwd = wx.BoxSizer(wx.HORIZONTAL)
        hsizer_pwd.Add(self.label_pwd, proportion=0, flag=wx.ALL, border=5)
        hsizer_pwd.Add(self.text_pwd, proportion=1, flag=wx.ALL, border=5)

        hsizer_button = wx.BoxSizer(wx.HORIZONTAL)
        hsizer_button.Add(self.bt_confirm, proportion=0, flag=wx.ALIGN_CENTER, border=5)
        hsizer_button.Add(self.bt_cancel, proportion=0, flag=wx.ALIGN_CENTER, border=5)
        # 添加容器，容器中控件纵向排列
        vsizer_all = wx.BoxSizer(wx.VERTICAL)
        vsizer_all.Add(self.title, proportion=0, flag=wx.BOTTOM | wx.TOP | wx.ALIGN_CENTER, border=15)
        vsizer_all.Add(hsizer_user, proportion=0, flag=wx.EXPAND | wx.LEFT | wx.RIGHT, border=80)
        vsizer_all.Add(hsizer_pwd, proportion=0, flag=wx.EXPAND | wx.LEFT | wx.RIGHT, border=80)
        vsizer_all.Add(hsizer_button, proportion=0, flag=wx.ALIGN_CENTER | wx.TOP, border=25)
        panel.SetSizer(vsizer_all)


if __name__ == '__main__':
    app = wx.App()
    frame = MyFrame(parent=None, id=-1)
    frame.Show()
    app.MainLoop()
