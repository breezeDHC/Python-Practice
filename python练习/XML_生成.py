#!/usr/bin/env python3 
#_*_ encoding:utf-8 _*_

#利用字符串的拼接

L = []
L.append(r'<?xml version="1.0"?>')
L.append(r'<root>')
L.append('some & data')
L.append(r'</root>')
xml = ''.join(L)
print(xml)
