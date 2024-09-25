from flask import Flask, render_template, request, redirect, url_for
import random

app = Flask(__name__)

random_number = None
guesses = 0

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/start', methods=['POST'])
def start():
    global random_number, guesses
    top_of_range = int(request.form['top_of_range'])
    random_number = random.randint(0, top_of_range)
    guesses = 0
    return redirect(url_for('guess'))

@app.route('/guess', methods=['GET', 'POST'])
def guess():
    global guesses, random_number
    if request.method == 'POST':
        user_guess = int(request.form['user_guess'])
        guesses += 1
        if user_guess == random_number:
            result = "You got it! You got it in {} guesses".format(guesses)
            return render_template('index.html', result=result)
        elif user_guess > random_number:
            result = "You were above the number!"
        else:
            result = "You were below the number!"
        return render_template('guess.html', result=result)
    return render_template('guess.html')

if __name__ == '__main__':
    app.run(debug=True)
