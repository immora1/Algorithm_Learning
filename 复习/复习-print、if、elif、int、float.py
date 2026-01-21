"""
# 开始复习

s = "Hello World!"
print(len(s))
print(s[-1], s[11], s[2:5], s[4: 7])
float_num = 1.2345
int_num = 21212
a = int(float_num)
print(type(s), type(len(s)), type(float_num), type(int_num), a, type(a))

# print(123)、print(3.14) 都可以；print() 会对参数调用 str() 得到可显示的文本再输出。
# 只有在“字符串拼接”时才需要显式转换："值=" + str(123)；更推荐 f"值={123}" 或 print("值=", 123)。
print(float_num)
print(f"值={float_num}")
"""

a = 1
b = 2
i = 0
for c in range(10):
    if i < 5:
        i += a
        print(i)
    elif i == 5:
        i += b
        print(i)
    elif i >= 6:
        a += b
        b += i
        i += a
        print(f"a = {a}, b = {b}, i = {i}")









