from flask import Flask, jsonify, redirect, url_for, render_template, request
from datetime import datetime
from pymongo import MongoClient

import json


# Helper function to read and write JSON file
def read_json():
    with open('superheroes.json', 'r') as file:
        data = json.load(file)
    return data

def write_json(data):
    with open('superheroes.json', 'w') as file:
        json.dump(data, file, indent=4)


app = Flask(__name__)

@app.route('/',  methods=['GET'])
def home():
    return render_template('index.html')


@app.route('/date', methods=['GET'])
def get_date():
    print("In date function")
    current_date = datetime.now().strftime('%Y-%m-%d')
    return jsonify({'date': current_date})


@app.route('/superheroes')
def superheroes():
    data = read_json()
    return render_template('list.html', superheroes=data['superheroes'])


@app.route('/submit_superheroes', methods=['GET', 'POST'])
def submit_superheroes():
    if request.method == 'POST':
        superhero_name = request.form['superhero_name']
        data = read_json()
        data['superheroes'].append(superhero_name)
        write_json(data)
        # return redirect(url_for('superheroes'))
        return redirect("/superheroes")
    else:
        return render_template('submit.html')


client = MongoClient('mongodb://host.docker.internal:27017/')
db = client['bananDb']
collection = db['bananFilm']


@app.route('/film', methods=['GET'])
def get_documents():
    documents = list(collection.find())
    for document in documents:
        document['_id'] = str(document['_id'])  # Convert ObjectId to string for JSON serialization
    return jsonify(documents), 200


if __name__ == '__main__':
    app.run(debug=True, port=5000, host='0.0.0.0')


