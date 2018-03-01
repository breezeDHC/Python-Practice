#!/usr/bin/env python3
#_*_ encoding:utf-8 _*_
def is_palindrome(n):
    return str(n) == str(n)[::-1]
def gen():
    n = 1
    while True:
        yield n
        n = n + 1
def lsg():
    it = gen()
    it = filter(is_palindrome,it)
    while True:
        yield next(it)
for n in lsg():
    if n < 1000:
        print(n)
    else:
        break
#output = filter(is_palindrome,range(1,1000))
#print(list(output))
