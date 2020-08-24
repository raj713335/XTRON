from flask import Flask, render_template, request, redirect
from datetime import datetime


#print("HELLO WORLD")

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/form')
def form():
    return render_template('form.html')





if __name__ == "__main__":
    app.run(debug=True)