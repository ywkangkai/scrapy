# -*- coding: utf-8 -*-
# @Time    : 2022/8/19 9:48 下午
# @Author  : 顾安
# @File    : 5. 循环接收并发送消息回执.py
# @Software: PyCharm


import socket


def main():
    udp_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    udp_socket.bind(('', 6789))
    # 循环接收
    while True:
        recv_data = udp_socket.recvfrom(1024)
        print(recv_data[0].decode())
        ip, port = recv_data[1]

        # 发送短信回执
        # print(ip, port)
        udp_socket.sendto(b'ok', (ip, port))
        if recv_data[0].decode() == 'exit':
            break
    udp_socket.close()


if __name__ == '__main__':
    main()
