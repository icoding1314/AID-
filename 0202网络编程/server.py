# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from socket import *
import os
import sys


def do_login(s, user, name, addr):
    if (name in user) or name == "管理员":
        s.sendto('该用户已经存在'.encode(), addr)
        return
    s.sendto(b'OK', addr)
    msg = '\n欢迎%s进入聊天室' % name
    for i in user:
        s.sendto(msg.encode(), user[i])
    user[name] = addr  # 将新近用户追加到字典中  user: {'hello': ('127.0.0.1', 36208)}


def do_chat(s, user, name, data):
    # 发送管理员消息
    msg = "\n{} 说： {}".format(name, data)
    for i in user:
        # 不能发送给自己，
        if i != name:
            s.sendto(msg.encode(), user[i])


def do_quit(s, user, name):
    msg = '\n%s 离开了聊天室' % name
    for i in user:
        if i == name:
            s.sendto(b'EXIT', user[i])
        else:
            s.sendto(msg.encode(), user[i])
    del user[name]  # 删除离开的用户


def do_child(s, addr):
    # 发送管理员信息
    while True:
        msg = input('管理员消息：')
        msg = 'C 管理员 ' + msg
        s.sendto(msg.encode(), addr)


def do_parent(s):
    # 接收客户端请求，并处理
    # 用于存储用户：{'Alex':('127.0.0.1', 8888)}
    # 使用可变类型，传参的时候，user会跟着改变
    user = {}
    while True:
        msg, addr = s.recvfrom(1024)
        # split() 用作分割字符串
        # strip（）函数用于删除指定字符串头尾信息（默认为空格）
        msgList = msg.decode().split(' ')    #msgList: <class 'list'>  
        if msgList[0] == 'L':
            do_login(s, user, msgList[1], addr)
        elif msgList[0] == 'C':
            data = ' '.join(msgList[2:])
            do_chat(s, user, msgList[1], data)
        elif msgList[0] == 'Q':
            do_quit(s, user, msgList[1])


def main():
    ADDR = ('0.0.0.0', 8888)
    s = socket(AF_INET, SOCK_DGRAM)
    s.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)
    s.bind(ADDR)

    pid = os.fork()
    if pid < 0:
        sys.exit('创建进程失败')
    elif pid == 0:
        # 此处为子进程，先退出成为僵尸，后于退出为孤儿，
        do_child(s, ADDR)  # 父子进程间通信
    else:
        do_parent(s)


if __name__ == "__main__":
    main()
