#!/usr/bin/env python3
#_*_ encoding:utf-8 _*_
from xml.parsers.expat import ParserCreate
#XML解析SAX流模式，主要是定义自己的三个事件函数，start_element,char_data,end_element,然后定义一个parser对象将其三个事件函数与自定义的三个相关联，最后调用对象的Parse方法。
class DefaultSaxHandler(object):
    def start_element(self,name,attrs):
        print('sax:start_element:%s,attr:%s' %(name, str(attrs)))
    
    def end_element(self,name):
        print('sax:end_element:%s' % name)

    def char_data(self, text):
        print('sax:char_data:%s' % text)

xml = r'''<?xml version="1.0"?>
<ol>
    <li><a href="/python">Ptrhon</a></li>
    <li><a href="/ruby">Ruby</a></li>
</ol>
'''

handler = DefaultSaxHandler()
parser = ParserCreate()
parser.StartElementHandler = handler.start_element
parser.EndElementHandler = handler.end_element
parser.CharacterDataHandler = handler.char_data
parser.Parse(xml)
