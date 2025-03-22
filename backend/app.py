from flask import Flask, render_template, jsonify
from database import get_logs, get_threats
import os

app = Flask(__name__, template_folder="../templates", static_folder="../static")


@app.route('/')
def dashboard():
    return render_template('index.html')

@app.route('/api/logs')
def logs():
    return jsonify(get_logs())

@app.route('/api/threats')
def threats():
    return jsonify(get_threats())

if __name__ == '__main__':
    app.run(debug=True)
