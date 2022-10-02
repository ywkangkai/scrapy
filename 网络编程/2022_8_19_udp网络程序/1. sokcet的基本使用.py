# -*- coding: utf-8 -*-
# @Time    : 2022/8/19 8:46 下午
# @Author  : 顾安
# @File    : 1. sokcet的基本使用.py
# @Software: PyCharm


# 完成网络程序的创建

# 1. 需要导入网络开发包
import socket

# 2. 确定目标 完成在当前机器上发送一条数据出去


def main():
    # 2.1 创建一个套接字对象 -> 完成网络数据的发送 [当前所使用的网络协议类型为udp]
    """
        通过socket模块中的socket方法去创建一个套接字对象
        参数
            family -> 网络类型
                ipv4 --> pc
                ipv6 --> 移动端

            type -> 协议类型
                tcp
                udp
                ftp
                ssh
        """
    udp_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    # 3. 当创建完套接字对象之后 使用这个对象进行数据的发送
    """
    sendto作用: 发送数据
        需要两个参数
            1.你要发送的信息
            2.当前要把数据发送到哪里去(ip，port)
            
        因为现在我们还没有学到数据的接收
            所以我现在通过虚拟机中的软件进行演示
            
        在使用sendto的时候, 需要注意当前发送的地址为一个元组
            在元组中有两个元素，ip和port
            ip地址定义为字符串
            port定义为整型
    """
    udp_socket.sendto(b'abc', ('192.168.65.244', 8080))

    # 4. 网络程序需要占用系统资源(端口) 我们需要释放端口 释放系统资源
    udp_socket.close()


# 运行代码
if __name__ == '__main__':
    main()


'''
当前程序中并没有指定端口
    如果没有指定端口的情况下
    操作系统会自动分配一个端口进行数据的收发
'''

