#########################################################################
	#File Name: smtp_attachment.py
	#Author: Breeze
	#mail: isduanhc@163.com
	#github: https://github.com/breezeDHC
	#csdn: https://blog.csdn.net/RBreeze
	#Created Time: 2018年02月06日 星期二 11时14分07秒
#########################################################################
           
#!/usr/bin/env python3
#_*_ encoding:utf-8 _*_

from email import encoders
from email.header import Header
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.utils import parseaddr, formataddr
from email.mime.base import MIMEBase
import smtplib

def _format_addr(s):
    name , addr = parseaddr(s)
    return formataddr((Header(name,'utf-8').encode(), addr))

from_addr = 'isduanhc@163.com'
password = 'dddhhhccc123'
to_addr = '852334606@qq.com'
smtp_server = 'smtp.163.com'

#邮件对象
msg = MIMEMultipart()
msg['From'] = _format_addr('python爱好者<%s>' % from_addr)
msg['To'] = _format_addr('管理员<%s>' % to_addr)
msg['Subject'] = Header('来自smtp的问候。。', 'utf-8').encode()

#邮件正文
#msg.attach(MIMEText('send with file...', 'plain', 'utf8'))
#如果对方无法查看html格式的邮件可以再添加一个纯文本，如果无法查看html邮件则自动查看出纯文本
msg.attach(MIMEText('<html><body><h1>Hello</h1>' + '<p><img src="cid:0"></p>' + '</body></html>', 'html', 'utf-8')) #将图片添加到正文，先按照添加附件的方式添加图片，然后用html的img标签，将src引用为'cid:0'如果有多张图片，则图片编号，引用不同的cid:x
#添加附件就是加上一个MIMEBase，从本地添加一个图
with open('1.png', 'rb') as f:
    #设置附件的MIME和文件名
    mime = MIMEBase('image', 'png', filename='1.png')
    #添加必要的头信息
    mime.add_header('Content-Disposition','attachment', filename='1.png')
    mime.add_header('Content-ID','<0>')
    mime.add_header('X-Attachment-Id', '0')
    #读取附件内容
    mime.set_payload(f.read())
    #Base64编码
    encoders.encode_base64(mime)
    #添加到MIMEMultiart中
    msg.attach(mime)
server = smtplib.SMTP(smtp_server, 25)
#25好端口使用明文传输，安全发送email需要加密SMTP会话
#server.starttls()  #创建安全连接
server.set_debuglevel(1)
server.login(from_addr, password)
server.sendmail(from_addr, [to_addr], msg.as_string())
server.quit()
