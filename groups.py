from flask import Blueprint,jsonify,request
import json
from bson.json_util import dumps, ObjectId
from db import mongo

groups_bp = Blueprint('groups',__name__,url_prefix='/groups')


@groups_bp.route('/',methods=['GET'])
def groups_get():
  if request.method == 'GET' :
    collection = mongo.db.groups
    res = dumps( collection.find({}) )
    return jsonify({
    'groups' : json.loads(res)
    })

@groups_bp.route('/<idGroup>',methods=['GET'])
def group_get_fn(idGroup) :
    group_id = idGroup
    if request.method == 'GET' and group_id is not None :
        collection = mongo.db.groups
        res = dumps( collection.find_one({'_id' : ObjectId(idGroup)}) )
        return jsonify({'group': json.loads(res)})   

@groups_bp.route('',methods=['POST'])
def groups_post_fn() :
    request_body = request.get_json()
    if request.method == 'POST':
      collection = mongo.db.groups
      res = str(collection.insert_one(request_body).inserted_id)
      return jsonify({ 'data' : res })


@groups_bp.route('/<idGroup>/alumns',methods=['POST'])
def groups_add_stu_fn(idGroup) :
    request_body = request.get_json()
    group_id = idGroup
    if request.method == 'POST' and group_id is not None :
      collection = mongo.db.groups
      collectionStudents = mongo.db.alumns
      projection  = json.loads(dumps(collectionStudents.find_one({ '_id' : ObjectId(request_body.get('_id')) },{'name':1,'surnames':1})))
      ids = projection.get('_id')['$oid']
      name = projection.get('name')
      surnames = projection.get('surnames')
      objectAdd = {'_id' : ids,'name' : name,'surnames' : surnames }

      res = str(collection.update_one({'_id' : ObjectId(group_id)},{'$addToSet' : { 'alumns' : objectAdd }}).modified_count)
      if(res == '1'):
        res = group_id
      return jsonify({ 'data' : res})

@groups_bp.route('/<idGroup>/alumns/<idStudent>',methods=['DELETE'])
def groups_del_stu_fn(idGroup,idStudent) :
    group_id = idGroup
    student_id = idStudent
    print(group_id,student_id)
    if request.method == 'DELETE' and group_id is not None :
      collection = mongo.db.groups
      res = str(collection.update_one({'_id' : ObjectId(group_id)},{'$pull' : { 'alumns' : { '_id' : student_id} }}).modified_count)
      if(res == '1'):
        res = student_id
      return jsonify({ 'removed' : res})


@groups_bp.route('/<idGroup>',methods=['PUT'])
def groups_upd_fn(idGroup) :
    group_id = idGroup
    request_body = request.get_json()
    if request.method == 'PUT' and group_id is not None:
      collection = mongo.db.groups
      res = str( collection.update_one({ '_id' : ObjectId(group_id)},{'$set' : request_body}).modified_count )
      if(res == '0'):
         res = idGroup
      return jsonify({ 'updated' : res})

@groups_bp.route('/<idGroup>',methods=['DELETE'])
def groups_del_fn(idGroup) :
    group_id = idGroup
    if request.method == 'DELETE' and group_id is not None:
      collection = mongo.db.groups
      res = str( collection.delete_one({ '_id' : ObjectId(group_id)}).deleted_count )
      if(res == '0'):
        res = idGroup
      return jsonify({ 'removed' : res})