# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from socket import *
import sys
import os


def login(s, ADDR):
    while True:
        name = input('请输入用户名：')
        msg = "L " + name
        s.sendto(msg.encode(), ADDR)
        data, addr = s.recvfrom(1024)
        if data.decode() == 'OK':
            print("@进入聊天室@")
            return name
        else:
            print(data.decode())


def do_child(s, name, addr):
    # 发送消息
    while True:
        text = input('发言(quit退出)>>>：')
        # strip（）函数用于删除指定字符串头尾信息（默认为空格）
        if text.strip() == 'quit':
            msg = "Q " + name
            s.sendto(msg.encode(), addr)
            sys.exit('\n退出聊天室')
        msg = "C %s %s" % (name, text)
        s.sendto(msg.encode(), addr)


def do_parent(s):
    # 接收消息，分析请求，做出处理[退出/打印消息]
    while True:
        msg, addr = s.recvfrom(1024)
        if msg.decode() == 'EXIT':
            sys.exit(0)
        print(msg.decode() + '\n发言(quit退出)>>>>', end='')


def main():
    if len(sys.argv) < 3:
        print('argv is error')
        return
    HOST = sys.argv[1]
    PORT = int(sys.argv[2])
    ADDR = (HOST, PORT)

    s = socket(AF_INET, SOCK_DGRAM)

    name = login(s, ADDR)
    if name:
        pid = os.fork()
        if pid < 0:
            sys.exit('创建子进程失败')
        elif pid == 0:
            do_child(s, name, ADDR)
        else:
            do_parent(s)
    else:
        return

if __name__ == "__main__":
    main()
