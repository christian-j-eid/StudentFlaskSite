from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def home():
    return render_template('base.html')

@app.route('/click')
def click():
    return render_template('beauty.html')
