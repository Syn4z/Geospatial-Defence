from flask import request, jsonify, Blueprint
from datetime import datetime
from sentinel_api import *
from weather_api import *
from models import *
from gpt_api import *

api = Blueprint('api', __name__)

@api.route('/api/welcome/', methods=['GET'])
def welcome():
    return jsonify({'message': 'Welcome to the API!'})

@api.route('/api/real_image/', methods=['POST'])
def real_image():
    data = request.get_json()
    client_id = data['client_id']
    client_secret = data['client_secret']

    coords = data['coordinates']
    time_interval = data['time_interval']
    if 'resolution' in data:
        resolution = data['resolution']
    else:
        resolution = 10
    if 'distance' in data:
        distance = data['distance']
    else:
        distance = 1

    config = set_up_sentinelhub_config(client_id, client_secret)
    img = get_sentinelhub_colored_img(config, coords, time_interval, resolution, distance)

    return jsonify({'message': 'image', 'image': str(img)}), 200

@api.route('/api/colored_image_ndmi/', methods=['POST'])
def colored_image_ndmi():
    data = request.get_json()
    client_id = data['client_id']
    client_secret = data['client_secret']

    coords = data['coordinates']
    time_interval = data['time_interval']
    if 'resolution' in data:
        resolution = data['resolution']
    else:
        resolution = 10
    if 'distance' in data:
        distance = data['distance']
    else:
        distance = 1

    config = set_up_sentinelhub_config(client_id, client_secret)
    img = get_sentinelhub_colored_img(config, coords, time_interval, resolution, distance)

    return jsonify({'message': 'image', 'image': str(img)}), 200

@api.route('/api/predict_seed_rate/', methods=['POST'])
def pred_seed_rate():
    data = request.get_json()

    seed_type = data['seed_type']
    coords = data['coordinates']

    weather_data = get_forecast_weather(coords)
    ndmi_data = predict_ndmi(weather_data)
    seed_rate = predict_seed_rate(ndmi_data)

    return jsonify({'message': 'prediction', 'prediction': seed_rate.to_dict(orient="records")}), 200

@api.route('/api/gpt_response/', methods=['POST'])
def gpt_response():
    data = request.get_json()

    seed_type = data['seed_type']
    planting_period = datetime.now().strftime("%Y-%m-%d")
    coords = data['coordinates']

    weather_data = get_forecast_weather(coords)
    ndmi_data = predict_ndmi(weather_data)
    seed_rate = predict_seed_rate(ndmi_data)
    response = chat_gpt(seed_type, planting_period, seed_rate)

    return jsonify({'message': 'response', 'response': response}), 200