from flask import Flask, jsonify
import requests
from newsapi import NewsApiClient
from settings import API_KEY
import pprint
import datetime as dt
from google.cloud import language_v1
from google.cloud.language_v1 import enums 

app = Flask(__name__)

@app.route('/home')
def sayHello():
    return "hello! we are home! 🎟"

# SYNTAX ANALYSIS TEST CALL
def sample_analyze_syntax(text_content):

    client = language_v1.LanguageServiceClient()

    # Available types: PLAIN_TEXT, HTML
    type_ = enums.Document.Type.PLAIN_TEXT

    # Optional. If not specified, the language is automatically detected.
    language = "en"
    document = {"content": text_content, "type": type_, "language": language}

    # Available values: NONE, UTF8, UTF16, UTF32
    encoding_type = enums.EncodingType.UTF8

    response = client.analyze_syntax(document, encoding_type=encoding_type)
    # Loop through tokens returned from the API
    for token in response.tokens:
        # Get the text content of this token. Usually a word or punctuation.
        text = token.text
        print(u"Token text: {}".format(text.content))
    
        # # Get the part of speech information for this token.
        part_of_speech = token.part_of_speech
        # Get the tag, e.g. NOUN, ADJ for Adjective, et al.
        print(
            u"Part of Speech tag: {}".format(
                enums.PartOfSpeech.Tag(part_of_speech.tag).name
            )
        )

        return enums.PartOfSpeech.Tag(part_of_speech.tag).name

    
# NYT API COMMENTS GET ROUTE
@app.route('/news')
def getNewsComments():
    url = f'https://api.nytimes.com/svc/community/v3/user-content/url.json?api-key={API_KEY}&offset=0&url=https%3A%2F%2Fwww.nytimes.com%2F2019%2F06%2F21%2Fscience%2Fgiant-squid-cephalopod-video.html'
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
    return jsonify(sample_analyze_syntax(content))
    # return content
