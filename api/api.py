from flask import Flask, jsonify, make_response
from flask_cors import CORS
import requests
import random
from settings import API_KEY
import pprint
from google.cloud import language_v1
from google.cloud.language_v1 import enums 

app = Flask(__name__)
CORS(app)

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

    # make lists of different word types
    adverbs = []
    verbs = []
    pronouns = []
    nouns = []
    adpositions = []
    punctuation = []
    determinatives = []
    adjectives = []
    numbers = []
    conjunctions = []
    prts = []

    response = client.analyze_syntax(document, encoding_type=encoding_type)
    # Loop through tokens returned from the API
    for token in response.tokens:
        # Get the text content of this token. Usually a word or punctuation.
        text = token.text    
        # # Get the part of speech information for this token.
        part_of_speech = token.part_of_speech
    
        # this is where we start collecting different lists of words
        if enums.PartOfSpeech.Tag(part_of_speech.tag).name == "VERB":
            verbs.append(text.content)
        elif enums.PartOfSpeech.Tag(part_of_speech.tag).name == "NOUN":
            nouns.append(text.content)
        elif enums.PartOfSpeech.Tag(part_of_speech.tag).name == "ADV":
            adverbs.append(text.content)
        elif enums.PartOfSpeech.Tag(part_of_speech.tag).name == "PRON":
            pronouns.append(text.content)
        elif enums.PartOfSpeech.Tag(part_of_speech.tag).name == "ADP":
            adpositions.append(text.content)
        elif enums.PartOfSpeech.Tag(part_of_speech.tag).name == "PUNCT":
            punctuation.append(text.content)
        elif enums.PartOfSpeech.Tag(part_of_speech.tag).name == "DET":
            determinatives.append(text.content)
        elif enums.PartOfSpeech.Tag(part_of_speech.tag).name == "ADJ":
            adjectives.append(text.content)
        elif enums.PartOfSpeech.Tag(part_of_speech.tag).name == "NUM":
            numbers.append(text.content)
        elif enums.PartOfSpeech.Tag(part_of_speech.tag).name == "CONJ":
            conjunctions.append(text.content)
        elif enums.PartOfSpeech.Tag(part_of_speech.tag).name == "PRT":
            prts.append(text.content)

    # parts = [verbs, nouns, adverbs, pronouns, adpositions, punctuation, determinatives, adjectives, numbers, conjunctions, prts]
    # print(f"Ⓜ️{parts[0][0]}")

    # not a randomized or organized poem yet
    # line_text = str(line)

    line_one = f"{nouns[0]} {verbs[0]} {adjectives[0]} {determinatives[3]}"
    line_two = f"{adjectives[1]} {nouns[18]}s {verbs[17]}"
    line_three = f"and {determinatives[2]} {nouns[2]} {adverbs[2]} {verbs[2]} {adjectives[2]} today."
    line_four = f"{pronouns[6]} {nouns[4]} {determinatives[4]} {adjectives[4]} {nouns[13]}"
    line_five = f"and {determinatives[5]} {nouns[5]} {adverbs[5]} {verbs[5]}s {nouns[19]} enough."
    line_six = f"{determinatives[6]} {adjectives[6]} {nouns[17]} {conjunctions[8]}"
    line_seven = f"{verbs[7]} {determinatives[7]} {adjectives[7]}, {verbs[8]}, {conjunctions[7]} {adverbs[11]}"
    line_eight = f"{numbers[3]} {adverbs[5]} {verbs[3]} {verbs[12]} my {nouns[16]}"
    line_nine = f"{nouns[2]} {adjectives[9]} {verbs[9]}"
    line_ten = f"{prts[10]} {adverbs[11]} {adjectives[10]} {verbs[11]}"

    return line_one, line_two, line_three, line_four, line_five, line_six, line_seven, line_eight, line_nine, line_ten
    # return verbs, nouns, adverbs, pronouns, adpositions, punctuation, determinatives, adjectives, numbers, conjunctions, prts

    # speech_parts.append({"Token text": text.content, "Part of speech": enums.PartOfSpeech.Tag(part_of_speech.tag).name})
    # this returns a list of lists with these parts of speech inside

# NYT API COMMENTS GET ROUTE
@app.route('/news')
def getNewsComments():
    article = f'https://www.nytimes.com/2020/08/12/arts/19th-amendment-black-womens-suffrage-photos.html'
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

@app.route('/topnews')
def getTopHeadlines():
    url = f'https://api.nytimes.com/svc/topstories/v2/home.json?api-key={API_KEY}'
    data = requests.get(url).json()
    urls = data['results']

    url_list = []
    index = 0
    while index < 10:
        url_list.append(urls[index]['url'])
        index += 1

    return jsonify(url_list)



