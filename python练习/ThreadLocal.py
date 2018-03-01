#!/usr/bin/env python3
#_*_ encoding:utf-8 _*_
import threading

#创建全局的ThreadLocal对象
local_school = threading.local()

def process_student():
    #获取当前线程关联的student
    std = local_school.student
    print('Hello,%s (in %s)' % (std,threading.current_thread().name))

def process_thread(name):
    #绑定当前线程的student
    local_school.student = name
    process_student()

t1 = threading.Thread(target = process_thread, args=('bob',),name='Thread-A')
t2 = threading.Thread(target = process_thread, args=('Alice',),name='THread-B')
t1.start()
t2.start()
t1.join()
t2.join()

