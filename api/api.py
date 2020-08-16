from flask import Flask, jsonify
import requests
import random
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

# # count syllables function
# def syllable_count(word):
#     word = word.lower()
#     count = 0
#     vowels = "aeiouy"
#     if word[0] in vowels:
#         count += 1
#     for index in range(1, len(word)):
#         if word[index] in vowels and word[index - 1] not in vowels:
#             count += 1
#     if word.endswith("e"):
#         count -= 1
#     if count == 0:
#         count += 1
#     return count

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

    random_noun = random.choice(nouns)
    random_verb = random.choice(verbs)
    random_adverb = random.choice(adverbs)
    random_pronoun = random.choice(pronouns)
    random_adposition = random.choice(adpositions)
    random_punctuation = random.choice(punctuation)
    random_determinative = random.choice(determinatives)
    random_adjective = random.choice(adjectives)
    random_number = random.choice(numbers)
    random_conjunction = random.choice(conjunctions)
    random_prt = random.choice(prts)

    random_parts = [random_noun, random_verb, random_adverb, random_pronoun, random_adposition, random_punctuation, random_determinative, random_adjective, random_number, random_conjunction, random_prt]
    random_word = random.choice(random_parts)

    line_one = random_word, random_word, random_word, random_word, random_word, random_word
    line_one_text = str(line_one)

    my_poem = {
        'line_one': line_one_text
        # 'line_two': [random_number, random_conjunction, random_verb, random_punctuation],
        # 'line_three': [random_adjective, random_prt, random_determinative, random_adverb, random_verb],
        # 'line_four': [random_noun, random_determinative, random_conjunction, random_verb],
        # 'line_five': [random_noun, random_adverb, random_verb, random_adposition],
        # 'line_six': [],
        # 'line_seven': [],
        # 'line_eight': [],
        # 'line_nine': [],
        # 'line_ten': [],
        # 'line_eleven': []
        # 'line_twelve': []
        # 'line_thirteen': [],
        # 'line_fourteen': []
    }

    # separator = ','
    # lines = separator.join(line)

    return my_poem
    # return verbs, nouns, adverbs, pronouns, adpositions, punctuation, determinatives, adjectives, numbers, conjunctions, prts

    # speech_parts.append({"Token text": text.content, "Part of speech": enums.PartOfSpeech.Tag(part_of_speech.tag).name})
    # this returns a list of lists with these parts of speech inside

   
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
    # this get
    return jsonify(sample_analyze_syntax(content))
    # return content



