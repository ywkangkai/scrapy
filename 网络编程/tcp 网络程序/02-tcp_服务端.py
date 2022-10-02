# -*- coding: utf-8 -*-
# @Time    : 2022/7/1 下午8:51
# @Author  : 图灵学院: 顾安
# @File    : 02-tcp_服务端.py
# @Software: PyCharm


import socket


def main():
    # 1. 创建tcp实例对象
    tcp_server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    # 2. 绑定端口
    tcp_server_socket.bind(('', 6789))
    # 3. 等待客户端进行连接
    tcp_server_socket.listen(128)
    # 4. 如果连接成功, 则生成一个新的套接字对象负责数据接收和数据发送
    new_socket, client_address = tcp_server_socket.accept()  # 堵塞
    # 5. 接收客户端发送过来的信息 堵塞
    recv_data = new_socket.recv(1024)
    print(recv_data.decode())
    # 6. 服务器能接收信息之外 也可以发送数据
    new_socket.send('ok'.encode('utf-8'))
    # 7. 关闭套接字
    new_socket.close()
    tcp_server_socket.close()


if __name__ == '__main__':
    main()
