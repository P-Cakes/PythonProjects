import requests
from bs4 import BeautifulSoup

# news.ycombinator.com/news

response = requests.get("https://news.ycombinator.com/news")
yc_webpage = response.text

soup = BeautifulSoup(yc_webpage, "html.parser")


all_news = soup.find_all("span", {"class": "titleline"})
article_texts = [a.find('a').getText() for a in all_news]
article_links = [a.find('a').get("href") for a in all_news]
# Get all span tangs containing scores
spans_score = soup.find_all("span", {"class": "score"})

# Get all scores from spans containing scores
article_scores = [int(score.getText().split()[0]) for score in spans_score]

# Get index of highest score
index = article_scores.index(max(article_scores))

# Print story title, link and votes of story with highest votes.
print(
    f"Story with highest upvotes.\nTitle: {article_texts[index]}\nUrl: {article_links[index]}\nVotes: {article_scores[index]}")

