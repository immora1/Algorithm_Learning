
from time import *

# start_time = time()
# for a in range(1, 1001):
#     for b in range(1, 1001):
#         for c in range(1, 1001):
#             if a + b + c == 1000 and a ** 2 + b ** 2 == c ** 2:
#                 print("找到结果 a, b, c: {}, {}, {}".format(a, b, c))

# end_time = time()
# print(f"程序执行的时间是：{end_time - start_time} 秒")



def imm(a):
    start_time = time()
    a += 1
    end_time = time()
    return a, f"程序执行的时间是：{end_time - start_time} 秒"

print(imm(9)[0])
print(imm(9)[1])
print(type(imm(19)))
