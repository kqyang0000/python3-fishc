print('--------- 游戏开始 ----------')
inp = input("请输入:")
inp = int(inp)
if inp == 8:
    print("you win")
else:
    if inp > 8:
        print("大了")
    else:
        print("小了")
print('--------- 游戏结束 ----------')
