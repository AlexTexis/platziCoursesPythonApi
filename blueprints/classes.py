from flask import Blueprint,jsonify,request
import json
from bson.json_util import dumps, ObjectId
from  .db import mongo

classes_bp = Blueprint('classes',__name__,url_prefix='/classes')

@classes_bp.route('/',methods=['GET'])
def get_all():
      classes = {}

      if request.method == 'GET' :
            collection = mongo.db.classes
            classes = dumps( collection.find({}) )

      return jsonify({
      'data' : json.loads(classes)
      })


@classes_bp.route('/<idClass>',methods=['GET'])
def get_one(idClass) :
      class_id = idClass
      clase = {}

      if request.method == 'GET' and class_id is not None :
            collection = mongo.db.classes
            clase = dumps( collection.find_one({'_id' : ObjectId(class_id)}) )

      return jsonify({
      'data': json.loads(clase)
      }) 


@classes_bp.route('',methods=['POST'])
def create() :
      created = {}
      request_body = request.get_json()

      if request.method == 'POST':
            collection = mongo.db.classes
            response = str(collection.insert_one(request_body).inserted_id)
            created = dumps({'_id' : response,**request_body })

      return jsonify({
      'data' : json.loads(created)
      })


@classes_bp.route('/<idClass>',methods=['DELETE'])
def delete(idClass) :
      class_id = idClass
      deleted = ''

      if request.method == 'DELETE' and class_id is not None:
            collection = mongo.db.classes
            response = str( collection.delete_one({ '_id' : ObjectId(class_id)}).deleted_count )
            if response == '1' :
                  deleted = class_id

      return jsonify({
      'data' : {'classRemoved' : deleted }
      })