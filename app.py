from flask import Flask, jsonify, redirect, url_for, render_template
from datetime import datetime


def say_apa():
	return "Apa"

app = Flask(__name__)


@app.route('/')
def home():
    return render_template('index.html')


@app.route('/date', methods=['GET'])
def get_date():
    print("In date function")
    current_date = datetime.now().strftime('%Y-%m-%d')
    return jsonify({'date': current_date})


if __name__ == '__main__':
    app.run(debug=True)


