# QLineEdit 是单行文本框，只能输入单行字符串。QTextEdit 控件是多行文本框，可以输入多行字符串。
"""
QLineEdit 常用方法：

setTextI()  设置文本框内显示的内容
text()  获取文本框内容
setPlaceholderText()  获取文本框内容
setMaxLength()  设置允许文本框内输入字符的最大长度
setEchoMode()  设置文本框希纳是字符的模式，有以下 4 种 模式：
    QLineEdit.Normal: 显示输入的字符，这是默认设置。
    QLineEdit.NoEcho: 不显示任何输入的字符，适用于即使密码长也需要保密的密码。
    QLineEdit.Password: 显示与平台相关的密码掩码，而不是实际输入的字符。
    QLineEdit.PasswordEchoOnEdit: 在编辑时显示字符，失去焦点后显示密码掩码字符。
clear()  清除文本框内容

QTextEdit 多行文本开给你控件，可以显示多行的文本内容，当文本内容超过控件的显示范围时，该控件将希纳是垂直滚动条。
QTextEdit 控件不仅可以显示文本内容，还可以显示 HTML 文档信息。
QTextEdit 的常用方法如下：

setPlainText()  设置文本内容
toPlainText()  获取文本内容
setTextColor()  设置文本颜色，例如，红色可以将参数设置为QtGui.QColor(255,0,0)
setTextBackgroundColor()  设置文本的背景颜色，颜色参数与setTextColor()相同
setHtml()  设置 HTML 文档内容
toHtml()  获取 HTML 文档内容
wordWrapMode()  设置自动换行
clear()  清除所有内容
"""
