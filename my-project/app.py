from flask import *
import requests

app=Flask(__name__)

@app.route("/")
def index():
    url="https://newsapi.org/v2/top-headlines?country=us&apiKey=c28411824f284716a10636471f8e7dba"
    r=requests.get(url).json()

    cases={
        'articles' : r['articles']
    }
    return render_template("index.html",case=cases)
if __name__=="__main__":
    app.run(debug=True)

#https://newsapi.org/docs/endpoints/top-headlines
