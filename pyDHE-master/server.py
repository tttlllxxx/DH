# @Time    : 2022/6/4 16:09
# @Author  : tlx
# @File    : server.py
# @Software: PyCharm
"""服务器"""

import socket
import DiffieHellman


def server():
    sk = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sk.bind(('127.0.0.1', 9090))
    sk.listen(5)
    m = DiffieHellman.DiffieHellman()

    while 1:
        print("Waiting connection from client...")
        conn, addr = sk.accept()  # 等待连接 -- 阻塞
        print("Connected by {}".format(addr))
        while 1:
            msg_r = conn.recv(1024).decode('utf-8')  # 阻塞等待接收客户端发来的消息
            m.get_message(msg_r)
            print('接收到来自%s的一个消息:%s' % (addr, msg_r))
            if msg_r == 'q':
                break
            msg_s = input('>>>')
            conn.send(msg_s.encode('utf-8'))  # 发送给客户端消息
            if msg_s == 'q':
                break
        conn.close()  # 服务器和当前客户端断开连接,程序回到上一层死循环,重新等待客户端的连接
        print("是否重连：y/n")
        temp = input('>>>')
        if temp == "y":
            print("等待重连")
        else:
            break
    sk.close()


server()
