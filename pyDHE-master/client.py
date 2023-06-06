# @Time    : 2022/6/4 16:09
# @Author  : tlx
# @File    : client.py
# @Software: PyCharm

"""客户端"""

from socket import socket
import DiffieHellman


def client():
    sk = socket()
    sk.connect(('127.0.0.1', 9090))
    m = DiffieHellman.DiffieHellman()

    while 1:
        msg_s = m.input_message()
        sk.send(msg_s.encode('utf-8'))
        if msg_s == 'q':
            break
        msg_r = sk.recv(1024).decode('utf-8')
        print(msg_r)
        if msg_r == 'q':
            break

    sk.close()


client()
