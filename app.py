from flask import Flask, render_template, request
import random

app = Flask(__name__)

choices = ['rock', 'paper', 'scissors']

@app.route('/', methods=['GET', 'POST'])
def index():
    result = ''
    player = ''
    computer = ''

    if request.method == 'POST':
        player = request.form['choice']
        computer = random.choice(choices)

        if player == computer:
            result = "It's a tie!"
        elif (player == 'rock' and computer == 'scissors') or \
             (player == 'scissors' and computer == 'paper') or \
             (player == 'paper' and computer == 'rock'):
            result = 'You win!'
        else:
            result = 'You lose!'

    return render_template('index.html', result=result, player=player, computer=computer)

if __name__ == '__main__':
    app.run(debug=True)

    
