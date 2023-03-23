import smtplib
from email.message import EmailMessage
# smtp.mailtrap.io- Mailtrap offers a free plan which allows us to send 500 mails per month"
class Mail:
    msg = EmailMessage()
    def __init__(self,p_host:str,p_port:int,p_mail_from:str,p_mail_pwd:str,p_mail_to:str,p_subject:str,p_msg:str,p_filename:str):
        self.host           =p_host
        self.port           =p_port
        self.mail_pwd       =p_mail_pwd
        self.msg['From']    =p_mail_from
        self.msg['To']      =p_mail_to
        self.msg['Subject'] =p_subject
        self.msg.set_content(p_msg)
        self.file_name      =p_filename
        self.mth_attach_file()
        self.mth_sendmail()

    def mth_attach_file(self):
        with open(file=self.file_name,mode='rb') as fp:
            img_data =fp.read()
            self.msg.add_attachment(img_data,maintype='text',subtype='txt')
            #msg.add_attachment(message, maintype='text', subtype='txt')

    def mth_sendmail(self):
        with smtplib.SMTP(host=self.host,port=self.port) as connection:
            connection.starttls()       # Hacer la conexion segura con el servidor de correo
            connection.login(user=self.msg['From'], password=self.mail_pwd)
            connection.send_message(msg=self.msg)
            # connection.sendmail(from_addr   =self.msg['From']
            #                      ,to_addrs  =self.msg['To']
            #                      ,msg       =f"Subject:Crypto File\n\n"
            #                      )
            connection.quit()