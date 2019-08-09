from flask import Flask, jsonify, request
from bson.json_util import dumps, ObjectId
import json
from flask_pymongo import PyMongo
from flask_cors import CORS

# import os

# heroku_mdb = os.environ.get('MDB', None)

app = Flask(__name__)
config_object = 'settings'
app.config.from_object(config_object)
print(app.config)
CORS(app)

# if heroku_mdb:
#     app.config['MONGO_URI'] = heroku_mdb
# else:
#     app.config['MONGO_URI'] = 'mongodb://localhost/mycontacts_db'

mongo = PyMongo(app)

# Routes and Controllers

# GET /
# @app.route('/', methods=['GET'])
# def index():
#     return jsonify({
#         'msg': 'API MYCONTACTS PY',
#         'status': 'ok'
#     })



@app.route('/',methods=['GET'])
def groups():
    return jsonify({
    'groups' : 'json.loads(res)'
    })

@app.route('/groups',methods=['GET'])
def groups_get():
    collection = mongo.db.groups
    res = dumps( collection.find({}) )
    return jsonify({
    'groups' : json.loads(res)
    })


# Start Point
if __name__ == '__main__':
    app.run()
