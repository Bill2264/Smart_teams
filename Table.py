from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def index():
    render_template('index.html')

@app.route("/update")
def update():
    dynamic_data = get_dynamic_data()

    return dynamic_data