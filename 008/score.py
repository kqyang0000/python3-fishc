score = int(input('请输入分数：'))
if 100 >= score >= 90:
    print('A')
elif 90 > score >= 80:
    print('B')
elif 80 > score >= 70:
    print('C')
elif 70 > score >= 0:
    print('D')
else:
    print('输入错误')
