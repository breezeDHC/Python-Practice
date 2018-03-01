#########################################################################
	#File Name: pop3_emailDowmload.py
	#Author: Breeze
	#mail: isduanhc@163.com
	#github: https://github.com/breezeDHC
	#csdn: https://blog.csdn.net/RBreeze
	#Created Time: 2018年02月06日 星期二 12时11分26秒
#########################################################################
           
#!/usr/bin/env python3
#_*_ encoding:utf-8 _*_

import poplib
from email.parser import Parser

#输入邮件地址，口令和pop3服务器地址
email = 'isduanhc@163.com'
password = 'dddhhhccc123'
pop3_server = 'pop.163.com'

#链接pop3服务器
server = poplib.POP3(pop3_server)
#打开或关闭调试信息
server.set_debuglevel(1)
#可选，打印pop3服务器的欢迎文字
print(server.getwelcome().decode('utf-8'))

#身份认证
server.user(email)
server.pass_(password)

#stat()返回邮件数量和占用空间
print('Message : %s , Size: %s' % server.stat())
#list()返回所有邮件编号
resp, mails, ocets = server.list()
print(mails)

#获取最新的一封email
index = len(mails)
#循环可获取所有的邮件
resp, lines, octets = server.retr(index)

#lines存储了邮件的原始文本的没一行
#可以获得整个邮件的原始文本
msg_content = b'\r\b'.join(lines).decode('utf-8')

msg = Parser().parsestr(msg_content)
#可以根据邮件索引号直接从服务器删除邮件
#server.dele(index)
#关闭链接
server.quit()
