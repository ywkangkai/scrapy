# -*- coding: utf-8 -*-
# @Time    : 2022/7/1 下午8:23
# @Author  : 图灵学院: 顾安
# @File    : 01-tcp_客户端.py
# @Software: PyCharm


import socket


def main():
    # 1. 创建套接字 tcp
    # SOCK_STREAM: TCP协议
    tcp_client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # 2. 连接服务器
    server_ip = input('请输入你要连接的服务器ip: ')
    server_port = int(input('请输入你要连接的服务器端口: '))
    server_address = (server_ip, server_port)
    tcp_client_socket.connect(server_address)

    # 3. 发送数据/接收数据
    send_data = input('请输入你要发送的数据: ')
    # 发送数据和udp不一样 udp:sendto  tcp: send
    tcp_client_socket.send(send_data.encode('utf-8'))

    # 4. 关闭套接字
    tcp_client_socket.close()


if __name__ == '__main__':
    main()
