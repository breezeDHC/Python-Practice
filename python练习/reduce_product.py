#!/usr/bin/env python3
#_*_ encoding:utf-8 _*_
from functools import reduce
def prod(l):
    def product(x,y):
        return x*y
    return reduce(product,l)
l = [3,5,7,9]
r = prod(l)
print(r)
