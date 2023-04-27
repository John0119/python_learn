"""
演示数据容器之：list列表的常用操作
"""
mylist = ['hi', 'hello', 'world']
# 1.1 查抄某元素在列表内的下标索引
index = mylist.index('hi')
print(f"hi在list的下表索引是{index}")

# 1.2 在指定位置插入元素
mylist.insert(1, "python")
print(f"插入后的list是{mylist}")

# 1.3 通过下表删除元素
del mylist[0]
print(f"删除后的list列表元素是{mylist}")

mylist.pop(0)
print(f"删除后的list列表元素是{mylist}")

# 1.4 在列表后面加入新的元素
mylist.append('python')
print(f"添加新元素后的list列表是{mylist}")