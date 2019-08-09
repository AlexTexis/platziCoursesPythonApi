from flask import Flask, jsonify, request
from db import mongo
from flask_cors import CORS
from groups import groups_bp

app = Flask(__name__)
config_object = 'settings'
app.config.from_object(config_object)
CORS(app)
app.register_blueprint(groups_bp)
mongo.init_app(app)


@app.route('/',methods=['GET'])
def groups():
    return jsonify({
    'message' : 'hello'
    })


# Start Point
if __name__ == '__main__':
    app.run()
