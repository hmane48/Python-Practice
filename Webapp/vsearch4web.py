from flask import Flask, render_template, request
from vsearch import search4vowels

app = Flask(__name__)

@app.route('/')
def hello() -> str:
    return 'Hello World from Flask!!'

@app.route('/search4', methods = ['POST'])
def do_search() -> 'html':
    phrase = request.form['phrase']
    letters = request.form['letters']
    results =  str(search4vowels(phrase,letters))
    return render_template('results.html',the_title='Here are your results:',
    the_phrase = phrase, the_letters = letters, the_results = results)

@app.route('/entry')
def entry_page() -> 'html':
    return render_template('entry.html',the_title='Welcome to Search4letters on the Web!')

if __name__ == '__main__':
    app.run(debug = True)
