# 函数的初体验
str1 = "hello,world"
str2 = "iscast"
str3 = "welcomepython"


# 定义一个计算字符串长度的函数my_len

def my_len(data):
    count = 0
    for i in data:
        count += 1
    print(f"字符串{data}长度是：{count}")


my_len(str1)
my_len(str2)
my_len(str3)
