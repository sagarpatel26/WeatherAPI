from app import app, BASE_URL
from flask import jsonify, request
import urllib2
import json
import datetime as dt

@app.route('/')
def landing_message():
    return 'Refer to github.com/sagarpatel26/WeatherAPI for the API Docs.'

@app.route('/weather/', methods=['GET'])
def weather_default():
    return jsonify(get_past_7_days_weather(q_param = request.remote_addr))

@app.route('/weather/q/<q>/', methods=['GET'])
def weather_q(q):
    return jsonify(get_past_7_days_weather(q_param = q))

@app.errorhandler(404)
def handle404(e):
    return 'Something went wrong please report [' + str(e) + ']'

# core functions
def get_past_7_days_weather(q_param):
    weather_url = BASE_URL + '&q=' + str(q_param) + get_past_days_params()
    return get_response(weather_url)

def get_past_days_params():
    today_date = dt.datetime.today()
    date_7_back = today_date - dt.timedelta(days = 6)
    return '&enddate=' + today_date.strftime('%Y-%m-%d')  + '&date=' + date_7_back.strftime('%Y-%m-%d')  + '&tp=24'

def get_response(url):
    return json.loads(urllib2.urlopen(url).read().decode())
