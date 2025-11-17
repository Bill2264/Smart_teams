from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def index():
   return render_template('index.html')


@app.route("/")
def end_table():
    return render_template('end_table.html')

@app.route("/")
def end():
    return render_template('end.html')


