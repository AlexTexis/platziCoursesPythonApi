from flask import Flask, jsonify, request
from flask_pymongo import PyMongo
from flask_cors import CORS

import os

heroku_mdb = os.environ.get('MDB', None)

app = Flask(__name__)

CORS(app)

if heroku_mdb:
    app.config['MONGO_URI'] = heroku_mdb
else:
    app.config['MONGO_URI'] = 'mongodb://localhost/mycontacts_db'

mongo = PyMongo(app)

# Routes and Controllers

# GET /
@app.route('/', methods=['GET'])
def index():
    return jsonify({
        'msg': 'API MYCONTACTS PY',
        'status': 'ok'
    })

# GET /contacts
@app.route('/contacts', methods=['GET'])
def get_contacts():
    contacts = mongo.db.contacts

    output = []

    for c in contacts.find():
        output.append({
            '_id': str(c['_id']),
            'name': c['name'],
            'phone': c['phone'],
            'email': c['email']
        })

    return jsonify({
        'contacts': output
    })

# POST /contacts
@app.route('/contacts', methods=['POST'])
def post_contacts():
    contacts = mongo.db.contacts

    name = request.json['name']
    phone = request.json['phone']
    email = request.json['email']

    contact_id = contacts.insert({
        'name': name,
        'phone': phone,
        'email': email
    })

    return jsonify({
        '_id': str(contact_id),
        'name': name,
        'phone': phone,
        'email': email
    })

# DELETE /contacts/
@app.route('/contacts/<ObjectId:contact_id>', methods=['DELETE'])
def delete_contact(contact_id):
    contacts = mongo.db.contacts

    contacts.delete_one({'_id': contact_id})

    return jsonify({
      'msg': 'Contact Deleted',
      'status': 'ok'
    })


# Start Point
if __name__ == '__main__':
    app.run()
