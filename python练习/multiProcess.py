#!/usr/bin/env python3
#_*_ encoding:utf-8 _*_
import os
##fork()在linux和mac中的调用
#print('Process (%s) start...' %os.getpid())
#pid = os.fork()
#if pid == 0:
#    print('I am child process(%s) and my parent is %s.' %(os.getpid(),os.getppid()))
#else:
#    print('I(%s) just created a child process(%s).' %(os.getpid(),pid))
#multiprocessing模块提供Process类来表示一个进程，传入参数就可以创建一个进程

#from multiprocessing import Process
#import os
#def run_proc(name):
#    print('run child process %s(%s)...'%(name,os.getpid()))
#
#if __name__=='__main__':
#    print('parent process %s.'%os.getpid())
#    p = Process(target = run_proc,args=('test',))
#    print('child process will start.')
#    p.start()
#    p.join()
#    print('child process end.')

##Pool启动大量子进程
#from multiprocessing import Pool
#import os,time,random
#
#def long_time_task(name):
#    print('run task %s(%s)...'%(name,os.getpid()))
#    start = time.time()
#    time.sleep(random.random()*3)
#    end = time.time()
#    print('task %s runs %0.2f seconds.' %(name,(end-start)))
#
#if __name__ == '__main__':
#    print('parent process %s.'% os.getpid())
#    p = Pool(4)
#    for i in range(5):
#        p.apply_async(long_time_task,args=(i,))
#        print('waiting for all subprocesses done...')
#        p.close()
#        p.join()
#        print('all subprocess done')

##子进程subprocess模块可以让我们方便的启动一个进程便控制其输入和输出
#import subprocess
#print('$ nslookup www.python.org')
#r = subprocess.call(['nslookup','www.python.org'])
#print('Exit code:',r)

#进程间通信：multiprocessing提供了Queue，Pipes等方式来是是实现通信
from multiprocessing import Process,Queue
import time,os,random
def write(q):
    print("Process to write:%s" % os.getpid())
    for value in ['A','B','C']:
        print('put %s to queue...' % value)
        q.put(value)
        time.sleep(random.random())
def read(q):
    print('process to read:%s' % os.getpid())
    while True:
        value = q.get(True)
        print('get %s from queue.' % value)
if __name__ == '__main__':
    q = Queue()
    pw = Process(target = write, args=(q,))
    pr = Process(target = read, args=(q,))
    pw.start()
    pr.start()
    pw.join()
    pr.terminate()

