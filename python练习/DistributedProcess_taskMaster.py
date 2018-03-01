#!/usr/bin/env python3
#_*_ encoding:utf-8 _*_

import random,time,queue
from multiprocessing.managers import BaseManager
#发送任务队列
task_queue = queue.Queue()
#接受结果队列
result_queue = queue.Queue()
#从BaseManager继承QueueManager
class QueueManager(BaseManager):
    pass
#吧两个Queue注册到网络上，callable参数关联了Queue对象
QueueManager.register('get_task_queue',callable=lambda:task_queue)
QueueManager.register('get_result_queue',callable=lambda:result_queue)

#绑定端口5000,设置验证码'abc'
manager = QueueManager(address=('',5000),authkey=b'abc')
#启动Queue
manager.start()
#获取通过网络访问的Queue对象
task = manager.get_task_queue()
result = manager.get_result_queue()

#放几个任务进去
for i in range(10):
    n = random.randint(0,10000)
    print('put task %d' % n)
    result = m.get_result_queue()
    task.put(n)
print('try get result')
#从result队列读取结果
for i in range(10):
    r = result.get(timeout=10)
    print('result:%s' % r)
#关闭
manager.shutdown()
print('master exit')
