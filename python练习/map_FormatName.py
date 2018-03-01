#!/usr/bin/env python3
#_*_ encoding:utf-8 _*_
#将名字规范化，首字母大写，其他小写
#方法：利用map，需要写一个规范函数规范每一个名字，先写一个大写转化为小写函数，规范函数中首先保存首字母大写与变量中，然后利用map吧其他其母转化为小写，在依次加到首字母后
def b2s(s):
    return s.lower()
def normalize(name):
    f = name[0].upper()
    tem = list(map(b2s,name[1:len(name)]))
    for n in range(1,len(name)-1):
        f  = f + tem[n]
    return f
l1 = ['adam','BOB','dsaT']
l2 = list(map(normalize,l1))
print(l2)
