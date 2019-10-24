def save_file(boy, girl, count):
    file_name_boy = '/Users/yangkaiqiang/Desktop/boy_' + str(count) + '.txt'
    file_name_girl = '/Users/yangkaiqiang/Desktop/girl_' + str(count) + '.txt'

    boy_file = open(file_name_boy, 'w')
    girl_file = open(file_name_girl, 'w')

    boy_file.writelines(boy)
    girl_file.writelines(girl)

    boy_file.close()
    girl_file.close()


def split_file(file_name):
    f = open(file_name)

    boy = []
    girl = []
    count = 1

    for each_line in f:
        if each_line[:6] != '======':
            (role, line_speak) = each_line.split(':', 1)
            if role == 'aaa':
                boy.append(line_speak)
            if role == 'bbb':
                girl.append(line_speak)
        else:
            save_file(boy, girl, count)

            boy = []
            girl = []
            count += 1

    save_file(boy, girl, count)
    f.close()


split_file('/Users/yangkaiqiang/Desktop/readme')
