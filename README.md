Weather API

Creating Simple Web Service to return past week weather information based on the location.

In order to get the historic weather data API provided by https://www.worldweatheronline.com/ is used, the service currently returns the weather information as provided by the API mentioned earlier, for last 7 days. It uses the start_date, end_date and time_period (24 Hrs) parameter as the fields to query the weather data.

The Service can be called https://weatherapi-172512.appspot.com hosted on Google Cloud Platform. Currently service supports:

1. https://weatherapi-172512.appspot.com/weather : This API check the users IP address and returns the corresponding location's weather information.
2. https://weatherapi-172512.appspot.com/weather/q/<param> : Here the param can be one of the following values:
    a. City or town name (eg., New+York; New+york,ny; London,united+kingdom) 
    b. UK or Canada Postal Code or US Zipcode (90201, 98101, 30052)
    c. Latitude and longitude (two comma separated numeric values, q=48.834,2.394)

In order to setup & deploy please follw the instructions from https://cloud.google.com/appengine/docs/standard/python/getting-started/python-standard-env.
