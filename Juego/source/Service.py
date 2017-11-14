import requests
import urllib2
import json

class DataService():
	def __init__(self):
		pass

	def get_data(self):
		scenarios = urllib2.urlopen('http://localhost:8000/scenarios/').read()
		characters = urllib2.urlopen('http://localhost:8000/characters/').read()
		data = {u'scenarios':json.loads(scenarios),u'characters':json.loads(characters)}
		# print(data['scenarios'][0]['name'])
		return data
