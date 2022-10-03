##################### Extra Hard Starting Project ######################

# 1. Update the birthdays.csv

# 2. Check if today matches a birthday in the birthdays.csv

# 3. If step 2 is true, pick a random letter from letter templates and replace the [NAME] with the person's actual name from birthdays.csv

# 4. Send the letter generated in step 3 to that person's email address.

from pandas import *
from datetime import *
from smtplib import *
from random import *

# {'name': 'Test', 'email': 'test@email.com', 'year': 1961, 'month': 12, 'day': 21}
# {'name': 'Hacker', 'email': 'bowluj@mail-xz.com', 'year': 2021, 'month': 10, 'day': 1}
# {'name': 'Test', 'email': 'sutbaj@mail-xz.com', 'year': 2021, 'month': 10, 'day': 2}
# {'name': 'Name', 'email': 'loefee@mail-xz.com', 'year': 2023, 'month': 20, 'day': 1}

data = read_csv(filepath_or_buffer='birthdays.csv').to_dict(orient='records')
for row in data:
    if datetime.now().day == int(row['day']) and datetime.now().month == int(row['month']):
        with open(file=f'letter_templates/letter_{randint(1,3)}.txt') as f:
            message = str(f.read()).replace('[NAME]', row['name'])
        my_email = "macketoi0326@gmail.com"
        connection = SMTP("smtp.gmail.com", port=587)
        connection.starttls()
        connection.login(user=my_email, password='xxrvflmcftooryur')
        connection.sendmail(from_addr=my_email,
                            to_addrs=row['email'],
                            msg=message)
        connection.close()

#Run code on: https://www.pythonanywhere.com/




