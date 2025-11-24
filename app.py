from flask import Flask, render_template, request, jsonify
from turbo_flask import Turbo

app = Flask(__name__)
turbo = Turbo(app)

@app.route("/")
def index():
    return render_template('index.html')
    
@app.route("/update")
def row():
    return turbo.stream(turbo.replace('dynamic-content', 'Updated Content!'))

class data:
    date=11/11/11
    amount = 100.0
    type = 'income'
    note = 'default'
