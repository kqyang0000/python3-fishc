from urllib import request, parse
import json
import time

while True:
    content = input('请输入需要翻译的内容：')
    if content == 'q!':
        break

    url = 'http://fanyi.youdao.com/translate?smartresult=dict&smartresult=rule'
    data = {'i': content, 'from': 'AUTO', 'to': 'AUTO', 'smartresult': 'dict',
            'client': 'fanyideskweb', 'salt': '15726255399983', 'sign': '2064eac81234992d82ea5f6a5af7da5c',
            'ts': '1572625539998', 'bv': '23dfa7fc0b5cde4c9bc1e29178220090', 'doctype': 'json',
            'version': '2.1', 'keyfrom': 'fanyi.web', 'action': 'FY_BY_REALTlME'}
    header = {
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_4) AppleWebKit/605.1.15 (KHTML, like Gecko) '
                      'Version/12.1 Safari/605.1.15'}

    data = parse.urlencode(data).encode('utf-8')
    req = request.Request(url, data, header)
    resp = request.urlopen(req)

    html = resp.read().decode('utf-8')
    html = json.loads(html)
    word = html['translateResult'][0][0]['tgt']
    print('翻译结果：%s' % word)
    time.sleep(5)
