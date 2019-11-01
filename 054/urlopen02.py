from urllib import request

req = request.Request('http://placekitten.com/g/300/300')
resp = request.urlopen(req)
pic = resp.read()

print(resp.geturl())
print(resp.getcode())
print(resp.info())
with open('/Users/yangkaiqiang/Desktop/images/300_300_cat.jpg', 'wb') as f:
    f.write(pic)
