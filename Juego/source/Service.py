import requests
import urllib2
import json

class DataService():
	def __init__(self):
		pass

	def get_data(self):
		request = urllib2.urlopen('http://localhost:8000/data/').read()
		content = json.loads(request)
		return content
