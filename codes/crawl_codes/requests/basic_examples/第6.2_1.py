import requests
# 第一种方式
r = requests.get('https://www.baidu.com/s?wd=python')
# 第二种方式
url = 'https://www.baidu.com/s'
params = {'wd': 'python'}
# 左边params是GET请求中表示设置参数
r = requests.get(url, params=params)
# 输出生成的URL
print(r.url)


