

# 执行JS文件
import execjs

with open('xialuo-03.js',encoding='utf-8') as f:
    js_coed = f.read()

# 编译JS文件
ctll = execjs.compile(js_coed)
# 执行JS 调方法
# res = ctll.call('xl')
# print(res)

res1 = ctll.call('xls','hello','world')
print(res1)

print(execjs.eval("Date.now()"))













