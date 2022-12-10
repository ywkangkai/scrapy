import requests

data = {"group": "rpc-xl",
        "action": "des",
        'e':'aSNUniTUWCUzE0xwU+qofkugs2duoilNq8+TJpNXv7Q=',
        't':'1670245087599'
        }

# 把这个值写活  就能获取不同的cookie值  __zp_sts__ == t    __zp_sseed__ == e

# 值再cookie的话  可能就是 set-cookie 头部返回的

sign = requests.get("http://127.0.0.1:5620/business-demo/invoke",params=data)
print(sign.json())


