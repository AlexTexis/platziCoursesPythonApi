from flask import Flask, jsonify
from blueprints.db import mongo
from flask_cors import CORS

#blueprints
from blueprints.courses import courses_bp
from blueprints.students import students_bp
from blueprints.classes import classes_bp

app = Flask(__name__)
config_object = 'settings'
app.config.from_object(config_object)
CORS(app)
app.register_blueprint(courses_bp)
app.register_blueprint(students_bp)
app.register_blueprint(classes_bp)
mongo.init_app(app)


@app.route('/',methods=['GET'])
def groups():
    return jsonify({
    'message' : 'platziCourses with flask'
    })


# Start Point
if __name__ == '__main__':
    app.run()
