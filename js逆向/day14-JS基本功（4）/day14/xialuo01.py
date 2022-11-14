
import requests

# 获取JS文件


# 1 执行访问
res  = requests.get('http://127.0.0.1:5001/')
print(res.text)

# 2 传参数
params = {
    'pwd':'123456'
}
res1  = requests.get('http://127.0.0.1:5001/api',params=params)
print(res1.text)




