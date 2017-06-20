import json
import random

import requests
from flask import Flask, jsonify
from flask import Response
from flask import request

from utils import json_abort, JSON_MIME

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
            'name': "LSTM (best results among available)",
            'url': '/api/models/lstm/text-sentiment'
        }
    ]
    return jsonify(result)


urls = {
    'brute': '',
    'brute-tuned': '',
    'lstm': 'https://lstm-model-service.herokuapp.com/api/sentiment?text={0}'
}


@app.route('/api/models/<string:model>/text-sentiment/', methods=['POST'], strict_slashes=False)
def get_model_analyzed_text_sentiment(model):
    data = request.get_json(force=True)
    if not data or not data.get('text'):
        return json_abort({
            'message': 'Must be JSON field text'
        }, 400)

    # now just mocking
    url = urls.get(model, '')
    if not url:
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
        result = json.dumps(result)
    else:
        response = requests.get(url.format(data['text']))
        result = '{}'
        if response.status_code == 200:
            result = response.json()
            result['sentiment'] -= 0.07
            for item in result['tokens']:
                item['sentiment'] -= 0.07
            result = json.dumps(result)
    return Response(result, mimetype=JSON_MIME)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
