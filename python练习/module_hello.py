#!/usr/bin/env python3
#_*_ encoding:utf-8 _*_

'a test module'
 
__author__ = 'duanhongchuan'

import sys

def test():
    argv = sys.argv
    if len(argv)==1:
        print('hello , world')
    elif len(argv) == 2:
        print('hello %s' % argv[1])
    else:
        print('Too many arguments!')

if __name__ == '__main__':
    test()
