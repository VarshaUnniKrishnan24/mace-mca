from flask import Flask, request, render_template, jsonify
from flask_cors import CORS
import numpy as np
import re
import nltk
from nltk.corpus import stopwords
from gensim.models import Word2Vec
from keras.layers import LSTM, Dense, Dropout
from keras.models import Sequential, load_model
from gensim.models.keyedvectors import KeyedVectors
from semantic_similarity import match_answer_with_key

np.seterr(divide="ignore", invalid="ignore")

def sent2word(x):
    stop_words = set(stopwords.words("english"))
    x = re.sub("[^A-Za-z]", " ", x)
    x.lower()
    filtered_sentence = []
    words = x.split()
    for w in words:
        if w not in stop_words:
            filtered_sentence.append(w)
    return filtered_sentence

def essay2word(essay):
    essay = essay.strip()
    tokenizer = nltk.data.load("tokenizers/punkt/english.pickle")
    raw = tokenizer.tokenize(essay)
    final_words = []
    for i in raw:
        if len(i) > 0:
            final_words.append(sent2word(i))
    return final_words

import re
import nltk
from language_tool_python import LanguageTool

class Node:
    def __init__(self, word):
        self.word = word
        self.deg = 0

def getWordCount(text):
    wordList = re.findall(r'\w+', text)
    return len(wordList)

def getSentenceCount(text):
    sentList = nltk.sent_tokenize(text)
    return len(sentList)

def getParaCount(text):
    paraList = text.splitlines()
    paraList[:] = [element for element in paraList if element != ""]
    return len(paraList)

def getAvgSentenceLength(text):
    sentList = nltk.sent_tokenize(text)
    sumSentLength = 0
    for sent in sentList:
        sumSentLength = sumSentLength + getWordCount(sent)
    return float(sumSentLength)/len(sentList)

def correct_grammar(text):
    tool = LanguageTool('en-US')
    matches = tool.check(text)

    found_mistakes = []
    for error in matches:
        # Get the offset of the error in the text
        error_offset = error.offset
        # Extract the word where the error occurs
        error_word = text[error_offset:error_offset + error.errorLength]
        # Add the word to the list of mistakes
        found_mistakes.append(error_word)

    found_mistakes_count = len(found_mistakes)
    
    return found_mistakes, found_mistakes_count


def makeVec(words, model, num_features):
    vec = np.zeros((num_features,), dtype="float32")
    noOfWords = 0.0
    index2word_set = set(model.index_to_key)
    for i in words:
        if i in index2word_set:
            noOfWords += 1
            vec = np.add(vec, model[i])
    vec = np.divide(vec, noOfWords)
    return vec

def getVecs(essays, model, num_features):
    c = 0
    essay_vecs = np.zeros((len(essays), num_features), dtype="float32")
    for i in essays:
        essay_vecs[c] = makeVec(i, model, num_features)
        c += 1
    return essay_vecs

def get_model():
    model = Sequential()
    model.add(
        LSTM(
            300,
            dropout=0.4,
            recurrent_dropout=0.4,
            input_shape=[1, 300],
            return_sequences=True,
        )
    )
    model.add(LSTM(64, recurrent_dropout=0.4))
    model.add(Dropout(0.5))
    model.add(Dense(1, activation="relu"))
    model.compile(loss="mean_squared_error", optimizer="rmsprop", metrics=["mae"])
    model.summary()
    return model

def convertToVec(text):
    content = text
    if len(content) > 20:
        num_features = 300
        model = KeyedVectors.load_word2vec_format("word2vecmodel.bin", binary=True)
        clean_test_essays = []
        clean_test_essays.append(sent2word(content))
        testDataVecs = getVecs(clean_test_essays, model, num_features)
        testDataVecs = np.array(testDataVecs)
        testDataVecs = np.reshape(
            testDataVecs, (testDataVecs.shape[0], 1, testDataVecs.shape[1])
        )

        lstm_model = load_model("final_lstm.h5")
        preds = lstm_model.predict(testDataVecs)
        return str(round(preds[0][0]))

app = Flask(__name__)
CORS(app)

@app.route("/", methods=["GET"])
def create_task():
    return render_template("index.html")

@app.route("/upload", methods=["GET"])
def go_to_upload_page():
    return render_template("mainpage.html")

@app.route("/grade", methods=["POST"])
def gradeAnswer():
    final_text = request.get_json("text")["text"]
    semantic_strictness = request.get_json("semantic_strictness")["semantic_strictness"]
    answer_key = request.get_json("answer_key")["answer_key"]
    score = convertToVec(final_text)
    semantic_score = 0
    if answer_key != "":
        semantic_score = match_answer_with_key(
            final_text, answer_key, float(semantic_strictness)
        )
    return jsonify({"score": score, "semantic_score": semantic_score}), 201

@app.route('/entity', methods=['POST'])
def entity():
    if request.method == 'POST':
        data = request.json
        essay_content = data.get('essayContent', '')

        # Calculate statistics
        word_count = getWordCount(essay_content)
        sentence_count = getSentenceCount(essay_content)
        paragraph_count = getParaCount(essay_content)
        avg_sentence_length = getAvgSentenceLength(essay_content)
        grammar_mistakes, num_grammar_mistakes = correct_grammar(essay_content)

        # Generate HTML report
        report_html = "<u><h4>Sentence Length Info:</h4></u>" \
                      f"<p>Word Count: {word_count}</p>" \
                      f"<p>Sentence Count: {sentence_count}</p>" \
                      f"<p>Paragraph Count: {paragraph_count}</p>" \
                      f"<p>Average Sentence Length: {avg_sentence_length}</p>"

        report_html += "<b><u><h4>Grammar And Spell Check:</h4></u></b>"
        if num_grammar_mistakes == 0:
            report_html += "<p>No grammar mistakes found.</p>"
        else:
            grammar_mistakes_str = ", ".join(grammar_mistakes)
            report_html += "<p>" + grammar_mistakes_str + "</p>"

        # Return the report HTML as JSON
        return jsonify({"html": report_html}), 200


if __name__ == "__main__":
    app.run(debug=True)
