
'''
python执行JavaScript报错
UnicodeDecodeError: 'gbk' codec can't decode byte 0x80 in position 116: illegal multibyte sequence
'''

#  第一种解决办法 改包 默认得编码
import subprocess
from functools import partial
subprocess.Popen = partial(subprocess.Popen, encoding="utf-8")

# 第二种 改源码
# 渠道 subprocess.py 文件 搜索encoding  改默认编码
