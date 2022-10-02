# -*- coding: utf-8 -*-
# @Time    : 2022/8/19 9:31 下午
# @Author  : 顾安
# @File    : 4. 使用udp完成数据接收.py
# @Software: PyCharm

"""
当前目标为数据的接收
    需要两个条件
        发送发必要要知道我们的ip和端口

        也就是说， 如果我们想要接收别人的数据
        那么就需要进行本地数据绑定
        本地数据: ip port
"""


import socket


def main():
    # 1. 创建套接字
    udp_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    # 2. 信息绑定
    '''
    端口号不是随便写的
    有一些端口号是无法使用
        443
        80
        22
        21
    '''
    udp_socket.bind(('', 6666))

    # 3. 数据接收
    # 1024代表一次性可以接收的最大字节数
    recv_data = udp_socket.recvfrom(1024)

    # 将数据打印到控制台上
    '''
    数据接收方法 recvfrom 会返回一个元组
    会有两个元素
        1. 当前发送方所发送的数据
        2. 发送方的ip地址和端口 是一个元组
    '''
    print(recv_data[0].decode())

    # 4. 关闭套接字
    udp_socket.close()


if __name__ == '__main__':
    main()
