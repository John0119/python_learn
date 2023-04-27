"""
tuple元组定义和操作
"""

# 定义元组
t1 = (1, 'hello', True)
t2 = ()
t3 = tuple()
print(f"t1的类型是：{type(t1)}，内容是：{t1}")
print(f"t2的类型是：{type(t2)}，内容是：{t2}")
print(f"t3的类型是：{type(t3)}，内容是：{t3}")


# 定义单个元素的元组
t4 = ("hello", )
print(f"t4的类型是：{type(t4)}，内容是：{t4}")


# 元组的嵌套
t5 = ((1, 2, 3), (4, 5, 6))
print(f"t5的类型是：{type(t5)}，内容是：{t5}")
# 通过下表索引
num = t5[1][2]
print(f"t5[1][2]={num}")


# 元组的操作：index查找方法
t6 = (1, 2, "hello", 3, 4, "hello")
print(t6.index("hello"))
# 元组的操作：count统计方法
print(t6.count("hello"))
# 元组的操作：len函数统计元组元素数量
print(len(t6))
# 元组的遍历：while
index = 0
while index < len(t6):
    print(f"元组的元素有：{t6[index]}")
    index += 1

# 元组的遍历：for
for element in t6:
    print(f"元组的元素有：{element}")