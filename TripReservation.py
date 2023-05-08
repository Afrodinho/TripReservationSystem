from flask import Flask, redirect, render_template, request

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/login')
def login():
    return render_template('login.html')

@app.route('/reserve')
def reserve():
    return render_template('reserve.html')

@app.route('/', methods=['POST'])
def submit_form():
    option = request.form['option']
    if option == 'login':
        return redirect('/login')
    elif option == 'reserve':
      return redirect('/reserve')

'''
Function to generate cost matrix for flights
Input: none
Output: Returns a 12 x 4 matrix of prices
'''
def get_cost_matrix():
    cost_matrix = [[100, 75, 50, 100] for row in range(12)]
    return cost_matrix

app.run()