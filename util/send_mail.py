__author__ = "xiaoke"
import smtplib
from email.mime.text import MIMEText
from email.header import Header
from email.mime.multipart import MIMEMultipart
import os


class SendEmail:
    '''发送文本，带html和带附件三种形式邮件的类'''

    global from_user
    global email_host
    global password
    # email_host = "smtp.qq.com"
    # from_user = "976249817@qq.com"
    email_host = "smtp.163.com"
    from_user = "xiaoke201310@163.com"
    # 这个地方一定要用授权码，不能用密码
    password = "xiaoke521"

    # 以正文的方式发送邮件
    def send_email(self, to_user_list, sub, content):
        # 构造发邮件标题的发件人，收件人，邮件主题
        user = "xiaoke" + "<" + from_user + ">"
        message = MIMEText(content, "plain", 'utf-8')
        message['Subject'] = Header(sub, "utf-8")
        message['From'] = user
        message['To'] = ';'.join(to_user_list)

        # 构造smtp服务所需要的一些参数
        server = smtplib.SMTP()
        server.connect(email_host)
        # server.set_debuglevel(1)
        # server.starttls()
        server.login(from_user, password)
        # 注意这里的第三个参数一定要是字符串类型的，而且是创建出来的message，否则报554错误
        server.sendmail(user, to_user_list, str(message))
        server.quit()

    # 发送邮件的主入口
    def send_main(self, pass_list, fail_list):
        pass_num = float(len(pass_list))
        fail_num = float(len(fail_list))
        count_num = pass_num + fail_num

        pass_result = "%.2f%%" % (pass_num / count_num * 100)
        fail_result = "%.2f%%" % (fail_num / count_num * 100)

        to_user_list = ['976249817@qq.com']
        sub = "接口自动化测试报告"
        content = "此次一共运行接口个数为%s个，通过个数为%s个，失败个数为%s,通过率为%s,失败率为%s" % (
            count_num, pass_num, fail_num, pass_result, fail_result)

        self.send_email(to_user_list, sub, content)

    # 以html的方式发送邮件
    def send_mail_html(self):
        pass

    # 发送带附件的邮件，首先要创建MIMEMultipart()实例，
    # 然后构造附件，如果有多个附件，可依次构造，最后利用smtplib.smtp发送。
    def send_mail_fujian(self):
        sender = "xiaoke201310@163.com"
        receivers = ['976249817@qq.com']  # 接收邮件，可设置为你的QQ邮箱或者其他邮箱

        # 创建一个带附件的实例
        message = MIMEMultipart()
        message['From'] = Header(sender, 'utf-8')
        message['To'] = ';'.join(receivers)
        subject = '所有接口测试邮件结果'
        message['Subject'] = Header(subject, 'utf-8')

        # 邮件正文内容
        message.attach(MIMEText('这是所有接口测试的结果，请查收附件', 'plain', 'utf-8'))

        # 构造附件1，传送当前目录下的 test.txt 文件
        att1 = MIMEText(open(
            'E:\\pycharmProject\\interface\\interfaceMyProject\\reports\\interface\\Test_TestRun_2018-03-26_17-12-49.html',
            'rb').read(), 'base64', 'utf-8')
        att1["Content-Type"] = 'application/octet-stream'
        # 这里的filename可以任意写，写什么名字，邮件中显示什么名字
        att1["Content-Disposition"] = 'attachment; filename="email01.html"'
        message.attach(att1)

        # 构造附件2，传送当前目录下的 runoob.txt 文件
        att2 = MIMEText(open(
            'E:\\pycharmProject\\interface\\interfaceMyProject\\reports\\interface\\Test_TestRun_2018-03-26_17-11-05.html',
            'rb').read(), 'base64', 'utf-8')
        att2["Content-Type"] = 'application/octet-stream'
        att2["Content-Disposition"] = 'attachment; filename="email02.html"'
        message.attach(att2)

        try:
            smtpObj = smtplib.SMTP()
            smtpObj.connect(email_host)
            smtpObj.login(from_user, password)
            smtpObj.sendmail(sender, receivers, str(message))
            print("邮件发送成功")
        except smtplib.SMTPException as e:
            print(e)
            print("Error: 无法发送邮件")

    def new_report(self):
        file_path = "E:\\pycharmProject\\interface\\interfaceMyProject\\reports\\interface"
        lists = os.listdir(file_path)
        # 重新按时间对目录下的报告进行排序
        lists.sort(key=lambda fn: os.path.getmtime(file_path + "\\" + fn))
        # 最新的文件
        # print(lists[-1])
        new_file_name = os.path.join(file_path, lists[-1])
        return new_file_name

    def send_mail_fujian_new_report(self, new_file_name):
        sender = "xiaoke201310@163.com"
        receivers = ['976249817@qq.com']

        # 创建一个带附件的实例
        message = MIMEMultipart()
        message['From'] = Header(sender, 'utf-8')
        message['To'] = ';'.join(receivers)
        subject = '所有接口测试邮件结果'
        message['Subject'] = Header(subject, 'utf-8')

        # 邮件正文内容
        message.attach(MIMEText('这是所有接口测试的结果，请查收附件', 'plain', 'utf-8'))

        # 构造附件
        att = MIMEText(open(new_file_name, 'rb').read(), 'base64', 'utf-8')
        att["Content-Type"] = 'application/octet-stream'
        # 这里的filename可以任意写，写什么名字，邮件中显示什么名字
        att["Content-Disposition"] = 'attachment; filename="new_report.html"'
        message.attach(att)

        try:
            smtpObj = smtplib.SMTP()
            smtpObj.connect(email_host)
            smtpObj.login(from_user, password)
            smtpObj.sendmail(sender, receivers, str(message))
            print("邮件发送成功")
        except smtplib.SMTPException as e:
            print(e)
            print("无法发送邮件")


if __name__ == '__main__':
    send_mail = SendEmail()
    # send_mail.send_main([1, 2], [3, 4])
    # send_mail.send_mail_fujian()
    # send_mail.send_mail_fujian_new_report()
