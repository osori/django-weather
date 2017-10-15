import json, requests
import random
import time

from .flickrphoto import FlickrPhoto

# For formatting city name query using Google Geocoding API
GOOGLE_API_KEY = 'Add your own'
GEOCODE_URL = "https://maps.googleapis.com/maps/api/geocode/json"

# For fetching weather data from Dark Sky API
DARKSKY_API_KEY = 'Add your own'
WEATHER_URL = 'https://api.darksky.net/forecast/' + DARKSKY_API_KEY + '/'


class Weather(object):
	def __init__(self, location_name):
		self.location_name = location_name
		self.result = ""
		start_time1 = time.time()

		# Get latitude and longitude of the location
		self.lat_lng = self.get_lat_lng()
		self.latlng_time = time.time() - start_time1
		
		# Fetch weather data
		start_time2 = time.time()
		self.weather_json = self.fetch_weather()
		self.get_current_weather()

		# Get location photos from Flickr
		self.photo_url = self.get_location_photo();
		self.fetchweather_time = time.time() - start_time2


	def get_lat_lng(self):
		params = {
			'key' : GOOGLE_API_KEY,
			'address' : self.location_name,
			'language' : 'en'
		}

		response = requests.get(GEOCODE_URL, params=params)
		json = response.json()

		if (len(json['results']) == 0):
			self.result = "__FAIL__"
			return
		else:
			lat_lng = json['results'][0]['geometry']['location']
			ret = repr(lat_lng['lat']) + "," + repr(lat_lng['lng'])
			self.formatted_name = json['results'][0]['address_components'][0]["long_name"]
			self.full_name = json['results'][0]['formatted_address']
		return ret

	def fetch_weather(self):
		if self.result == "__FAIL__": return
		params = {
			'units': 'si'
		}
		response = requests.get(WEATHER_URL + self.lat_lng, params=params)
		json = response.json()

		return json

	def get_current_weather(self):
		if self.result == "__FAIL__": return
		json = self.weather_json['currently']
		self.current_summary = json['summary']
		self.current_temperature = json['temperature']
		self.current_precipProbability = json['precipProbability']
		self.current_humidity = json['humidity']

	def get_location_photo(self):
		fp = FlickrPhoto(self.formatted_name)
		photo_list = fp.photo_list
		try:
			return random.choice(photo_list)
		except Exception as e:
			return "http://lorempixel.com/1024/768/nature/"