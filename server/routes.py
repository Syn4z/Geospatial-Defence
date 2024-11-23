from flask import request, jsonify, Blueprint


api = Blueprint('api', __name__)

api.route('/api/welcom', methods=['GET'])
def welcome():
    return jsonify({'message': 'Welcome to the API!'})