
import smtplib 

li = ["xxxxx@gmail.com", "yyyyy@gmail.com"] 
  
for dest in li: 
    s = smtplib.SMTP('smtp.gmail.com', 587) 
    s.starttls() 
    s.login("antonysandesh2000@gmail.com", "******") 
    message = "Message_you_need_to_send"
    s.sendmail("sender_email_id", dest, message) 
    s.quit()
