from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Flask Dockerized App1'

@app.route('/pilot')
def pilot():
    return 'pilot'

@app.route('/pilot/coisa')
def pilota():
    return 'pilot coisa'


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5002)