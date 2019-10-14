print('--------- 游戏开始 ----------')
inp = input("请输入:")
inp = int(inp)
while inp != 8:
    inp = input("猜错了，请重新输入:")
    inp = int(inp)
    if inp == 8:
        print("you win")
    else:
        if inp > 8:
            print("大了")
        else:
            print("小了")
print('--------- 游戏结束 ----------')
