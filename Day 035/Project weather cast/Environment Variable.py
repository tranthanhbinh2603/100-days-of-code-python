#Environment Variables
#Neu gõ env vào cmd (mac thôi, còn set trên windows), sẽ ra 1 đống biến số.

#2 mục đích: 1 là thuận tiện, 2 là để bảo mật

#Thêm 1 biến môi trường: export <tên biến>=<giá trị>; (Linux hoặc pythonanyware). Hệ điều hành khác tự mò

#Sử dụng biến môi trường:
from os import *
print(getenv('APPDATA'))
print(environ.get('APPDATA'))

#Trên pythonanyware, bạn có thể thêm export <tên biến>=<giá trị>; trước khi chạy câu lệnh chạy file.  (Từng cặp giá trị trước, 2 cặp nhập 2 cặp)

#trước khi gửi code lên git hay bất cứ chổ nào trên internet, luôn nho loại bỏ giá trị API ra