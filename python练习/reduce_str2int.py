#!/usr/bin/env python3
#_*_ coding:utf-8 _*_
#将一个字符串转化为整数
from functools import reduce
D = {'0':0,'1':1,'2':2,'3':3,'4':4,'5':5,'6':6,'7':7,'8':8,'9':9}
def str2int(s):
    def fn(x,y):
        return x*10 + y
    def char2num(s):
        return D[s]
    return reduce(fn,map(char2num,s))
s = str2int('123')
print(s)
