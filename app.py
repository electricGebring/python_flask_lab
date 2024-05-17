from flask import Flask, jsonify
from datetime import datetime


def say_apa():
	return "Apa"



app = Flask(__name__)

@app.route('/date', methods=['GET'])
def get_date():
    current_date = datetime.now().strftime('%Y-%m-%d')
    return jsonify({'date': current_date})

if __name__ == '__main__':
    app.run(debug=True)


