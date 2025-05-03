from flask import Flask, render_template
import requests
from bs4 import BeautifulSoup

app = Flask(__name__)

def get_hacker_news():
    url = "https://news.ycombinator.com/"
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')

    headlines = []
    titles = soup.select(".titleline > a")
    for idx, item in enumerate(titles[:15], 1): 
        headlines.append({"rank": idx, "title": item.text, "link": item["href"]})
    
    return headlines

@app.route("/")
def index():
    headlines = get_hacker_news()
    return render_template("index.html", headlines=headlines)

if __name__ == "__main__":
    app.run(debug=True)

    