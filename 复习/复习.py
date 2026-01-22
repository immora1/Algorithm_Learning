
# # 开始复习

# # ————————————————————————————————————————————————————————————————————————————————————————————————————
# s = "Hello World!"
# print(len(s))
# print(s[-1], s[11], s[2:5], s[4: 7])
# float_num = 1.2345
# int_num = 21212
# a = int(float_num)
# print(type(s), type(len(s)), type(float_num), type(int_num), a, type(a))

# # print(123)、print(3.14) 都可以; print() 会对参数调用 str() 得到可显示的文本再输出。
# # 只有在“字符串拼接”时才需要显式转换："值=" + str(123)；更推荐 f"值={123}" 或 print("值=", 123)。
# print(float_num)
# print(f"值={float_num}")


# # ————————————————————————————————————————————————————————————————————————————————————————————————————
# from math import *

# a = 1
# b = 2
# c = 0
# for i in range(10):
#     if i < 5:
#         c += 2 * a
#         print(c)
#     elif i == 5:
#         c += b
#         print(c)
#     elif i >= 6:
#         a += b
#         b += c
#         c += a
#         print(f"a = {a}, b = {b}, c = {c}")

# c = log2(10)
# d = 2 ** 3

# print(c, d, type(c), type(d))

# # ————————————————————————————————————————————————————————————————————————————————————————————————————
# a = input("请输入数字：")
# print(a, type(a))


# def test(a, b):
#     c = a + b ** 2
#     print(c)
# test(1, 4)


# # ————————————————————————————————————————————————————————————————————————————————————————————————————
# # 定义简单函数的时候修改“形参”，不会改变“实参”。 但是使用复杂函数的时候修改“形参”，会改变“实参”。
# x = 10
# def foo(y):
#     y += 1
#     return y
# print(x, foo(x))

# # 用复杂函数(eg：list，dict，tenple)的时候修改“形参”，会改变“实参”。
# x = [10, 20, 30]
# z = [10, 20, 30]
# def foo_1(y):
#     y[0] += 1
#     return y
# print(x, foo_1(x), end="\n")

# # 可以通过使用 [:] 创建一个副本来避免修改“实参”。z[:]相当于将z复制了一份。
# print(z, foo_1(z[:]))


# # ————————————————————————————————————————————————————————————————————————————————————————————————————
# # 一个“*”代表输出一个‘元组’——*args——args可以替换成任何词。
# def imm_1(*args):
#     print(args[0],args)

# # 但是这样不会修改实参
# a = imm_1(1,2,3,4,5)
# b = imm_1(6,7,8,9,10)


# # 两个“*”代表输出一个‘字典’——**args——args可以替换成任何词。
# def imm_2(**args):
#     for key, value in args.items():
#         print(key, value)
#     print(args)
# imm_2(name="zhangsan", age=18, sex="male")

# # ————————————————————————————————————————————————————————————————————————————————————————————————————
# def imm_3(a, b):
#     return a + b

# def imm_4(a, b):
#     c = a * b

# # 没有return就变成None，有return就返回
# print(imm_3(1, 2), imm_4(1, 2))
# print(type(imm_3(1, 2)), type(imm_4(1, 2)))

# # return可以返回：数值，字符串，布尔值，列表，元组，字典，集合，函数等。没写return就自动返回None。


# # ————————————————————————————————————————————————————————————————————————————————————————————————————
# # 需要分清全局变量和局部变量。这是两个不同的空间，函数内部可以使用全局变量，但是函数外部不可以使用局部变量。
# a = 1
# def imm_5():
#     a = 2
#     print(a)

# # 当函数内部有与函数外边同名的变量时，会创建一个新的局部变量，就不会使用全局变量了。
# n = 123
# def imm_6():
#     n = 321
#     print(n)

# imm_6()
# print(n)

# # 可以通过使用 global 关键字来修改全局变量。
# b = 121
# def imm_7():
#     global b
#     b = 100
#     print(b)

# imm_7()
# print(b)

# # ————————————————————————————————————————————————————————————————————————————————————————————————————


# # 对象和类

# # 对象就是字典
# stu1 = {'name' : "zhangsan", 'age' : 18, 'sex' : "male", 'score' : 100}
# stu2 = {'name' : "lisi", 'age' : 19, 'sex' : "female", 'score' : 90}
# stu3 = {'name' : "wangwu", 'age' : 20, 'sex' : "male", 'score' : 80}


# # 类，用于描述对象的一个模板
# class student:
#     def __init__ (self, a, b, c, d):
#         self.name = a
#         self.age = b
#         self.sex = c
#         self.score = d

#     def state(self):
#         print("listen")
#     def write(self):
#         print("write")

# # 类（）就是把类当成一个函数，这就相当于变成一个‘对象’或‘实例’或‘变量’
# a = student("liuzi", 18, "male", 100)
# b = student("yifei", 19, "female", 90)
# c = student("yuanyu", 20, "male", 80)
# print(a.__dict__.items()[0])


# # ————————————————————————————————————————————————————————————————————————————————————————————————————


# # 面向对象的封装与私有属性

# class imm:
#     def __init__(self, a):
#         self.n = a
#     def foo1(self):
#         return self.n
#     def foo2(self):
#         self.n += 1


# # 这样n就可以在这个类里面的当成一个局部变量，不会影响全局变量也不会被全局变量改变。但是如果直接使用 " a.n = 100 " 也可能会改变局部变量。
# a = imm(10)
# a.foo2()
# print(a.foo1())


# # 因此需要二借用私有属性

# class imm_1:
#     def __init__(self, a):
#         self.__n = a
#     # 这里set_n可以改成其他名称“a”、“b”
#     # 必须通过这个内置函数来修改私有属性。使用私有属性的原因是可以在定义里面加条件判断来增加数据的安全性。
#     def set_n(self, b):
#         if b >= 100:
#             self.__n = b
#         else:
#             print("error")   
#     # 同理如果想获取返回值，也可以添加条件判断来增加数据的安全性。
#     def get_n(self):
#         return self.__n
#     def foo(self):
#         self.__n += 1


# a = imm_1(10)

# a.foo()
# print(a.get_n())
# # 因为变成私有属性，所以不能直接通过 “a.__n = 100” 来修改n的值
# a.__n = 100
# print(a.get_n())

# a.set_n(100)
# print(a.get_n())
# # 未能达到改变的阈值，所以不允许改变n的值
# a.set_n(50)
# print(a.get_n())


# # ————————————————————————————————————————————————————————————————————————————————————————————————————




class imm:
    def __init__(self, a):
        self.__n = a
    # 使用@property装饰器来简化上面的代码
    @property
    def n(self):
        return self.__n
    # 通过使用@.setter 和 @.deleter 来分别设置和删除属性。
    @n.setter
    def n(self, b):
        if b >= 0:
            self.__n = b
        else:
            print("error")

    @n.deleter
    def n(self):
        self.__n = 0

a = imm(10)
print(a.n)      # 获取值: 10
a.n = 20        # 设置值
print(a.n)      # 20
del a.n         # 删除/重置值
print(a.n)      # 0




