from flask import Blueprint,jsonify,request
import json
from bson.json_util import dumps, ObjectId
from .db import mongo

courses_bp = Blueprint('courses',__name__,url_prefix='/courses')


@courses_bp.route('/',methods=['GET'])
def get_all():
    courses = {}

    if request.method == 'GET' :
        collection = mongo.db.courses
        courses = dumps( collection.find({}) )

    return jsonify({
    'data' : json.loads(courses)
    })


@courses_bp.route('/<idCourse>',methods=['GET'])
def get_one(idCourse) :
    course_id = idCourse
    course = {}

    if request.method == 'GET' and course_id is not None :
        collection = mongo.db.courses
        course = dumps( collection.find_one({'_id' : ObjectId(course_id)}) )

    return jsonify({
    'data': json.loads(course)
    })   


@courses_bp.route('',methods=['POST'])
def create() :
    created = {}
    request_body = request.get_json()

    if request.method == 'POST':
        collection = mongo.db.courses
        response = str(collection.insert_one(request_body).inserted_id)
        created = dumps({'_id' : response,**request_body })

    return jsonify({
    'data' : json.loads(created)
    })


@courses_bp.route('/<idCourse>',methods=['PUT'])
def update(idCourse) :
    course_id = idCourse
    request_body = request.get_json()
    updated = {}

    if request.method == 'PUT' and course_id is not None:
        collection = mongo.db.courses     
        response = str( collection.update_one({ '_id' : ObjectId(course_id)},{'$set' : request_body}).modified_count )
        if response == '1':
            updated = dumps({ '_id' : course_id,**request_body })

    return jsonify({
    'data' : json.loads(updated)
    })


@courses_bp.route('/<idGroup>',methods=['DELETE'])
def delete(idCourse) :
    course_id = idCourse
    deleted = ''

    if request.method == 'DELETE' and course_id is not None:
        collection = mongo.db.courses
        response = str( collection.delete_one({ '_id' : ObjectId(course_id)}).deleted_count )
        if response == '1' :
            deleted = course_id

    return jsonify({
    'data' : {'courseRemoved' : deleted }
    })

# STUDENTS

@courses_bp.route('/<idCourse>/students',methods=['POST'])
def add_student(idCourse) :
    request_body = request.get_json()
    course_id = idCourse
    projection = {}
    studentAdd = {}

    if request.method == 'POST' and course_id is not None :
        collectionCourse = mongo.db.courses
        collectionStudents = mongo.db.students

        # projection Student
        projection = json.loads(dumps(collectionStudents.find_one({
        '_id' : ObjectId(request_body.get('_id')) },
        {'name':1,'surnames':1
        })))

        #get attrs projection
        _idStudent = projection.get('_id')['$oid']
        nameStudent = projection.get('name')
        surnamesStudent = projection.get('surnames')
        studentObject = {'_id' : _idStudent,'name' : nameStudent,'surnames' : surnamesStudent }

        response = str(collectionCourse.update_one({
        '_id' : ObjectId(course_id)},
        {'$addToSet' : { 'alumns' : studentObject }
        }).modified_count)

        if(response == '1'):
            studentAdd = projection

    return jsonify({
    'data' : { '_id' : course_id,'saved' : studentAdd }
    })


@courses_bp.route('/<idCourse>/students/<idStudent>',methods=['DELETE'])
def remove_student(idCourse,idStudent) :
    course_id = idCourse
    student_id = idStudent
    student_removed = ''

    if request.method == 'DELETE' and course_id is not None :
        collection = mongo.db.courses
        response = str(collection.update_one({
            '_id' : ObjectId(course_id)},
            {'$pull' : { 'alumns' : { '_id' : student_id} }
            }).modified_count)

        if(response == '1'):
            student_removed = student_id

    return jsonify({
    'data' : { 
        '_id' :course_id , 'removed' : student_removed 
    } 
    })

# CLASSES
@courses_bp.route('/<idCourse>/classes',methods=['POST'])
def add_class(idCourse) :
    request_body = request.get_json()
    course_id = idCourse
    projection = {}
    classAdd = {}

    if request.method == 'POST' and course_id is not None :
        collectionCourse = mongo.db.courses
        collectionClass = mongo.db.classes

        #projection class
        projection = json.loads(dumps(collectionClass.find_one({
        '_id' : ObjectId(request_body.get('_id')) },
        {'name':1,'label':1
        })))

        #get attrs projection
        _idClass = projection.get('_id')['$oid']
        nameClass = projection.get('name')
        nameLabel = projection.get('label')
        classObject = {'_id' : _idClass,'name' : nameClass,'label' : nameLabel }

        response = str(collectionCourse.update_one({
        '_id' : ObjectId(course_id)},
        {'$addToSet' : { 'class' : classObject }
        }).modified_count)

        if(response == '1'):
            classAdd = projection

    return jsonify({
    'data' : { '_id' : course_id,'saved' : classAdd }
    })


@courses_bp.route('/<idCourse>/classes/<idClase>',methods=['DELETE'])
def remove_class(idCourse,idClase) :
    course_id = idCourse
    class_id = idClase
    class_removed = ''
    if request.method == 'DELETE' and course_id is not None :
        collection = mongo.db.courses
        response = str(collection.update_one({
        '_id' : ObjectId(course_id)},
        {'$pull' : { 'class' : { '_id' : class_id } }
        }).modified_count)

        if(response == '1'):
            class_removed = class_id

    return jsonify({
    'data' : { 
        '_id' :course_id , 'removed' : class_removed 
    } 
    })