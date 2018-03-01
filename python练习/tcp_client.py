#!/usr/bin/env python3
#_*_ encoding:utf-8 _*_

import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(('www.baidu.com',80))
s.send(b'GET / HTTP/1.1\r\nHost:www.baidu.com\r\nConnection:close\r\n\r\n')
bu = []
while True:
    d = s.recv(1024)
    if d:
        bu.append(d)
    else:
        break
data = b''.join(bu)
header,html = data.split(b'\r\n\r\n',1)
print(header.decode('utf-8'))
with open('baidu.html','wb') as f:
    f.write(html)
s.close()

