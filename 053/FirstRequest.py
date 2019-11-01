from urllib import request

response = request.urlopen('https://www.taobao.com')
html = response.read()
html = html.decode('utf-8')
print(html)
