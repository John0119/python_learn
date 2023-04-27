"""
演示list列表的循环，用while和for两种循环方式
"""


def list_while_func():
    """
    使用while循环遍历列表
    :return: None
    """

    my_list = ["hello", "python", "world"]
    # 循环控制变量通过下标索引来控制，默认0
    # 每一次循环将下标+1
    # 循环条件：下表索引变量 < 列表的元素数量

    # 定义一个变量来标记列表的下标
    index = 0
    while index < len(my_list):
        element = my_list[index]
        print(f"遍历的元素是{element}")
        index += 1


def list_for_func():
    """
    使用for循环遍历列表
    :return: None
    """

    my_list = ["hello", "python", "world"]
    # for 变量 in 容器
    for element in my_list:
        print(f"列表的变量有{element}")


"""
举一反三
"""


def list_func(data):
    for element in data:
        print(f"列表的变量有{element}")


my_list = ['1', '2', '3', '4']
list_func(my_list)