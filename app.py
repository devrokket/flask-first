from flask import Flask
app = Flask(__name__)

@app.route('/')
def root():
    return 'Welcome'

@app.route('/shopping')
def shopping():
    return 'All of themselves.'

