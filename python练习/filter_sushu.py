#!/usr/bin/env python3
#_*_ encoding:utf-8 _*_
#产生3开始的自然数序列生成器
def _odd_iter():
    n = 1
    while True:
        n = n + 2
        yield n
#筛选函数
def _not_divisible(n):
    return lambda x:x%n>0
def primes():
    yield 2
    #初始化序列
    it = _odd_iter()
    while True:
        n = next(it)
        yield n
        it = filter(_not_divisible(n),it)  #构造新序列,此处以序列第一个为n
#以it的每一个数为x，如果是第一个数的倍数，则返回0,则删除序列中的这个数
for n in primes():
    if n < 1000:
        print(n)
    else:
        break
