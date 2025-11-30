import requests
from bs4 import BeautifulSoup

URL = "https://link.me/k1ngkyrg1os"
page = requests.get(URL)

soup = BeautifulSoup(page.content, "html.parser")

profile = soup.find(id="profileContainer")

total_follower_count = profile.find("span", class_="font-semibold mr-1")

# print(total_follower_count)

# why does this work?
total_follower_count_clean = ""
for word in total_follower_count:
    total_follower_count_clean
    
