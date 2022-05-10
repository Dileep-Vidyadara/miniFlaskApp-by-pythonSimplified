from crypt import methods
import debian
from flask import Flask, flash, redirect, render_template, request, url_for

app = Flask(__name__)
app.secret_key = 'fnjfndsmfndsmfn'

@app.route('/')
@app.route('/home')
def home():
    flash('Hey! What should we call you?')
    return render_template('index.html')

@app.route('/greet', methods=['GET','POST'])
def greet():
    USERNAME = request.form['userName']
    flash(f'Hello! {USERNAME} Welcome to our website ')
    return render_template('index.html') 
    

if __name__ == '__main__':
    app.run(debug=True)