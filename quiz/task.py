from flask import Flask, render_template, jsonify
from data import questions

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")


@app.route("/data.py/quiz")
def get_quiz():
    return jsonify(questions)

if __name__ =="__main__":
    app.run(debug=True)
    