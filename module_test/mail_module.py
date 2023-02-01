from random import randint
from email.message import EmailMessage
import smtplib


def send_email_otp(to):
   try:
      otp=randint(1000,99999)
      body="OTP From AI_Car_OTP_Generator\nYour OTP is: "+str(otp)
      subject="Email Verification Code"
      msg = EmailMessage()
      msg.set_content(body)
      msg['subject']=subject
      msg['to'] = to

      user = "sarveshgandhere2002@gmail.com"
      msg['from']=user
      password = "kburswetbalyszew"

      server = smtplib.SMTP("smtp.gmail.com",587)
      server.starttls()
      server.login(user,password)
      server.send_message(msg)
      server.quit()
   except:
      return "False"
   else:
      return str(otp)

def send_password(to,password):
   body="Your password is: "+str(password)
   subject="Forgot password mail"
   msg = EmailMessage()
   msg.set_content(body)
   msg['subject']=subject
   msg['to'] = to

   user = "sarveshgandhere2002@gmail.com"
   msg['from']=user
   password = "kburswetbalyszew"

   server = smtplib.SMTP("smtp.gmail.com",587)
   server.starttls()
   server.login(user,password)
   server.send_message(msg)
   server.quit()
   

