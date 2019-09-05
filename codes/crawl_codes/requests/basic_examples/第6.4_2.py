import requests
url = 'https://weibo.cn/mblog/sendmblog?rl=0&st=bd6702'
cookies = {'xxx': 'xxx'}
files = {'content': (None, 'Python爬虫'),
         'pic': ('pic', open('test.png', 'rb'), 'image/png'),
         'visible': (None, '0')}
r = requests.post(url, files=files, cookies=cookies)
print(r.status_code)

