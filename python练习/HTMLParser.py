#!/usr/bin/env python3 
#_*_ encoding:utf-8 _*_

from urllib import request
from html.parser import HTMLParser
from html.entities import name2codepoint

class MyHTMLParser(HTMLParser):

    def handler_starttag(self, tag, attrs):
        print('<%s>' % tag)

    def handler_endtag(self, tag):
        print('</%s>' % tag)

    def handler_startendtag(self, tag, attrs):
        print('<%s/>' % tag)
    
    def handle_data(self, data):
        print(data)
    
    def handler_comment(self, data):
        print('<!--', data, '-->')

    def handle_entityref(self, name):
        print('&%s;' % name)

    def handler_charref(self, name):
        print('&#%s;' % name)

parser = MyHTMLParser()
#parser.feed('''<html>
#<head></head>
#<body>
#<!-- test html parser -->
#    <p> Some <a href=\"#\">html</a>HTML&nbsp;tutorial...<br>END</p>
#</body></html>''')
data_html = request.urlopen('https://www.python.org/events/python-events/')
data = data_html.read().decode()
parser.feed(data)
