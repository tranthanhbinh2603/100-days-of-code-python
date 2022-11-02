# Step 1 - Choose Your Path and Download the Starting Project
# Download the starting project
# Download the project by clicking on this link:
# Unzip the downloaded file and open the project in PyCharm.
# Take a look through the starting project to get a sense for the structure of the final program.
# You can choose to build the project entirely yourself or you can follow step-by-step challenges. If you feel you are an advanced programmer and you have learnt and understood all the concepts in the course so far (OOP, APIs, datetime, List and Dictionary Comprehensions) then stop here and try to create the project yourself using the APIs listed below. If you prefer smaller step-by-step challenges then continue to the next lesson.
# Make Your Own Copy of the Starting Google Sheet
# Make a copy of the Google sheet.

# APIs Required
# Google Sheet Data Management - https://sheety.co/
# Kiwi Partners Flight Search API (Free Signup, Requires Credit Card Details) - https://partners.kiwi.com/
# Tequila Flight Search API Documentation - https://tequila.kiwi.com/portal/docs/tequila_api
# Twilio SMS API - https://www.twilio.com/docs/sms

# Program Requirements
# Use the Flight Search and Sheety API to populate your own copy of the Google Sheet with International Air Transport Association (IATA) codes for each city. Most of the cities in the sheet include multiple airports, you want the city code (not the airport code see here).
# Use the Flight Search API to check for the cheapest flights from tomorrow to 6 months later for all the cities in the Google Sheet.
# If the price is lower than the lowest price listed in the Google Sheet then send an SMS to your own number with the Twilio API.
# The SMS should include the departure airport IATA code, destination airport IATA code, departure city, destination city, flight price and flight dates. e.g.

# Toggle these options when setting up with the API providers
# Sheety API
# Avoid making too many unnecessary requests with the Sheety API while testing your code. The free tier for the Sheety API only allows 200 requests per month.
# Also, enable the PUT option so that you can write to your Google sheet
# Register with the Kiwi Partners Flight Search API
# Your account name should be the same as what you used later in "First name" and "Last name".
# There is no need to provide a credit card or billing information (you can skip that section) when you create your "Solution" (previously called "Application").
# When registering for your API key choose Meta Search as your product type.
# Then choose One-Way and Return.
# In summary, your "solution" should look something like this:
# If the website prompts you for the type of partnership you can either choose "Book with Kiwi.com" or the affiliate program. Both should work for this project.
# B1.1: Tai ve giai nen
# B1.2: Tao ban sao tu https://docs.google.com/spreadsheets/d/1YMK-kYDYwuiGZoawQy7zyDjEIU9u8oggCV4H2M9j7os/edit, bật chế độ chỉnh sửa rồi copy link
# B1.3: Đảm bảo có các api sau đây:
# Quản lý dữ liệu trang tính của Google - https://sheety.co/
# API tìm kiếm chuyến bay của Kiwi Partners (Đăng ký miễn phí, Yêu cầu thẻ tín dụng) - https://partners.kiwi.com/
# Tài liệu về API tìm kiếm chuyến bay Tequila - https://tequila.kiwi.com/portal/docs/tequila_api
# API Twilio SMS - https://www.twilio.com/docs/sms
# Program Requirements: ở trên
# Một số lưu ý:
# - Bật lệnh put ở trong sheety

# Buoc 2: Get sheet bằng sheety, sau đó đưa tất cả dữ liệu về 1 list. Duyệt list đó thay ma iata la "Testing",
# cuoi cung put len sheety.

# Bước 3: Sử dụng api https://tequila.kiwi.com/portal/docs/tequila_api/locations_api#:~:text=GET-,/locations/query,-Search%20by%20query
# Để get mã iata. Chú ý term nhập thẳng tên thành phố vào luôn nha (đừng bị lừa thành mã iata, mệt lắm)

#Bước 4: Tìm giá nhỏ nhất dùng API (khó nha)

#Bước 5: Gửi tin nhắn

#Ngay 2:
#Buoc 6: Tạo 1 project repl, thêm trang "user" vào googlesheet cũ, trong đó chứa 3 côt "First Name", "Last Name", "Email"
# Chọn sync bên sheety, sau đó bật chế độ post cho trang tính mới.
# Cuối cùng viết code để post.
# Code cua minh: https://replit.com/@Tran-ThanhThanh/ImpressivePeriodicProprietarysoftware?v=1

#Buoc 7: Xu li ngoai le. Neu co ngoai le tra ra, ban catch no tra ve null.
# 1. Add Bali, DPS, 501 to the last row of the prices sheet in your copy of the Flight Deals Google Sheet:
# NOTE: Bali is not a city, but the city in Bali with the largest airport is not well known to most people (Denpasar). To find the historic low price, I used this website: https://www.faredetective.com/farehistory/
# 2. Run your program and it will crash, we've set the max_stopovers to 0 and there are no direct flights from London to Denpasar (Bali). Use exception handling to prevent this. You'll need to use try/except/else to catch the situations when the flight data is empty and let the code continue without crashing.
# HINT: if the flight data is empty, you'll return an empty flight object (None) to main.py you can use continue to let the for loop to continue to run when flight is None. https://www.w3schools.com/python/ref_keyword_continue.asp

# Buoc 8 - Destinations without Direct Flights
# There are a lot of popular destinations that our customers will want to go to that don't have direct flights. e.g. Bali
# 1. If a flight is not found, check to see if there are flights with 1 stop and pretty print the result with pprint().
# 2. Modify the FlightData class to add 2 optional init parameters with default values - stop_overs=0 and via_city="" . Instead of the printing the result from (1.) above, create a flight object with stop_overs set to 1 and via_city as the name of stopover city. Examine the data you printed in (1.) carefully to extract the information for origin_city, origin_airport, destination_city, destination_airport, out_date, and return_date .
# HINT: the "route" key value pair you get back from the API now contains a list with 4 items. [origin -> stop_over, stop_over -> destination, destination -> stop_over, stop_over -> origin].
# 3. Format the message to the NotificationManager in main.py to add the stop_over number and via_city, if a flight is found that requires a stopover.
# e.g. It should read:
# Low price alert! Only £498 to fly from London-LHR to Denpasar-DPS, from 2020-11-18 to 2020-12-01
# Flight has 1 stop over, via Ho Chi Minh City.

# Buoc 9: Gui mail
# Now that our program is working as expected, all that's left to do is to notify our customers when there is a good deal!
# 1. Create a method in the NotificationManager called send_emails() . Use what you have learnt about smtplib and sending emails to send all our customers in the users sheet from Google Sheets the message that contains the flight deal.
# NOTE: when sending emails, it won't like the "£" symbol, you might get an error like the one below: (lỗi dấu euro)
# You can solve this by encoding the message with UTF-8 e.g. https://stackoverflow.com/questions/9942594/unicodeencodeerror-ascii-codec-cant-encode-character-u-xa0-in-position-20#answer-9942885
# 2. You can generate a Google Flight link with all the information pre-populated so that users can book the flights by clicking on the link in the email.
# e.g. This is the Google flight link for a flight from STN to SXF from 2020-08-25 to 2020-09-08.
# https://www.google.co.uk/flights?hl=en#flt=STN.SXF.2020-08-25*SXF.STN.2020-09-08
# Figure out which part of the URL needs to be replaced and construct a URL when for any cheap flights. Send this URL along with the message when you email your customers.
# e.g. In file Mail Example.png



