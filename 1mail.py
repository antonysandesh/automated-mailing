# -*- coding: utf-8 -*-
"""1mail.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/18x13DYlEHrMkbpKBecy4JNZg_TkRr941
"""

import smtplib 

s = smtplib.SMTP('smtp.gmail.com', 587) 
s.starttls() 
# Authentication 
s.login("sender_email_id", "sender_email_id_password") 
message = "Message_you_need_to_send"
s.sendmail("sender_email_id", "receiver_email_id", message) 
s.quit()