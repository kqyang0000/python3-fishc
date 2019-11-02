import urllib.request
import random

url = 'http://www.whatismyip.com.tw'
ip_list = ['183.154.50.46:9999', '183.146.157.12:9999', '59.57.149.185:9999']

proxy_handler = urllib.request.ProxyHandler({'http': '222.128.9.235:33428'})
opener = urllib.request.build_opener(proxy_handler)
opener.addheaders = [('User-Agent', 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_4) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/12.1 Safari/605.1.15')]
urllib.request.install_opener(opener)

response = urllib.request.urlopen(url)
html = response.read().decode('utf-8')
print(html)
