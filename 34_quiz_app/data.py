import requests
import html

trivia_api_url = "https://opentdb.com/api.php?amount=10&category=18&type=boolean"
response = requests.get(trivia_api_url)
response.raise_for_status()
question_data = response.json()["results"]
# In order to format html escapes in the question data, we need to install the html library
for question in question_data:
    question["question"] = html.unescape(question["question"])
    question["correct_answer"] = html.unescape(question["correct_answer"])
