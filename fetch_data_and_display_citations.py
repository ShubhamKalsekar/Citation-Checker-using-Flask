
# import requests
# from flask import Flask, render_template
# import nltk
# from nltk.tokenize import word_tokenize
# from nltk.corpus import stopwords
# from nltk.tokenize import sent_tokenize

# # Download NLTK data files (if not already installed)
# nltk.download('punkt')
# nltk.download('stopwords')

# app = Flask(__name__)

# # Fetch data from API
# def fetch_data():
#     url = "https://devapi.beyondchats.com/api/get_message_with_sources"
#     response = requests.get(url)
#     data = response.json()
#     return data["data"]["data"]

# # Extract citations from data
# def extract_citations(data):
#     citations = []
#     stop_words = set(stopwords.words('english'))

#     for item in data:
#         response_text = item['response']
#         sources = item['source']

#         response_tokens = set(word_tokenize(response_text.lower())) - stop_words
#         matched_sources = []

#         for source in sources:
#             context_tokens = set(word_tokenize(source['context'].lower())) - stop_words
#             if response_tokens & context_tokens:
#                 matched_sources.append({
#                     "id": source['id'],
#                     "link": source.get('link', '')
#                 })

#         citations.append({
#             "response_id": item['id'],
#             "citations": matched_sources
#         })

#     return citations

# @app.route('/')
# def index():
#     data = fetch_data()
#     citations = extract_citations(data)
#     return render_template('index.html', citations=citations)

# if __name__ == '__main__':
#     app.run(debug=True)

""" Output: 
Citations
Response ID: 1
ID: 71
ID: 8 Link
ID: 159
ID: 157
ID: 73
ID: 57
ID: 11
ID: 75
ID: 2 Link
ID: 62
ID: 60
Response ID: 2
ID: 127 Link
ID: 7
ID: 126 Link
ID: 4
ID: 60
ID: 75
ID: 71
ID: 73
ID: 115 Link
...
Response ID: 10
ID: 9
ID: 4368
ID: 609
ID: 4353
ID: 2 Link
ID: 1984
ID: 4382
ID: 4365
ID: 834
ID: 3 Link
ID: 4359

""" 






import requests
from flask import Flask, render_template
import nltk
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords


nltk.download('punkt')
nltk.download('stopwords')

app = Flask(__name__)

def fetch_data():
    url = "https://devapi.beyondchats.com/api/get_message_with_sources"
    response = requests.get(url)
    data = response.json()
    return data["data"]["data"]


def extract_citations(data):
    citations = []
    stop_words = set(stopwords.words('english'))

    for item in data:
        response_text = item['response']
        sources = item['source']

        response_tokens = set(word_tokenize(response_text.lower())) - stop_words
        matched_sources = []

        for source in sources:
            context_tokens = set(word_tokenize(source['context'].lower())) - stop_words
            if response_tokens & context_tokens:
                matched_sources.append({
                    "id": source['id'],
                    "link": source.get('link', '')
                })

        for source in matched_sources:
            citations.append(source)

    return citations

@app.route('/')
def index():
    data = fetch_data()
    citations = extract_citations(data)
    return render_template('index.html', citations=citations)

if __name__ == '__main__':
    app.run(debug=True)
