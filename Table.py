from flask import Flask, render_template# type: ignore

app = Flask(__name__)

class draw:
    @app.route("/")
    def index():
        return render_template('index.html')


Draw = draw()

Draw.index
