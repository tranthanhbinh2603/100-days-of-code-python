# Step 1 - Setup API Credentials and Google Spreadsheet
# 1. Go to this link and create a copy of the My Workouts Spreadsheet. You may need to login/register.
# (Vào trang https://docs.google.com/spreadsheets/d/1DHL6Y8XAHSC_KhJsa9QMekwP8b4YheWZY_sxlH3i494/edit?usp=sharing, chọn Tệp -> Tạo bản sao)
# 2. Go to the Nutritionix API website and select "Get Your API Key" to sign up for a free account. Double check your spam folder (and/or your gmail "promotions" tab) for the Nutritionix verification email.
# (Vào https://www.nutritionix.com/business/api đăng kí tài khoản, nhanh hơn thì vào https://developer.nutritionix.com/signup)
# 3. Once logged in, you should be able to access your API key and App id:
# (Đăng nhập xong vào https://developer.nutritionix.com/admin/access_details để lấy 2 mã Application ID và Application Keys)
# 4. Create a new project in PyCharm and in the main.py create 2 constants to store the APP_ID and API_KEY that you got from Nutritionix.
# (Tạo 2 hằng số APP_ID and API_KEY trong file lập trình

#Step 2 - Get Exercise Stats with Natural Language Queries
# Solution: https://gist.github.com/angelabauer/dd71d7072626afd728e1730584c6e4b8
# 1. Using the Nutritionix "Natural Language for Exercise" API Documentation, figure out how to print the exercise stats for a plain text input.
# You can hard code the API key and the App Id for now. In step 6, we'll store the API key and app id as environment variables.
# HINT 1:  Use what you have learnt about Authentication headers and the relevant part of the Nutritionix Authentication Documentation to authenticate your request.
# HINT 2: Use what you have learnt about making POST requests and the relevant part of the Nutritionix Exercise Documentation to make your request with the required parameters.
#https://docs.google.com/document/d/1_q-K-ObMTZvO0qUEAxROrN3bwMujwAN25sLHwJzliK0/edit#, https://docs.google.com/document/d/1_q-K-ObMTZvO0qUEAxROrN3bwMujwAN25sLHwJzliK0/edit#heading=h.gz6pu9o7f9iz, https://docs.google.com/document/d/1_q-K-ObMTZvO0qUEAxROrN3bwMujwAN25sLHwJzliK0/edit#heading=h.zhjgcprrgvim

# Step 3 - Setup Your Google Sheet with Sheety
# 1. Log into Sheety with your Google Account (the same account that owns the Google Sheet you copied in step 1).
# Make sure the email matches between your Google Sheet and Sheety Account. e.g.
# 2. In your project page, click on "New Project" and create a new project in Sheety with the name "Workout Tracking" and paste in the URL of your own "My Workouts" Google Sheet.
# 3. Click on the workouts API endpoint and enable GET and POST.
#Tiếng việt
#Bước 1: Vào https://sheety.co/ rồi đăng nhập tài khoản đã tao sheet
#Bước 2: Đăng nhập xong vào https://dashboard.sheety.co/, sau do chon new project -> From google sheet, paste link chia sẻ google sheet ở trên. Làm theo hướng dẫn
#Bước 3: Tạo xong project bật hết tất cả các quyền lên

#Step 4: Saving Data into Google Sheets
#1.  Using the Sheety Documentation, write some code to use the Sheety API to generate a new row of data in your Google Sheet for each of the exercises that you get back from the Nutritionix API. The date and time columns should contain the current date and time from the Python datetime module.
#HINT 1: Parameters have to be lower case. Also, pay special attention to this part in the documentation: https://sheety.co/docs/requests#:~:text=Sheety%20expects%20your%20record%20to%20be%20nested%20in%20a%20singular%20root%20property%20named%20after%20your%20sheet.%20For%20example%20if%20your%20endpoint%20is%20named%20emails%2C%20nest%20your%20record%20in%20a%20property%20called%20email.
#HINT 2: Remember you can generate text in title case by using the Python .title() method.
# https://www.w3schools.com/python/ref_string_title.asp
# HINT 3: Remember you can format a datetime object using the .strftime() method.
# https://www.w3schools.com/python/python_datetime.asp
# Debugging 🐞 Tip: If you're having any issues, double-check that you are logged in to Sheety with the same Google account that owns the spreadsheet you're trying to modify.
# Solu: https://gist.github.com/angelabauer/164864b78175bb1ecd3d3fd7f4ee39b7

# Step 5 - Authenticate Your Sheety API
# At the moment there is no authentication that's required to access your Sheety endpoint. That means anyone could read and write to your "My Workout" Google Sheet.
#
# 1. Add either "Basic Authentication" or "Bearer Token" to your Sheety endpoint to secure it.  You can hardcode the token in your code for now while you test your code. Once you're sure it works, we can add it to the environment variables in the next step.
#
#
# What is Bearer authentication?
#
# Bearer authentication (also known as token authentication) is an HTTP authentication scheme that involves security tokens. The name “Bearer authentication” basically means “give access to the bearer of this token.” The security token or “bearer token” is just a cryptic string. An example of a bearer token would be a string that could look something like this:
#
# "AAAAAAAAAAAAAAAAAAAAAMLheAAAAAAA0%2BuSeid%2BULvsea4JtiGRiSDSJSI%3DEUifiRBkKG5E2XzMDjRfl76ZC9Ub0wnz4XsNiRVBChTYbJcE3F"
#
# The idea is that whoever has the secret token, has permission to interact with the spreadsheet. A client - like your browser or mobile app - would then send this security token in the Authorization header when making requests to Sheety's server.
#
#
#
# 2. Using the Sheety documentation on authentication to update your Python code to authenticate your request.
#
# HINT: You'll need to read the relevant section on the request module documentation to do this.
#
# Basic Authentication: https://requests.readthedocs.io/en/master/user/authentication/#basic-authentication
#
# Bearer Authentication: https://stackoverflow.com/questions/29931671/making-an-api-call-in-python-with-an-api-that-requires-a-bearer-token
#
#
#
# SOLUTION
#Link dùng cho step 5:
# https://sheety.co/docs/authentication.html
# https://stackoverflow.com/questions/29931671/making-an-api-call-in-python-with-an-api-that-requires-a-bearer-token
#https://requests.readthedocs.io/en/latest/user/authentication/#basic-authentication
#https://gist.github.com/TheMuellenator/974c39779ec516c4c60e918c001e48ba

# Step 6 - Environment Variables in Repl.it
# In order to be able to post our workout data while we're out and about, it would be easier if we can access the console and run the code in Repl.it
#
# However, because Repl.it is open source, we don't want other people to see our API keys and secrets.
#
# 1. Using what you know about Environment Variables (see Day 35), update your code to use environment variables for all sensitive data including:
#
# APP_ID
#
# API_KEY
#
# SHEET_ENDPOINT
#
# USERNAME
#
# PASSWORD
#
# TOKEN
#
#
#
# HINT 1: You'll need to import the os module.
#
# Here's how you would set environment variables
#
# APP_ID = os.environ["APP_ID"]
# API_KEY = os.environ["API_KEY"]
# and here is how you would get an environment variable
#
# APP_ID = os.environ.get("APP_ID")
# API_KEY = os.environ.get("API_KEY")
#
#
# 2. Use the Repl.it documentation to work out how to create a .env file in Repl.it and store your Environment Variables in there.
#
# https://docs.repl.it/repls/secret-keys#:~:text=env%20files%20are%20used%20for,see%20the%20contents%20of%20the%20.
#
#
#
# HINT 2: Environment variables are declared without spaces!
#
# HINT 3: https://stackoverflow.com/questions/4906977/how-to-access-environment-variable-values
#
# HINT 4: https://img-c.udemycdn.com/redactor/raw/2020-07-27_14-49-17-73eb2d5ac7a886b723619c856c429935.png
#
# SOLUTION: https://gist.github.com/angelabauer/2e147663f998bbcf7b403c6c83f56a14
#Bước 6 này đọc cho vui thôi.
