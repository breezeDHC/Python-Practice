#!/usr/bin/env python3
#_*_ encoding:utf-8 _*_
#此处对于整数的处理同str2int，对于小数部分可以先转化为int，在乘以10的负的位数次方
from functools import reduce
import math
def str2float(s):
    D={'1':1,'2':2,'3':3,'4':4,'5':5,'6':6,'7':7,'8':8,'9':9}
    def char2int(s):
        return D[s]
    def f(x,y):
        return x*10 + y
    numF = 0
    numL = s.split('.')
    for index,numS in enumerate(numL):
        if index == 0:
            numF = numF + reduce(f,map(char2int,numS))
        else:
            numF = numF + reduce(f,map(char2int,numS))*pow(10,0-len(numS))
    return numF
print(str2float('123.56'))

