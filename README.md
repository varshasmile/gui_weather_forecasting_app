# gui_weather_forecasting_app

Python program to create a Weather Forecasting Application using Python Programming concepts And Tkinter GUI to develop Application.

“WEATHER FORECASTING” using openweathermap API
It is a service that provides weather data, including current weather data, forecasts, and historical data to the developer of web services and mobile application .It provides an API with JSON,XML and HTML formats. To use this current weather data API ,one must need the API key, User needs to create an account on openweathermap.org then only can use theAPIs. We use two modules in the program ‘requests’ And ‘JSON’.

User will enter the city name & the current temperature; humidity, pressure and wind, all details will be fetched from openweatherapi. System will take these parameters and will predict weather. Weather forecasting system takes parameters such as temperature, humidity, pressure, and wind and will forecast weather based on previous record therefore this prediction will prove reliable.

	Importing the module – tkinter

Modules required:
	Tkinter requests
	json

API call:
 http://api.openweathermap.org/data/2.5/forecast?id=524901&APPID={APIKEY}
 Parameters:
 APPID: {APIKEY} is your unique API key
 	Example of API call:
 	api.openweathermap.org/data/2.5/forecast?id=524901&APPID=1111111111

to start with (after installing python in your system - tkinter is already built-in):
pip install geopy
pip install timezonefinder
pip install requests
pip install pytz
pip install pillow# gui_weather_forecasting_app
