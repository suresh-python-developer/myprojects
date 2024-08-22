from bs4 import BeautifulSoup
import requests

response = requests.get("https://www.empireonline.com/movies/features/best-movies-2/")
webpage_text = response.text
soup = BeautifulSoup(webpage_text,"html.parser")

all_text = soup.findAll("h3")
list = []
for text in all_text:
         list.append(text.string.strip())
list.reverse()

with open("data.txt","w") as file:
    for sinle_item in list:
        file.write(f"{sinle_item}\n")


