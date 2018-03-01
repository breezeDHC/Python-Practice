#!/usr/bin/env python3
# _*_ encoding:utf-8 _*_
def by_name(t):
    return t[1]
l=[('Bob',75),('Adam',92),('Bart',66),('Lisa',88)]
l1=sorted(l,key = by_name,reverse=True)
print(l1)
