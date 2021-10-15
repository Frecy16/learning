"""
QPushButton 是 PyQt 中最普通也是常用的按钮之一，QPushButton的常用方法如下：

setText()  设置按钮所显示的文本
text()  获取按钮所显示的文本
setIcon()  设置按钮上的图标，可以将参数设置为 QtGui.QIcon('图标路径')
setIconSize()  设置按钮图标的大小，参数可以设置为QtCore.QSize(int width, int height)
setEnabled()  设置按钮是否可用，参数设置为False时，按钮为不可用状态
setShortcut()  设置按钮的快捷键，参数可以设置为键盘中的按钮或组合键，例如”'Alt+0'“

如果需要QPushButton 控件实现 1 个单击效果的时候，可以使用以下代码：
# 参数中的self.click 为单击事件所触发的方法名称
self.pushButton.clicked.connect(self.click)

QRadioButton 单选按钮
QRadioButton 也是按钮的一种，多数用于实现”二选一“ 或 ”多选一“ 的选择现象。
常用方法如下：

setText()  设置单选按钮显示的文本
text()  获取单选按钮显示的文本
setChecked()  设置单选按钮是否为选中状态，True 为选中状态
isChecked()  设置单选按钮的状态，True为选中状态，False为未选中状态
"""
from PyQt5 import QtCore, QtGui, QtWidgets


class Main_window(object):
    def radioBtn(self):
        self.radioButton.toggled.connect(lambda: self.button_state(self.radioButton))
        self.radioButton_2.toggled.connect(lambda: self.button_state(self.radioButton_2))

    def button_state(self, button):
        if button.text() == 'RadioButton1':  # 判断单选按钮的名称
            if button.isChecked() == True:  # 判断单选按钮是否被选中
                print(button.text() + '已选中')
            else:
                print(button.text() + '未选中')

        if button.text() == 'RadioButton2':
            if button.isChecked() == True:
                print(button.text() + '已选中')
            else:
                print(button.text() + '未选中')
