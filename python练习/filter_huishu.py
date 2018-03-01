#!/usr/bin/env python3
#_*_ encoding:utf-8 _*_
def is_palindrome(n):
    return str(n) == str(n)[::-1]
output = filter(is_palindrome,range(1,1000))
print(list(output))
