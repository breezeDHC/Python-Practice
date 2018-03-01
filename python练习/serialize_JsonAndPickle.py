#!/usr/bin/env python3
#_*_ encoding:utf-8 _*_

#1.pickle模块的序列化,pickle序列化时是得到一个bytes
import pickle
d = dict(name='duan',age=45)
#利用pickle.dumps并写入文件
b = pickle.dumps(d)   #序列化为bytes
f = open('se.txt','wb')
f.write(b)
f.close()
#利用pickle.dump直接吸入一个file-like object
f = open('se.txt','wb')
pickel.dump(d,f)
f.close()

#反序列化，利用pickle.loads
f = open('se.txt','rb')
bs = f.read()
print(pickle.loads(bs))
f.close()
#反序列化，利用pickle.load直接反序列化一个file-like object
f = open('se.txt','rb')
print(pickle.load(f))
f.close()

#json序列化，json序列化为一个str
import json
d = dict(name='bob',age =23)
#利用json.dumps序列化并写入一个文件
f = open('json.txt','w')
jt = json.dumps(d)
f.write(jt)
f.close()
#利用json.dump直接序列化写入一个file-like object
f = open('json.txt','w')
json.dump(d,f)

#利用json.loads()反序列化得到一个dict
f = open('json.txt','r')
print(json.loads(f.read()))
f.close()
#利用json.load()直接反序列化一个file-like object
f = open('json.txt','r')
print(json.load(f))
f.close()

#实现class实例的序列化和反序列
import json
class Student(object):
    def __init(self,name,age):
        self.name = name
        self.age = age

#在实现序列化时我们需要定义一个转化函数，将class实例转化为dict在序列化
def student2dict(obj):
    return {
            'name':obj.name,
            'age':obj.age
            }
#在反序列化先反序列化为一个dict，同时我们也需要一个函数，将dict转化为class实例 
def dict2student(di):
    reutrn Student(di['name'],di['age'])
#序列化
s = Student('bob',23)
print(json.dumps(s,default=student2dict))
#对于序列化时的转化函数，由于class实例都有一个__dict__属性，记录实例变量故
print(json.dumps(s,defailt= lambda obj:obj.__dict__))
#反序列化
json_str='{"name":"bob","age":23}'
print(json.loads(json_str,object_hook=dict2student))
        
