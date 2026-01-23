from time import *
def encode(a, b, c, d, e):
    start_time = time()
    assert 0 < a <= 8, f"维度1超出范围,必须在(0,8]，你输入了{a}"
    assert 0 < b <= 8, f"维度2超出范围,必须在(0,8]，你输入了{b}"
    assert 0 < c <= 8, f"维度3超出范围,必须在(0,8]，你输入了{c}"
    assert 0 < d <= 6, f"维度4超出范围,必须在(0,6]，你输入了{d}"
    assert 0 < e <= 5, f"维度5超出范围,必须在(0,5]，你输入了{e}"
    token = (a - 1) * 8 * 8 * 6 * 5 + (b - 1) * 8 * 6 * 5 + (c - 1) * 6 * 5 + (d - 1) * 5 + (e - 1)
    end_time = time()
    return token, f"程序执行的时间是：{end_time - start_time} 秒"

set = list(map(int, input("请输入坐标,一共5个维度，维度1-3范围是(0, 8]，维度4范围是(0, 6]，维度5范围是(0, 5]：").split(" ")))

try:
    if len(set) != 5:
        print("请输入5个维度的坐标信息")
    elif set[0] <= 0 or set[0] > 8:
        print("维度1超出范围,必须在(0,8]")
    elif set[1] <= 0 or set[1] > 8:
        print("维度2超出范围,必须在(0,8]")
    elif set[2] <= 0 or set[2] > 8:
        print("维度3超出范围,必须在(0,8]")
    elif set[3] <= 0 or set[3] > 6:
        print("维度4超出范围,必须在(0,6]")
    elif set[4] <= 0 or set[4] > 5:
        print("维度5超出范围,必须在(0,5]")
    else:
        print(encode(int(set[0]), int(set[1]), int(set[2]), int(set[3]), int(set[4])))
except IndexError:
    print("请输入正确的坐标信息")

# print(set, type(set), type(set[0]))