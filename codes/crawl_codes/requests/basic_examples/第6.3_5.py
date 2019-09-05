import requests
url = 'https://movie.douban.com/'
r = requests.get(url)
# r.cookies是RequestsCookieJar对象
print(r.cookies)
mycookies = r.cookies

# RequestsCookieJar转换字典
cookies_dict = requests.utils.dict_from_cookiejar(mycookies)
print(cookies_dict)

# 字典转换RequestsCookieJar
cookies_jar = requests.utils.cookiejar_from_dict(cookies_dict, cookiejar=None, overwrite=True)
print(cookies_jar)

# 在RequestsCookieJar对象添加Cookies字典中
print(requests.utils.add_dict_to_cookiejar(mycookies, cookies_dict))
