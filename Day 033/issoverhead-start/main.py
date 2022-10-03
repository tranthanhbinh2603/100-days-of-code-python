import requests
from datetime import datetime
from smtplib import *
from time import sleep

MY_LAT = 11.225380 # Your latitude
MY_LONG = 107.292160 # Your longitude

response = requests.get(url="http://api.open-notify.org/iss-now.json")
response.raise_for_status()
data = response.json()

iss_latitude = float(data["iss_position"]["latitude"])
iss_longitude = float(data["iss_position"]["longitude"])

#Your position is within +5 or -5 degrees of the ISS position.


parameters = {
    "lat": MY_LAT,
    "lng": MY_LONG,
    "formatted": 0,
}

response = requests.get("https://api.sunrise-sunset.org/json", params=parameters)
response.raise_for_status()
data = response.json()
sunrise = int(data["results"]["sunrise"].split("T")[1].split(":")[0])
sunset = int(data["results"]["sunset"].split("T")[1].split(":")[0])

time_now = datetime.now()

is_running = True

while is_running:
    if abs(iss_longitude - MY_LONG) < 5 and abs(iss_latitude - MY_LAT) < 5:
        print('IN THE HEAD')
        response = requests.get("https://api.sunrise-sunset.org/json", params=parameters) #Dùng cái này để ta check thời gian mặt trời mọc và lặn. Đêm tối nằm trong khoảng đó.
        response.raise_for_status()
        data = response.json()
        sunrise = int(data["results"]["sunrise"].split("T")[1].split(":")[0])
        sunset = int(data["results"]["sunset"].split("T")[1].split(":")[0])

        if sunrise >= datetime.now().hour or sunset <= datetime.now().hour:
            my_email = "macketoi0326@gmail.com"
            connection = SMTP("smtp.gmail.com", port=587)
            connection.starttls()
            connection.login(user=my_email, password='xxrvflmcftooryur')
            data = None
            message = f"HUMM, IIS IN THE HEAD"
            connection.sendmail(from_addr=my_email,
                                to_addrs='leha.tieuhocthanhson@gmail.com',
                                msg=message)
            connection.close()

    response = requests.get(url="http://api.open-notify.org/iss-now.json")
    response.raise_for_status()
    data = response.json()
    iss_latitude = float(data["iss_position"]["latitude"])
    iss_longitude = float(data["iss_position"]["longitude"])

    for secs in range(60, 0, -1):
        print('Time remaining:', secs)
        sleep(1)




#If the ISS is close to my current position
# and it is currently dark
# Then send me an email to tell me to look up.
# BONUS: run the code every 60 seconds.



