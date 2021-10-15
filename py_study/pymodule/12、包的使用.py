# 可以将多个具有相似或者有关联的多个模块放到一个文件夹里，便于统一管理
# 这个文件夹，我们就可以称之为包
# python包里，会有一个 __init__.py
from chat import receive_message
from chat.send_message import x

# import chat
print(receive_message.y)
print(x)
