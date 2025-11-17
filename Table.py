from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def index():
    return "<!DOCTYPE html><html><head><title>Flask Dynamic Data</title></head><body><h1>Table</h1><div></div><table><tr><th>Date</th><th>Amount</th><th>type</th><th>Note</th></tr><tr><td>11/11/11</td><td>$100</td><td>Income</td><td>car wash</td></tr></table> </body></html>"

