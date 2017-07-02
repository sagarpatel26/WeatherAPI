from app import app, BASE_URL
from flask import jsonify, request
import urllib2
import json
import datetime as dt

@app.route('/weather', methods=['GET'])
def weather_default():
    return jsonify(get_past_7_days_weather(q_param = 30052))

@app.route('/weather/zip/<int:_zip>', methods=['GET'])
def weather_zip(_zip):
    return jsonify(get_past_7_days_weather(q_param = _zip))

@app.route('/weather/my', methods=['GET'])
def weather_user_location():
    remote_user_ip = request.remote_addr
    return jsonify(get_weather_ip_addr(q_param = remote_user_ip))

# core functions
def get_past_7_days_weather(q_param):
    zip_location_url = BASE_URL + '&q=' + str(q_param) + get_past_days_params()
    return get_response(zip_location_url)

def get_past_days_params():
    today_date = dt.datetime.today()
    date_7_back = today_date - dt.timedelta(days = 6)
    return '&enddate=' + today_date.strftime('%Y-%m-%d')  + '&date=' + date_7_back.strftime('%Y-%m-%d')  + '&tp=24'

def get_response(url):
    return json.loads(urllib2.urlopen(url).read().decode())
