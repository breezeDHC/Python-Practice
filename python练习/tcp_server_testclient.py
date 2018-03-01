#!/usr/bin/env python3
#_*_ encoding:utf-8 _*_

import socket

s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.connect(('127.0.0.1',9999))
print(s.recv(1024).decode('utf-8'))
for data in [b'Michael',b'Tracy',b'Sarac']:
    s.send(data)
    print(s.recv(1024).decode('utf-8'))
s.send(b'exit')
s.close()
