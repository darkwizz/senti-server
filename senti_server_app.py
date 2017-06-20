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
            'name': "LSTM",
            'url': '/api/models/lstm/text-sentiment'
        }
    ]
    return jsonify(result)


urls = {
    'brute': '',
    'brute-tuned': '',
    'lstm': ''
}


@app.route('/api/models/<string:model>/text-sentiment/', methods=['POST'], strict_slashes=False)
def get_model_analyzed_text_sentiment(model):
    data = request.get_json(force=True)
    if not data or not data.get('text'):
        return json_abort({
            'message': 'Must be JSON field text'
        }, 400)

    # now just mocking
    tokens = data['text'].split(' ')
    result = {
        'sentiment': 0.0,
        'tokens': []
    }
    for token in tokens:
        if not token.isalpha():
            continue
        result['tokens'].append({
            'token': token,
            'sentiment': random.random()
        })
        result['sentiment'] += result['tokens'][-1]['sentiment']
    result['sentiment'] /= len(result['tokens'])
    return jsonify(result)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
