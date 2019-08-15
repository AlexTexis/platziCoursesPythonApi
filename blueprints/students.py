from flask import Blueprint,jsonify,request
import json
from bson.json_util import dumps, ObjectId
from .db import mongo

students_bp = Blueprint('students',__name__,url_prefix='/students')

@students_bp.route('/',methods=['GET'])
def get_all():
      students = {}

      if request.method == 'GET' :
            collection = mongo.db.alumns
            students = dumps( collection.find({}) )

      return jsonify({
      'data' : json.loads(students)
      })


@students_bp.route('/<idStudent>',methods=['GET'])
def get_one(idStudent) :
      student_id = idStudent
      student = {}

      if request.method == 'GET' and student_id is not None :
            lection = mongo.db.alumns
            student = dumps( collection.find_one({'_id' : ObjectId(student_id)}) )

      return jsonify({
      'data': json.loads(student)
      }) 


@students_bp.route('',methods=['POST'])
def create() :
      created = {}
      request_body = request.get_json()

      if request.method == 'POST':
            collection = mongo.db.alumns
            response = str(collection.insert_one(request_body).inserted_id)
            created = dumps({'_id' : response,**request_body })

      return jsonify({
      'data' : json.loads(created)
      })


@students_bp.route('/<idStudent>',methods=['PUT'])
def update(idStudent) :
      student_id = idStudent
      updated = ''
      request_body = request.get_json()

      if request.method == 'PUT' and student_id is not None:
            collection = mongo.db.alumns     
            response = str( collection.update_one({ '_id' : ObjectId(student_id)},{'$set' : request_body}).modified_count )
            if response == '1':
                  updated = dumps({ '_id' : student_id,**request_body })

      return jsonify({
      'data' : json.loads(updated)
      })


@students_bp.route('/<idStudent>',methods=['DELETE'])
def delete(idStudent) :
      student_id = idStudent
      deleted = ''

      if request.method == 'DELETE' and student_id is not None:
            collection = mongo.db.alumns
            response = str( collection.delete_one({ '_id' : ObjectId(student_id)}).deleted_count )
            if response == '1' :
                  deleted = student_id

      return jsonify({
      'data' : {'studentRemoved' : deleted }
      })