from requests import *
from datetime import *
from twilio.rest import Client

STOCK = "TSLA"
COMPANY_NAME = "Tesla Inc"

API_KEY_STOCK = "0R2Z5IS0V7Z76QKQ"
API_KEY_NEWS = "7ac91ae7cb46414aae40091dfb6be039"

## STEP 1: Use https://www.alphavantage.co
# When STOCK price increase/decreases by 5% between yesterday and the day before yesterday then print("Get News").

#API: https://www.alphavantage.co/documentation/
#Using api: https://www.alphavantage.co/query?function=TIME_SERIES_INTRADAY&symbol=TSLA&interval=5min&apikey=0R2Z5IS0V7Z76QKQ
#Lấy key: https://www.alphavantage.co/support/#api-key

## STEP 2: Use https://newsapi.org
# Instead of printing ("Get News"), actually get the first 3 news pieces for the COMPANY_NAME.

## STEP 3: Use https://www.twilio.com
# Send a seperate message with the percentage change and each article's title and description to your phone number.


#Optional: Format the SMS message like this: 
"""
TSLA: 🔺2%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
or
"TSLA: 🔻5%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
"""
list_news = []
# https://newsapi.org/v2/everything?q=tesla&from=2022-09-09&sortBy=publishedAt&apiKey=7ac91ae7cb46414aae40091dfb6be039
def Get_News():
    parra1 = {
        'q': 'tesla',
        'sortBy': 'publishedAt',
        'apiKey': '7ac91ae7cb46414aae40091dfb6be039'
    }
    data = get('https://newsapi.org/v2/everything', params=parra1)
    data.raise_for_status()
    for i in range(0, 3):
        key = ("Title", "Description")
        dict_news = dict.fromkeys(key, data.json()["articles"][i]['title'])
        dict_news['Description'] = data.json()["articles"][i]['description']
        list_news.append(dict_news)
    #print(list_news)

parra = {
    'function': 'TIME_SERIES_DAILY',
    'symbol': 'TLSA', #Mã cố phiếu
    'interval': '60min',
    'apikey': API_KEY_STOCK
}

def Send_Message():
    account_sid = 'AC6039a7fe299031fb85f652d3a9b40515'
    auth_token = '6457d2bcc2977d22b00012b37ad110f5'
    client = Client(account_sid, auth_token)

    message = client.messages \
        .create(
        body= f"""{STOCK} {'🔺' if abs(100 - devient) > 0 else '🔻'} {round(abs(100 - devient))}%\n
Headline: {list_news[0]['Title']}. \n
Brief: {list_news[0]['Description']}.\n
Headline: {list_news[1]['Title']}. \n
Brief: {list_news[1]['Description']}.\n
Headline: {list_news[2]['Title']}. \n
Brief: {list_news[2]['Description']}.\n""",
        from_='+13857072715',
        to='+84352863102'
    )

    print(message.sid)

data = get('https://www.alphavantage.co/query', params=parra)
data.raise_for_status()
#print(data.json())
#Chọn giá close để đo giá.
#List compeson dùng trong tình huống này
#print(data.json()["Time Series (Daily)"].items()) #Chuyển thành dạng dict item
list_data = [value for (key, value) in data.json()["Time Series (Daily)"].items()]
devient = float(list_data[0]['4. close']) / float(list_data[1]['4. close']) * 100
print(abs(100 - devient))
if abs(100 - devient) > 5:
    Get_News()
    Send_Message()

Get_News()
Send_Message()
