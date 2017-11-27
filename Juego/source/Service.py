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

	def get_highs_score(self):
		highs_score = urllib2.urlopen('http://localhost:8000/player_list/').read()
		data = {u'highs_score':json.loads(highs_score)}
		# print(data['scenarios'][0]['name'])
		return data
