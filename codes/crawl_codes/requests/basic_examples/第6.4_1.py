import requests
url = 'http://cc.stream.qqmusic.qq.com/C100001Yyla31Dr60y.m4a?fromtag=52'
r = requests.get(url)
f = open('mymusic.m4a', 'wb')
# r.content获取响应内容（字节流）
f.write(r.content)
f.close()
