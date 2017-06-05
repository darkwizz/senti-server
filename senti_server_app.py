from flask import Flask, jsonify

app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'Hello from senti api server!'


@app.route('/api/models/', methods=['GET'])
def get_available_methods():
    result = [
        {
            'name': "Brute",
            'url': '/api/models/brute/text-sentiment'
        }
    ]
    return jsonify(result)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
