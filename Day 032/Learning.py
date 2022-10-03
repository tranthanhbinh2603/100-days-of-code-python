from smtplib import *
import datetime as dt
import calendar as cl
from random import *

#1 số cổng stmp:
# Gmail: smtp.gmail.com
# Hotmail: smtp.live.com
# Outlook: outlook.office365.com
# Yahoo: smtp.mail.yahoo.com

#smtplib.SMTP("smtp.gmail.com", port=587) - Chỉnh cổng
#https://accounts.google.com/b/0/DisplayUnlockCaptcha - Unlock captcha đăng nhập google

#Qua fix loi 2022:
#Step 1: https://myaccount.google.com/u/3/security - Turn on 2 step verify (Sử dụng số điên thoại)
#Step 2: https://myaccount.google.com/u/3/apppasswords - Tạo ứng dụng mới rồi nhận password


#Cách gửi mail:
# my_email = "macketoi0326@gmail.com"
# connection = SMTP("smtp.gmail.com", port=587)
# connection.starttls()
# connection.login(user=my_email, password='xxrvflmcftooryur')
# #connection.sendmail(from_addr=my_email, to_addrs='leha.tieuhocthanhson@gmail.com', msg="Hacker moi den day")
# connection.sendmail(from_addr=my_email,
#                     to_addrs='leha.tieuhocthanhson@gmail.com',
#                     msg="Subject:Hacker moi den day\n\nAAAAAAAA. Tao muon giet may")
# connection.close()

#Thư viện thời gian
#from datetime import *

# print(dt.datetime.now())
# print(dt.datetime.now().year)
# print(dt.datetime.now().day)
# print(dt.datetime.now().month)
# print(dt.datetime.now().hour)
# print(dt.datetime.now().minute)
# print(dt.datetime.now().second)
# print(dt.datetime.now().weekday())

# date_of_birth = dt.datetime(year=2006, month=3, day=26, hour=9, minute=15)
# print(date_of_birth)


#Thử thách: Random 1 chuỗi trong file quotes.txt và gửi tên thứ
#Bổ sung: Có thể check theo 1 ngày nào đó, nếu nó true thì mới gửi mail
# print(cl.day_name[dt.datetime.now().weekday()])
my_email = "macketoi0326@gmail.com"
connection = SMTP("smtp.gmail.com", port=587)
connection.starttls()
connection.login(user=my_email, password='xxrvflmcftooryur')
data = None
with open('quotes.txt', mode='r') as f:
    data = f.readlines()
message = f"Subject:Test quotes\n\n{choice(data)}\n{cl.day_name[dt.datetime.now().weekday()]}"
connection.sendmail(from_addr=my_email,
                    to_addrs='leha.tieuhocthanhson@gmail.com',
                    msg=message)
connection.close()
