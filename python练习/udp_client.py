#########################################################################
	#File Name: udp_client.py
	#Author: Breeze
	#mail: isduanhc@163.com
	#github: https://github.com/breezeDHC
	#csdn: https://blog.csdn.net/RBreeze
	#Created Time: 2018年01月24日 星期三 18时02分09秒
#########################################################################
           
#!/usr/bin/env python3
#_*_ encoding:utf-8 _*_
        
import socket

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
for data in [b'sd',b'sdfs',b'qasd']:
    s.sendto(data,('127.0.0.1',9999))
    print(s.recv(1024).decode('utf-8'))
s.close()
