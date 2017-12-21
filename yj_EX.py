from flask import Flask, jsonify, request

app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'Hello World!'


@app.route('/yj_index', methods=('GET', ))
def yj_ex():
    return jsonify({
        'code': 200,
        'msg': 'ok',
        'data': {
            'tbzhye': 81000,
            'mbzhye': 9000,
            'edzhye': 1000,
            'xjzhye': 2000,
            'cardNum': 3,
            'mbAdd': 10000,
            'mbTime': '08-10 22:00',
            'spAdd': 2000,
            'spTime': '08-11 10:00',
            'xjAdd': 30000,
            'xjTime': '08-12 12:00'
        }
    })


if __name__ == '__main__':
    app.run()
