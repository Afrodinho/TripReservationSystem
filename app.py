from flask import Flask, redirect, render_template, request

app = Flask(__name__)

@app.route('/', methods=["GET", "POST"])
def Form():
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

if __name__ == "__app__":
    app.run(host='0.0.0.0')
