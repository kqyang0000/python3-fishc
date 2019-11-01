from urllib import request

response = request.urlopen('http://placekitten.com/g/500/600')
pic = response.read()

with open('/Users/yangkaiqiang/Desktop/images/500_600_cat.jpg', 'wb') as f:
    f.write(pic)
