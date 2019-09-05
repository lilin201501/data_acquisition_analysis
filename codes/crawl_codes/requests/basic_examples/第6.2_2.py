import requests
# 字典类型
data = {'key1': 'value1', 'key2': 'value2'}
# 元组或列表
(('key1', 'value1'), ('key1', 'value2'))
# Json
import json
data = {'key1': 'value1', 'key2': 'value2'}
# 将字典转换Json
data=json.dumps(data)
# 发送POST请求
r = requests.post("https://www.baidu.com/", data=data)
print(r.text)



