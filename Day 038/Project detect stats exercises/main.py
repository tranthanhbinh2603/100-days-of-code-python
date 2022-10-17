from requests import *
from datetime import *

APP_ID = 'b3cbfc39'
APP_KEY = '6ccc0e8c7b48e1789368f3e4c2aa89a4'

SHEETY_ENDPOINT = 'https://api.sheety.co/3bbc8e294f7b6a69e668615a446142c8/myWorkouts/workouts'

header = {
    'x-app-id': APP_ID,
    'x-app-key': APP_KEY,
    'Content-Type': 'application/json'
}

body = {
     "query":"Ran 2 miles and walked for 3Km.",
     "gender":"male",
     "weight_kg":68,
     "height_cm":172,
     "age":17
}



data = post('https://trackapi.nutritionix.com/v2/natural/exercise', headers=header, json=body).json()
#Sử dụng chữ in nhỏ đề điền data:
for exercises in data['exercises']:
    # Tới step 5 mới học cái này
    header = {
        'Authorization': 'Bearer 7PtX6pofETdZhfeSDWWqEEwJ4D8p2sRVahYGxmcQTEyaeTURum'
    }
    now = datetime.now()
    workouts = {
        "workout": {
            "date": now.strftime("%d/%m/%Y"),
            "time": now.strftime("%X"),
            "exercise": str(exercises['name']).title(),
            "duration": str(exercises['duration_min']).title(),
            "calories": str(exercises['nf_calories']).title()
        }
    }
    #print(body)
    #print(post(url=SHEETY_ENDPOINT, json=workouts).text)
    print(post(url=SHEETY_ENDPOINT, json=workouts, headers=header).text)
