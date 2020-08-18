from flask import Flask, jsonify, make_response
from flask_cors import CORS
import requests
import random
from settings import API_KEY
import pprint
from google_nlp import sample_analyze_syntax

app = Flask(__name__)
CORS(app)
 
# NYT API COMMENTS GET ROUTE
@app.route('/news')
def getNewsComments():
    top_url = f'https://api.nytimes.com/svc/topstories/v2/home.json?api-key={API_KEY}'
    data = requests.get(top_url).json()
    urls = data['results']

    url_list = []
    index = 0

    while index < len(urls):
        url_list.append(urls[index]['url'])
        index += 1
    
    # have to hard code the possible links because some links do not have enough comments to analyze 
    articles = ["https://www.nytimes.com/2020/08/17/us/politics/democrats-women-voters-anger.html", "https://www.nytimes.com/2020/08/17/us/politics/bernie-sanders-dnc.html",
                "https://www.nytimes.com/2020/08/17/world/coronavirus-covid.html",
                "https://www.nytimes.com/2020/08/17/us/k-12-schools-reopening.html",
                "https://www.nytimes.com/2020/08/17/upshot/pandemic-recession-cities-fiscal-shortfall.html",
                "https://www.nytimes.com/2020/08/16/style/does-rapid-covid-testing-work-weddings-parties.html",
                "https://www.nytimes.com/2020/08/17/opinion/coronavirus-hopsitals-visitors.html",
                "https://www.nytimes.com/2020/08/17/opinion/coronavirus-cities-suburbs.html",
                "https://www.nytimes.com/2020/08/15/opinion/joe-biden-2020-1988-what-it-takes.html",
                "https://www.nytimes.com/2020/08/17/opinion/coronavirus-schools-teachers.html",
                "https://www.nytimes.com/2020/08/17/opinion/tennessee-19th-amendment.html",
                "https://www.nytimes.com/2020/08/16/opinion/us-coronavirus-testing.html",
                "https://www.nytimes.com/2020/08/15/opinion/sunday/biden-harris.html",
                "https://www.nytimes.com/2020/08/17/business/giant-bikes-coronavirus-shortage.html",
                "https://www.nytimes.com/2020/08/17/us/supreme-court-college-free-speech.html",
                "https://www.nytimes.com/2020/08/12/well/growth-mindset-resilience.html",
                "https://www.nytimes.com/2020/08/13/science/animal-tears.html",
                "https://www.nytimes.com/2020/08/11/health/microaggression-medicine-doctors.html"]
    
    article = random.choice(articles)

    url = f'https://api.nytimes.com/svc/community/v3/user-content/url.json?api-key={API_KEY}&offset=0&url={article}'
    data = requests.get(url).json()
    comments = data['results']['comments']

    # iterate through the comments to just get the comment bodies
    global comments_list
    comments_list = []

    index = 0
    while index < len(comments):
    # for key in comments[index]:
        comments_list.append(comments[index]['commentBody'])
        index += 1
    
    # turn the list into a string with join magic
    separator = ','
    content = separator.join(comments_list)
    # this get
    return jsonify(sample_analyze_syntax(content))
    # return content

# use this route to find links with enough comments to generate poems
@app.route('/topnews')
def getTopNews():
    top_url = f'https://api.nytimes.com/svc/topstories/v2/home.json?api-key={API_KEY}'
    data = requests.get(top_url).json()
    urls = data['results']

    url_list = []
    index = 0

    while index < len(urls):
        url_list.append(urls[index]['url'])
        index += 1
    
    return jsonify(urls)



