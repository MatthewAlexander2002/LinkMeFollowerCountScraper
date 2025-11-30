import requests
from bs4 import BeautifulSoup

def get_total_follower_count():
    URL = "https://link.me/k1ngkyrg1os"
    page = requests.get(URL)

    soup = BeautifulSoup(page.content, "html.parser")

    profile = soup.find(id="profileContainer")
    total_follower_count = profile.find("span", class_="font-semibold mr-1")

    for word in total_follower_count:
        return word.strip()

if __name__ == "__main__":
    print(get_total_follower_count())
