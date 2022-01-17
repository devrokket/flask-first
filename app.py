from infinite_note.infinite_note import output_question
from flask import Flask
app = Flask(__name__)


@app.route('/')
def root():
    return 'Welcome'


@app.route('/shopping')
def shopping():
    return 'All of themselves.'


@app.route('/answer')
def inf_note_answer():
    q = output_question()
    return q
