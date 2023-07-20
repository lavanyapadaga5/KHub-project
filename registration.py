from flask import Flask, render_template, request, redirect, session
from datetime import datetime

app = Flask(_name_)
app.secret_key = 'your_secret_key'  # Set a secret key for session management


# Temporary data storage
doctors = {
    'doctor1': 'password1',
    'doctor2': 'password2',
    'doctor3': 'password3'
}

appointments = {}


@app.route('/')
def home():
    if 'username' in session:
        return redirect('/dashboard')
    return render_template('index.html')


@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        if username in doctors:
            return render_template('register.html', error='Username already exists')
        doctors[username] = password
        return redirect('/')
    return render_template('register.html')


@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        if username in doctors and doctors[username] == password:
            session['username'] = username
            return redirect('/dashboard')
        return render_template('login.html', error='Invalid username or password')
    return render_template('login.html')

