from bs4 import BeautifulSoup
import requests

response = requests.get("https://news.ycombinator.com/")
webpage_text = response.text

soup = BeautifulSoup(webpage_text, "html.parser")
text = soup.findAll(name="span", class_="titleline")

for single_text in text:
    print(single_text.select_one("a").string.strip())
