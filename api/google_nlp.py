from google.cloud import language_v1
from google.cloud.language_v1 import enums 

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

    line_one = f"To {pronouns[0]}, {adjectives[0]} {nouns[0]}, {pronouns[1]} {adverbs[0]} can be {adjectives[1]},"
    line_two = f"For as {pronouns[2]} were when {adpositions[0]} {pronouns[3]} {nouns[1]} I {verbs[0]},"
    line_three = f"Such seems {pronouns[4]} {nouns[2]} still. {numbers[0]} {nouns[3]} {adjectives[2]},"
    line_four = f"Have from {determinatives[0]} {nouns[4]} {verbs[1]} {numbers[1]} {pronouns[5]} {nouns[5]},"
    line_five = f"{numbers[1]} {adjectives[3]} {nouns[6]} to {adjectives[4]} {nouns[7]} {verbs[2]},"
    line_six = f"In process of the {nouns[7]} have I {verbs[3]},"
    line_seven = f"{numbers[1]} {nouns[8]} {nouns[9]} in {numbers[1]} {adjectives[5]} {nouns[10]} {verbs[4]},"
    line_eight = f"Since {adverbs[1]} I saw you {adjectives[6]}, which yet are {adjectives[7]}."
    line_nine = f"! {adverbs[2]} {verbs[5]} {nouns[11]} like a {nouns[12]}"
    line_ten = f"{verbs[6]} from {pronouns[5]} {nouns[13]}, and no {nouns[14]} {verbs[7]};"
    line_eleven = f"So your {adjectives[8]} {nouns[15]}, which {verbs[8]} still {adverbs[3]} {verbs[9]},"
    line_twelve = f"{nouns[16]} {nouns[17]}, and {pronouns[6]} {nouns[18]} {verbs[10]} be {verbs[11]}:"
    line_thirteen = f"For {nouns[19]} of which, {verbs[12]} this {pronouns[7]} {nouns[20]} {verbs[13]}:"
    line_fourteen = f"{numbers[2]} you were {verbs[14]} was {nouns[21]} {nouns[22]} {nouns[23]}."

    sonnet = line_one, line_two, line_three, line_four, line_five, line_six, line_seven, line_eight, line_nine, line_ten, line_eleven, line_twelve, line_thirteen, line_fourteen
    # , line_five, line_six, line_seven, line_eight, line_nine, line_ten
    return sonnet
    # return verbs, nouns, adverbs, pronouns, adpositions, punctuation, determinatives, adjectives, numbers, conjunctions, prts

    # speech_parts.append({"Token text": text.content, "Part of speech": enums.PartOfSpeech.Tag(part_of_speech.tag).name})
    # this returns a list of lists with these parts of speech inside
