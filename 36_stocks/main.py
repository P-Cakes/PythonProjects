from datetime import timedelta
from datetime import datetime

import requests
import os
with open('api_key.txt', 'r') as f:
    for line in f:
        if line.strip():  # ignore empty lines
            key, value = line.strip().split('=', 1)
            os.environ[key] = value
            # alpha_api
            # news_api

alpha_api = os.environ.get('alpha_api')
news_api = os.environ.get('news_api')

STOCK_NAME = "TSLA"
COMPANY_NAME = "Tesla Inc"

STOCK_ENDPOINT = "https://www.alphavantage.co/query"
NEWS_ENDPOINT = "https://newsapi.org/v2/everything"

url = f'https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&symbol={STOCK_NAME}&interval=5min&apikey={alpha_api}'
r = requests.get(url)
data = r.json()

# print(data)


    ## STEP 1: Use https://www.alphavantage.co/documentation/#daily
# When stock price increase/decreases by 5% between yesterday and the day before yesterday then print("Get News").

#TODO 1. - Get yesterday's closing stock price. Hint: You can perform list comprehensions on Python dictionaries. e.g. [new_value for (key, value) in dictionary.items()]
newest_date = data['Meta Data']['3. Last Refreshed']
# print(newest_date)
yesterday_day_close = data['Time Series (Daily)'][newest_date]['4. close']
# print(yesterday_day_close)
#TODO 2. - Get the day before yesterday's closing stock price
yesterday_date_date = datetime.strptime(newest_date,  "%Y-%m-%d") - timedelta(days=1)
yesterday_date = yesterday_date_date.strftime("%Y-%m-%d")
# print(yesterday_date)
previous_close = data['Time Series (Daily)'][yesterday_date]['4. close']
# print(previous_close)
#TODO 3. - Find the positive difference between 1 and 2. e.g. 40 - 20 = -20, but the positive difference is 20. Hint: https://www.w3schools.com/python/ref_func_abs.asp
close_difference = abs(float(yesterday_day_close) - float(previous_close))
#TODO 4. - Work out the percentage difference in price between closing price yesterday and closing price the day before yesterday.
close_difference_percentage = (close_difference / float(previous_close)) * 100
#TODO 5. - If TODO4 percentage is greater than 5 then print("Get News").
print(f"""Yesterday's closing price: {yesterday_day_close}
Day before yesterday's closing price: {previous_close}
Difference: {close_difference}
Percentage: {close_difference_percentage}
""")
if close_difference_percentage > 0:
    news_response = requests.get(NEWS_ENDPOINT, params=dict(q=COMPANY_NAME, apiKey=news_api))
    # print("Get News")
    three_articles = news_response.json()["articles"][:3]
    print(three_articles)
#TODO 6. - Instead of printing ("Get News"), use the News API to get articles related to the COMPANY_NAME.

#TODO 7. - Use Python slice operator to create a list that contains the first 3 articles. Hint: https://stackoverflow.com/questions/509211/understanding-slice-notation


    ## STEP 3: Use twilio.com/docs/sms/quickstart/python
    #to send a separate message with each article's title and description to your phone number. 

#TODO 8. - Create a new list of the first 3 article's headline and description using list comprehension.

#TODO 9. - Send each article as a separate message via Twilio. 



#Optional TODO: Format the message like this: 
"""
TSLA: 🔺2%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
or
"TSLA: 🔻5%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
"""

