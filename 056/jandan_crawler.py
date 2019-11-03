import os
from urllib import request
import time
import random

path = '/Users/yangkaiqiang/Desktop/images/'
prefix = 'MjAxOTExMDIt'
suffix = '=#comments'
encrypt_pages = {
    '1': 'MQ=', '2': 'Mg=', '3': 'Mw=', '4': 'NA=', '5': 'NQ=', '6': 'Ng=', '7': 'Nw=', '8': 'OA=', '9': 'OQ=',
    '10': 'MTA', '11': 'MTE', '12': 'MTI', '13': 'MTM', '14': 'MTQ', '15': 'MTU', '16': 'MTY', '17': 'MTc', '18': 'MTg',
    '19': 'MTk',
    '20': 'MjA', '21': 'MjE', '22': 'MjI', '23': 'MjM', '24': 'MjQ', '25': 'MjU', '26': 'MjY', '27': 'Mjc', '28': 'Mjg',
    '29': 'Mjk',
    '30': 'MzA', '31': 'MzE', '32': 'MzI', '33': 'MzM', '34': 'MzQ', '35': 'MzU', '36': 'MzY', '37': 'Mzc', '38': 'Mzg',
    '39': 'Mzk',
    '40': 'NDA', '41': 'NDE', '42': 'NDI', '43': 'NDM', '44': 'NDQ', '45': 'NDU', '46': 'NDY', '47': 'NDc', '48': 'NDg',
    '49': 'NDk',
    '50': 'NTA', '51': 'NTE', '52': 'NTI', '53': 'NTM', '54': 'NTQ', '55': 'NTU', '56': 'NTY', '57': 'NTc', '58': 'NTg',
    '59': 'NTk',
    '60': 'NjA', '61': 'NjE', '62': 'NjI', '63': 'NjM', '64': 'NjQ', '65': 'NjU', '66': 'NjY', '67': 'Njc', '68': 'Njg',
    '69': 'Njk',
    '70': 'NzA', '71': 'NzE', '72': 'NzI', '73': 'NzM', '74': 'NzQ', '75': 'NzU', '76': 'NzY', '77': 'Nzc', '78': 'Nzg',
    '79': 'Nzk'
}


def url_open(url):
    proxies = ['119.23.21.39:80', '52.80.131.144:8001', '140.143.60.228:8001', '119.147.212.247:8866',
               '183.57.44.62:808']
    proxy = random.choice(proxies)

    proxy_support = request.ProxyHandler({'http:': proxy})
    opener = request.build_opener(proxy_support)
    request.install_opener(opener)

    req = request.Request(url)
    req.add_header('User-Agent', 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_4) AppleWebKit/605.1.15 (KHTML, '
                                 'like Gecko) Version/12.1 Safari/605.1.15')
    return request.urlopen(req).read()


def get_page(url):
    html = url_open(url).decode('utf-8')
    start = html.find('current-comment-page') + 23
    end = html.find(']', start)
    print('总页数' + html[start:end])
    return html[start:end]


def find_imgs(page_url):
    img_addrs = []

    html = url_open(page_url).decode('utf-8')
    start = html.find('img src=')

    while start != -1:
        end = html.find('.jpg', start, start + 255)
        if end != -1:
            img_addrs.append('http:' + html[start + 9:end + 4])
        else:
            end = start + 9
        start = html.find('img src=', end)

    for each in img_addrs:
        print(each)
    return img_addrs


def save_imgs(img_addrs):
    for each in img_addrs:
        filename = each.split('/')[-1]
        with open(filename, 'wb') as f:
            img = url_open(each)
            f.write(img)


def download(i):
    os.mkdir(path + i)
    os.chdir(path + i)

    # url = 'http://jandan.net/ooxx/'
    url = 'http://jandan.net/' + i + '/'
    pages = int(get_page(url))

    for p in range(pages):
        index = str(int(p) + 1)
        page_url = url + prefix + encrypt_pages[index] + suffix
        print('第 %s 页' % index)
        img_addrs = find_imgs(page_url)
        save_imgs(img_addrs)
        time.sleep(3)


if __name__ == '__main__':
    inp = input("请输入爬取文件类型：")
    download(inp)
