import requests
from bs4 import BeautifulSoup
from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

@app.route('/')
def main_page():
    return get_total_follower_count()


def get_total_follower_count():
    URL = "https://link.me/k1ngkyrg1os"
    page = requests.get(URL)

    soup = BeautifulSoup(page.content, "html.parser")

    profile = soup.find(id="profileContainer")

    total_follower_count = profile.find("span", class_="font-semibold mr-1")

    # print(total_follower_count)

    # why does this work?
    # total_follower_count_clean = ""
    for word in total_follower_count:
        return word
    

if __name__ == '__main__':
    app.run()