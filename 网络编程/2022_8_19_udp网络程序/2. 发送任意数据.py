# -*- coding: utf-8 -*-
# @Time    : 2022/8/19 9:10 下午
# @Author  : 顾安
# @File    : 2. 发送任意数据.py
# @Software: PyCharm


import socket


def main():
    # 1. 创建套接字
    udp_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    # 2. 发送任意数据
    send_data = input('请输入你要发送的数据: ')
    # 3. 获取用户数据的数据并发送
    """
    encode: 进行编码的一个方法
    可以手动指定一个编码集
    """
    udp_socket.sendto(send_data.encode('utf-8'), ('127.0.0.1', 6666))
    # 4. 关闭套接字释放资源
    udp_socket.close()


if __name__ == '__main__':
    main()
