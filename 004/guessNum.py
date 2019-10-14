import random

secret = random.randint(1, 10)

print('--------- 游戏开始 ----------')
inp = input("请输入:")
inp = int(inp)
if inp == secret:
    print("you win")
else:
    while inp != secret:
        if inp > secret:
            inp = input("大了，请重新输入:")
            inp = int(inp)
        if inp < secret:
            inp = input("小了，请重新输入:")
            inp = int(inp)
        if inp == secret:
            print("you win")
            break
print('--------- 游戏结束 ----------')
