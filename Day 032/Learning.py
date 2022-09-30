from smtplib import *

#1 số cổng stmp:
# Gmail: smtp.gmail.com
#
# Hotmail: smtp.live.com
#
# Outlook: outlook.office365.com
#
# Yahoo: smtp.mail.yahoo.com

#smtplib.SMTP("smtp.gmail.com", port=587) - Chỉnh cổng

#https://accounts.google.com/b/0/DisplayUnlockCaptcha - Unlock captcha đăng nhập google

#Cách gửi mail:
my_email = "macketoi0326@gmail.com"
connection = SMTP("smtp.gmail.com", port=587)
connection.starttls()
connection.login(user=my_email, password='MacketoiGe1')
connection.sendmail(from_addr=my_email, to_addrs='leha.tieuhocthanhson@gmail.com')

