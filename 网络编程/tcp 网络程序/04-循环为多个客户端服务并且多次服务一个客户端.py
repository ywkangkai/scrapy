# -*- coding: utf-8 -*-
# @Time    : 2022/7/1 下午9:40
# @Author  : 图灵学院: 顾安
# @File    : 04-循环为多个客户端服务并且多次服务一个客户端.py
# @Software: PyCharm


import socket


def main():
    tcp_server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    tcp_server_socket.bind(('', 1234))
    tcp_server_socket.listen(128)

    while True:
        print('循环等待客户端的连接...')
        new_socket, client_address = tcp_server_socket.accept()
        print('当前客户端为:', client_address)
        # print(new_socket)
        while True:
            # 信息接收
            recv_data = new_socket.recv(1024).decode('utf-8')
            # 当前客户端发送的信息不为空 则返回消息回执
            if recv_data:
                print('当前客户端发送过来的信息为: ', recv_data)
                new_socket.send(b'ok...')
            else:
                break

        new_socket.close()
        print('服务完毕...')
        break
    tcp_server_socket.close()


if __name__ == '__main__':
    main()
