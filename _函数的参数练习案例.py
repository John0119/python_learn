def check(num):
    print("欢迎来到这里，请出示你的体温。")
    if num <= 37.5:
        print(f"你的体温{num}，正常请进！")
    else:
        print(f"你的体温{num}，异常请隔离！")


check(37.4)