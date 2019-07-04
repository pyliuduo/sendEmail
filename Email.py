
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.application import MIMEApplication


#发送smtp邮件
def sendMail(file_new):
    sender = '13058197453@163.com' #发送人邮箱

    receiver = ['13058197453@163.com', ]  # 收件人邮箱，，可设置多个

    mailToCc = ['zhaohuabing@lewanhuyu.com','liuduo@lewanhuyu.com',]  # 抄送人
    subject = '跑胡子自动化测试报告'
    smtpserver = 'smtp.163.com'
    username = '13058197453@163.com'
    password = 'ld4637807'

    msg = MIMEMultipart()
    msg['Subject'] = subject
    msg['From'] = sender
    msg['To'] = ';'.join(mailToCc)

    puretext = MIMEText('自动化执行测试报告请见附件!')
    msg.attach(puretext)


    # 首先是html类型的附件
    htmlpart = MIMEApplication(open(file_new, 'rb').read())  #b 二进制字节
    htmlpart.add_header('Content-Disposition', 'attachment', filename='testReport.html')
    msg.attach(htmlpart)

    smtp = smtplib.SMTP()  # smtp服务器
    smtp.connect(smtpserver) #链接服务器
    smtp.login(username, password) #登录邮箱
    smtp.sendmail(sender, receiver + mailToCc, msg.as_string()) #发送邮箱数据
    smtp.quit() #关闭邮箱

if __name__ == '__main__':
    sendMail('./test.html')

