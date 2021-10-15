def tell_story(place, person1, person2):
    print("从前有座山")
    print("山里有座%s" % place)
    print("%s里有个%s" % (place, person1))
    print("还有一个%s" % person2)
    print("%s在%s讲故事" % (person1, person2))
    print("故事的内容是：")


# age = int(input('请输入孩子的年龄：\n'))
# if 0 <= age <= 3:
#     for i in range(5):
#         tell_story('尼姑庵', '师太', '小尼姑')
# elif 3 < age <= 5:
#     tell_story('道观', '老道', '童子')  # 会把实参一一对应的传递，交给形参处理
# else:
#     print("别用这个故事忽悠了，换个花样吧")

# 还可以通过定义变量名的形式给形参赋值
tell_story(person2='青年', person1='禅师', place='武当山')
