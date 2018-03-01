#########################################################################
	#File Name: smtp.py
	#Author: Breeze
	#mail: isduanhc@163.com
	#github: https://github.com/breezeDHC
	#csdn: https://blog.csdn.net/RBreeze
	#Created Time: 2018年02月06日 星期二 09时49分15秒
#########################################################################
           
#!/usr/bin/env python3
#_*_ encoding:utf-8 _*_

from email import encoders
from email.header import Header
from email.utils import parseaddr, formataddr
import smtplib
from email.mime.text import MIMEText

def _format_addr(s):
    name, addr = parseaddr(s) #用来解析字符串中的email地址
    return formataddr((Header(name, 'utf-8').encode(), addr))

from_addr = 'isduanhc@163.com' 
password = 'dddhhhccc123'
to_addr = '852334606@qq.com'
smtp_server = 'smtp.163.com'

#msg = MIMEText('hello, send by python...', 'plain', 'utf-8')
msg = MIMEText('<html><body><h1>Hello</h1>' + '<p>send by <a href="http://www.python.org">Python</a>...</p>' + '</body></html>', 'html', 'utf-8') #html邮件，将正文换成html代码，将第二个参数设置为html
msg['From'] = _format_addr('Python爱好者<%s>' % from_addr)
msg['To'] = _format_addr('管理员<%s>' % to_addr)
msg['Subject'] = Header('来自smtp的问候','utf-8').encode()
server = smtplib.SMTP(smtp_server, 25) #smtp协议默认端口25
server.set_debuglevel(1)               #打印出和smtp交互信息
server.login(from_addr, password)      #登陆服务器
server.sendmail(from_addr, [to_addr], msg.as_string()) #发送邮件，可以发给多人,邮件正文是个str，用as_string（）将MIMEText对象变成str
server.quit()
