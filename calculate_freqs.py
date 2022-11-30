import json
from nltk import word_tokenize, download
from nltk.corpus import stopwords
import contractions
import os

download('punkt', quiet=True)
download('stopwords', quiet=True)

sw = set(stopwords.words('english'))

def sort_dict_by_values(d, reverse=False):
    return {key: val for key, val in sorted(d.items(), key = lambda ele: ele[1], reverse=not reverse)}

def tokenize_comment(c):
    c = repr(c).encode('utf-16', 'surrogatepass').decode('utf-16')
    c = contractions.fix(c)
    c = word_tokenize(c)
    c = [word.lower() for word in c if word.isalpha()]
    c = [word for word in c if word not in sw]
    return c

def tokenize_comments(comments):
    return [{'score': e['score'], 'tokenized': tokenize_comment(e['content'])} for e in comments]

def calculate_straight_freq(tokenized):
    concatenated = []
    for post in tokenized:
        for comment in post['comments']:
            concatenated += comment['tokenized']

    freq = {}
    for e in concatenated:
        if e in freq:
            freq[e] += 1
        else:
            freq[e] = 1

    return sort_dict_by_values(freq)

def calculate_weighted_freq(tokenized):
    concatenated = []
    for post in tokenized:
        concatenated += post['comments']

    freq = {}
    for c in concatenated:
        for e in c['tokenized']:
            if e in freq:
                freq[e] += c['score']
            else:
                freq[e] = c['score']

    return sort_dict_by_values(freq)
    

if __name__ == '__main__':
    files = os.listdir("comments")

    files = [f for f in files if f.endswith(".json")]

    if not "freqs" in os.listdir("."):
        os.mkdir("./freqs")

    for file in files:
        if not file[:-5] in os.listdir("./freqs"):
            os.mkdir(f"./freqs/{file[:-5]}")

        comments = {}
        with open(f'comments/{file}', 'r') as f:
            comments = json.loads(f.read())

        tokenized = [{'comments': tokenize_comments(e['comments'])} for e in comments]

        freq = calculate_straight_freq(tokenized)
        with open(f"./freqs/{file[:-5]}/straight_freq.json", 'wt') as f:
            f.write(json.dumps(freq, ensure_ascii=False))

        freq = calculate_weighted_freq(tokenized)
        with open(f"./freqs/{file[:-5]}/weighted_freq.json", 'wt') as f:
            f.write(json.dumps(freq, ensure_ascii=False))
