from flask import Flask, redirect, render_template, request
import os

app = Flask(__name__)

def occupiedSeats():
    reservedSeats = ""
    count = 0
    with open('final_project_files/reservations.txt', 'r') as file:
        for line in file.readlines():            
            entries = line.split(',')
            reservedSeats += f'{entries[1].strip()} {entries[2].strip()},'
            count += 1
    return [reservedSeats, count]

#Home Page
@app.route('/')
def home():
    return render_template('index.html')

@app.route('/', methods=['POST'])
def submit_form():
    option = request.form['option']
    if option == 'login':
        return redirect('/login')
    elif option == 'reserve':
      return redirect('/reserve')

#Log in Page
@app.route('/login')
def login():
   return render_template('login.html')

@app.route('/loginAuth', methods=['POST'])
def loginAuth():
    username = request.form['Username']
    password = request.form['password']
    
    with open('final_project_files/passcodes.txt','r') as file:
        for line in file:
            line = line.strip()  # remove leading/trailing whitespace
            user, pw = line.split(",")  # split line into username and password
            if username == user and password == pw:
                print("Sending you to the Admin page!")
                return redirect('/admin')
    
    print("Invalid username or password!")
    return redirect('/login')

@app.route('/admin')
def admin():
    return 'Welcome to the admin page!'



#Reserve Page
@app.route('/reserve')
def reserve():
    reservedSeats = occupiedSeats()[0]
    count = occupiedSeats()[1]
    return render_template('reserve.html', reservedSeats = reservedSeats, count = count)



'''
Function to generate cost matrix for flights
Input: none
Output: Returns a 12 x 4 matrix of prices
'''
# def get_cost_matrix():
#     cost_matrix = [[100, 75, 50, 100] for row in range(12)]
#     return cost_matrix


@app.route('/storeData', methods=['POST'])
def Reservation_Data():
    data = request.data.decode('utf-8')
    with open('final_project_files/reservations.txt', 'a') as f:
        f.write(data + '\n')
    return 'Data stored successfully'




app.run()
