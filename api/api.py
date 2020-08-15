from flask import Flask, jsonify
import requests
from newsapi import NewsApiClient   
import pprint
import datetime as dt
from settings import API_KEY
from google.cloud import language_v1
from google.cloud.language_v1 import enums


app = Flask(__name__)

@app.route('/home')
def sayHello():
    return "hello! we are home! 🎟"

# NEWS API TEST ROUTE

@app.route('/news')
def getNews():
    newsapi = NewsApiClient(api_key=API_KEY)
    top_headlines = newsapi.get_top_headlines(
    q='covid',
    language='en')

    for article in top_headlines['articles']:
        print('Title : ',article['title'])
        print('Description : ',article['description'],'\n\n')

# SYNTAX ANALYSIS TEST ROUTE

    