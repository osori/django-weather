import json, requests

# Flickr API: For fetching related images of location
FLICKR_API_KEY = 'Add your own'
FLICKR_SECRET = 'Add your own'
FLICKR_SEARCH_URL = 'https://api.flickr.com/services/rest/'

class FlickrPhoto(object):
	def __init__(self, query):
		self.query = query
		self.photo_list = self.loadPhotos();

	def loadPhotos(self):
		photo_list = []
		params = {
			'method':'flickr.photos.search',
			'api_key':FLICKR_API_KEY,
			'secret':FLICKR_SECRET,
			'text': self.query,
			# 'geo_context': 2, # outdoors option, currently not implemented on flickr yet
			'sort': 'relevance',
			'safe_search': 1,
			'format':'json',
			'nojsoncallback': 1,
			'extras': 'original_format',
		}

		response = requests.get(FLICKR_SEARCH_URL, params=params)
		json = response.json()

		for photo in json['photos']['photo']:
			has_original = 0;
			photo_list.append(self.getURLtoPhoto(photo, has_original))

		return photo_list

	def getURLtoPhoto(self, flickr_photo, has_original):
		if (has_original):
			return "https://farm" + str(flickr_photo['farm'])+ ".staticflickr.com/" + flickr_photo['server'] + "/" + flickr_photo['id'] + "_" + flickr_photo['originalsecret'] + "_o." + flickr_photo['originalformat']

		else:
			return "https://farm" + str(flickr_photo['farm'])+ ".staticflickr.com/" + flickr_photo['server'] + "/" + flickr_photo['id'] + "_" + flickr_photo['secret'] + "_z.jpg"
