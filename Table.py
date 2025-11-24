from flask import Flask, render_template, request, jsonify
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

@app.route("/")
def index():
    return render_template('index.html')
    
@app.route("/update", methods=['row'])
def row():
    return render_template('table.html')

class data:
    date=11/11/11
    amount = 100.0
    type = 'income'
    note = 'default'

if __name__ == '__main__':
    app.run(debug=True)