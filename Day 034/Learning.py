# HTML Entities
# https://www.w3schools.com/html/html_entities.asp
# https://www.freeformatter.com/html-escape.html
# https://stackoverflow.com/questions/2087370/decode-html-entities-in-python-string

#Ép kiểu bắt buoc cho bien trong ham
# age: int

#Type hint, hint ->:
#Muc dích: Xác định đối so cho việc nhắc lệnh trong pycharm
def isDrive(age: int) -> bool:
    if age > 18:
        return True
    else:
        return False

print(isDrive(100))
