import os
with open('password.txt', 'r') as f:
    for line in f:
        if line.strip():  # ignore empty lines
            key, value = line.strip().split('=', 1)
            os.environ[key] = value

my_gmail = os.getenv('my_gmail')
gmail_password = os.getenv('gmail_password')
my_yahoo = os.getenv('my_yahoo')


import datetime as dt
today = (dt.datetime.now().month, dt.datetime.now().day)
# print(today)

import pandas
import random
import smtplib

data = pandas.read_csv("birthdays.csv")
# print(data)

birthdays_dict = {(data_row.month, data_row.day): data_row for (index, data_row) in data.iterrows()}

for key in birthdays_dict:
    if today == key:
        birthday_person = birthdays_dict[key]
       # print(birthday_person)
        with open(f"letter_templates/letter_{random.randint(1,3)}.txt") as file:
            letter = file.read()
            letter = letter.replace("[NAME]", birthday_person["name"])

            with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
                connection.starttls()
                connection.login(user=my_gmail, password=gmail_password)
                connection.sendmail(
                    from_addr=my_gmail,
                    to_addrs=my_gmail,
                    msg=f"Subject:Happy Birthday!\n\n{letter}"
                )


