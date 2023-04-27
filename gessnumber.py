# 猜数字
import random
num = random.randint(1, 100)
# 用户输入数字


flag = True
count = 0

while flag:
    guess_num = int(input("请输入："))
    count += 1
    if guess_num == num:
        print("你猜中了！！")
        print(f"你一共猜了{count}次")
        flag = False
    else:
        if guess_num > num:
            print("你猜大了！")
        if guess_num < num:
            print("你猜小了！")



