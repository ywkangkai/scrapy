# -*- coding: utf-8 -*-
# @Time    : 2022/7/1 下午9:17
# @Author  : 图灵学院: 顾安
# @File    : 03-循环为多个客户端进行服务.py
# @Software: PyCharm

import socket


def main():
    # 1. 创建套接字
    tcp_server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    # 2. 绑定信息
    tcp_server_socket.bind(('', 8888))
    # 3. 监听
    tcp_server_socket.listen(128)

    # 4. 循环为多个客户端进行服务
    while True:
        print('循环等待客户端的连接...')
        new_socket, client_address = tcp_server_socket.accept()
        print('当前客户端为: %s' % str(client_address))

        # 5. 数据接收
        recv_data = new_socket.recv(1024).decode('utf-8')
        print('当前客户端发送过来的数据为: ', recv_data)

        # 6. 成功接收信息之后发送信息回执
        new_socket.send(b'ok...')

        # 7. 判断当前消息如果为exit时则退出整个程序
        if recv_data == 'exit':
            new_socket.close()
            tcp_server_socket.close()
            break

        # 7. 关闭套接字
        new_socket.close()
        print('服务完毕...\n')


if __name__ == '__main__':
    main()
