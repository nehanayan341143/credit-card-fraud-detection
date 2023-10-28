# -*- coding: utf-8 -*-
"""
Created on Thu Nov 25 09:30:15 2021

@author: Neha
"""
import smtplib
from email.message import EmailMessage
mail_server = smtplib.SMTP_SSL('smtp.gmail.com')


try:
    mail_server.login("0126cs191064@oriental.ac.in", "abcd@123456")
except:
    print("Login failed")

message = EmailMessage()

message['To'] = "kneha4876@gmail.com"
#message['To'] = "tanushathakur4@gmail.com"
message['From'] = "0126cs191064@oriental.ac.in"
message['Subject'] = 'Alert!!!'
body="""Fraud Transaction detected 
         please contact your nearest bank
         
         
         Do not reply to this Email"""
message.set_content(body)

try:
    if input("Do you want to send this Email(Y/N): ").lower()=='y':
        mail_server.send_message(message)
        print("Email sent to '{}' sucessfully".format(message['To']))
    else:
        print("EMail not sent")
except:
        print("Exception occured! Email not sent")
finally:
    mail_server.quit()