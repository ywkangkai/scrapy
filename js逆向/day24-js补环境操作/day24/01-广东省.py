import json
import hashlib

data =  '{"type":"trading-type","publishStartTime":"","publishEndTime":"","siteCode":"44","secondType":"A","projectType":"","thirdType":"","dateType":"","total":168235,"pageNo":2,"pageSize":10,"openConvert":true}'

#  dateType=&openConvert=true
'''
key=value & key=value 

aa=&bb=张三

a b c d e


'''
# for key in sorted(data.keys())
data_it = json.loads(data)
datas = '&'.join(['{}={}'.format(key,data_it[key]) for key in sorted(data_it.keys()) ])
xxx = datas.replace('True','true')
print(xxx)

n = 'zlW7eMsCbw4S9oeq'
o = 'k8tUyS$m'
import time
params = n+o+xxx + str(int(time.time())*1000)
sign = hashlib.sha256(params.encode()).hexdigest()
print(sign)




