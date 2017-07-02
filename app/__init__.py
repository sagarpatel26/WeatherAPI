from flask import Flask 

app = Flask(__name__)


BASE_URL = 'http://api.worldweatheronline.com/premium/v1/past-weather.ashx?key=??&format=json'

from app import weather 
