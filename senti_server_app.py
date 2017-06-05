import random

from flask import Flask, jsonify
from flask import request

from utils import json_abort

app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'Hello from senti api server!'


@app.route('/api/models/', methods=['GET'])
def get_available_methods():
    result = [
        {
            'name': "Brute Neural",
            'url': '/api/models/brute/text-sentiment'
        },
        {
            'name': "Tuned Brute Neural",
            'url': '/api/models/brute-tuned/text-sentiment'
        },
        {
            'name': "SVM (Support Vector Machine)",
            'url': '/api/models/svm/text-sentiment'
        }
    ]
    return jsonify(result)


@app.route('/api/models/brute/text-sentiment/', methods=['POST'], strict_slashes=False)
def get_brute_model_analyzed_text_sentiment():
    data = request.get_json(force=True)
    if not data or not data.get('text'):
        return json_abort({
            'message': 'Must be JSON field text'
        }, 400)

    # now just mocking
    tokens = data['text'].split(' ')
    result = []
    for token in tokens:
        if not token.isalpha():
            continue
        item = {
            'token': token,
            'sentiment': random.random()
        }
        result.append(item)
    return jsonify(result)


@app.route('/api/models/brute-tuned/text-sentiment/', methods=['POST'], strict_slashes=False)
def get_tuned_brute_model_analyzed_text_sentiment():
    data = request.get_json(force=True)
    if not data or not data.get('text'):
        return json_abort({
            'message': 'Must be JSON field text'
        }, 400)

    # now just mocking
    tokens = data['text'].split(' ')
    result = []
    for token in tokens:
        if not token.isalpha():
            continue
        item = {
            'token': token,
            'sentiment': random.random()
        }
        result.append(item)
    return jsonify(result)


@app.route('/api/models/svm/text-sentiment/', methods=['POST'], strict_slashes=False)
def get_svm_model_analyzed_text_sentiment():
    data = request.get_json(force=True)
    if not data or not data.get('text'):
        return json_abort({
            'message': 'Must be JSON field text'
        }, 400)

    # now just mocking
    tokens = data['text'].split(' ')
    result = []
    for token in tokens:
        if not token.isalpha():
            continue
        item = {
            'token': token,
            'sentiment': random.random()
        }
        result.append(item)
    return jsonify(result)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
