#!/usr/bin/env python3
#_*_ encoding:utf-8 _*_

#import time,threading
##新线程执行代码
#def loop():
#    print('thread %s is running...' % threading.current_thread().name)
#    n = 0
#    while n < 5:
#        n = n + 1
#        print('thread %s >>> %s' % (threading.current_thread().name,n))
#        time.sleep(1)
#    print('thread %s ended.' % threading.current_thread().name)
#print('thread %s is running...' % threading.current_thread().name)
#t = threading.Thread(target = loop,name='LoopThread')
#t.start()
#t.join()
#print('thread %s ended.' % threading.current_thread().name)


##多线程同时操作一个变量吧内容改错例子
#import time,threading
#
#balance = 0
##lock = threading.lock()
#def change_it(n):
#    global balance
#    balance = balance + n
#    balance = balance - n
#
#def run_thread(n):
#    for i in range(100000):
##        lock.acquire()   #上锁
##        try:
#            change_it(n)
##        finally:
##            lock.release()
#
#t1 = threading.Thread(target=run_thread,args(5,))
#t2 = threading.Thread(target=run_thread,args(8,))
#t1.start()
#t2.start()
#t1.join()
#t2.join()
#print(balance)

#启动cpu核心数量的死循环线程
import threading,multiprocessing

def loop():
    x = 0
    while True:
        x = x^1
for i in range(multiprocessing.cpu_count()):
    t = threading.Thread(target=loop)
    t.start()
