#########################################################################
	#File Name: udp_sercer.py
	#Author: Breeze
	#mail: isduanhc@163.com
	#github: https://github.com/breezeDHC
	#csdn: https://blog.csdn.net/RBreeze
	#Created Time: 2018年01月24日 星期三 17时58分24秒
#########################################################################
           
#!/usr/bin/env python3
#_*_ encoding:utf-8 _*_

import socket
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.bind(('127.0.0.1',9999))
print('bind udp on 9999')
while True:
    data,addr = s.recvfrom(1024)
    print('reveived from %s:%s.' % addr)
    s.sendto(b'hello , %s!' % data,addr)
    
