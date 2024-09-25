from flask import Flask, render_template, request, redirect, url_for
import random

app = Flask(__name__)

user_wins = 0
computer_wins = 0
options = ["rock", "paper", "scissors"]

@app.route('/')
def home():
    return render_template('index.html', user_wins=user_wins, computer_wins=computer_wins)

@app.route('/play', methods=['POST'])
def play():
    global user_wins, computer_wins
    user_input = request.form['user_input'].lower()

    if user_input not in options:
        return redirect(url_for('home'))

    random_number = random.randint(0, 2)
    computer_pick = options[random_number]

    if user_input == computer_pick:
        result = "It's a tie!"
    elif (user_input == "rock" and computer_pick == "scissors") or \
         (user_input == "paper" and computer_pick == "rock") or \
         (user_input == "scissors" and computer_pick == "paper"):
        result = "You won!"
        user_wins += 1
    else:
        result = "You lost!"
        computer_wins += 1

    return render_template('index.html', user_wins=user_wins, computer_wins=computer_wins, result=result)

if __name__ == '__main__':
    app.run(debug=True)
