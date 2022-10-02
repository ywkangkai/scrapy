# -*- coding: utf-8 -*-
# @Time    : 2022/8/19 9:20 下午
# @Author  : 顾安
# @File    : 3. 利用udp进行数据的循环发送.py
# @Software: PyCharm


import socket

'''
第二个参数为协议类型
    本节课所使用的类型只有两种
        udp
        tcp
'''


def main():
    udp_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    # 循环发送数据
    while True:
        # 1. 获取数据
        send_data = input('请输入你要发送的数据: ')
        # 2. 获取用户输入的数据并发送
        udp_socket.sendto(send_data.encode(), ('127.0.0.1', 6789))
        # 3. 因为是死循环 那么如果想要退出循环怎么办？
        # 判断用户输入的字符是否为退出 如果是退出 break
        if send_data == '退出':
            break
    # 4. 关闭套接字
    udp_socket.close()


if __name__ == '__main__':
    main()

