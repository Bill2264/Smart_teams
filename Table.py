from flask import Flask, render_template, request, jsonify
from turbo_flask import Turbo

app = Flask(__name__)
turbo = Turbo(app)


data = [
    ("11/11/11", "100.0","income","default"),
]
@app.route("/")
def index():
    return render_template('index.html',data=data)
    
@app.route("/update")
def row():
    data.extend(("11/11/11", "100.0","income","default"),)