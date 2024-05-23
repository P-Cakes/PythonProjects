import smtplib

import os
with open('password.txt', 'r') as f:
    for line in f:
        if line.strip():  # ignore empty lines
            key, value = line.strip().split('=', 1)
            os.environ[key] = value

my_gmail = os.getenv('my_gmail')
gmail_password = os.getenv('gmail_password')
my_yahoo = os.getenv('my_yahoo')

with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
    connection.starttls()
    connection.login(user=my_gmail, password=gmail_password)
    connection.sendmail(
        from_addr=my_gmail,
        to_addrs=my_yahoo,
        msg="Subject:Hello\n\nThis is the body of my email"
    )
#
import datetime as dt
now = dt.datetime.now()
day_of_week = now.weekday()

import random
if day_of_week == 2:
    with open("quotes.txt") as file:
        all_quotes = file.readlines()
        quote = random.choice(all_quotes)
        with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
            connection.starttls()
            connection.login(user=my_gmail, password=gmail_password)
            connection.sendmail(
                from_addr=my_gmail,
                to_addrs=my_gmail,
                msg=f"Subject:HelloTest\n\n{quote}"
            )