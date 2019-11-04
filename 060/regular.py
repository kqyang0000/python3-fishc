from urllib import request
import re

path = '/Users/yangkaiqiang/Desktop/images/nvshen/'


def url_open(url):
    req = request.Request(url)
    req.add_header('User-Agent', 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_4) AppleWebKit/605.1.15 (KHTML, '
                                 'like Gecko) Version/12.1 Safari/605.1.15')
    req.add_header('Referer', url)
    return request.urlopen(req).read()


def get_img(html):
    p = r'<img src="(http://[^"]+\.jpg)"'
    img_list = re.findall(p, html)

    for i in img_list:
        i = str(i).replace('-2', '').replace('kaifa.com', 'demo.com:8010')
        print(i)
        file_name = i.split('/')[-1]

        with open(path + file_name, 'wb') as f:
            f.write(url_open(i))


if __name__ == "__main__":
    url = 'http://nvshen2.92demo.com/'
    get_img(url_open(url).decode('utf-8'))
