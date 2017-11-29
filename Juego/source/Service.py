import requests
import urllib2
import urllib
import json

class DataService():
	def __init__(self):
		pass

	def get_data(self):
		scenarios = urllib2.urlopen('https://ulimasoftware2.herokuapp.com/scenarios/').read()
		characters = urllib2.urlopen('https://ulimasoftware2.herokuapp.com/characters/').read()
		data = {u'scenarios':json.loads(scenarios),u'characters':json.loads(characters)}
		# print(data['scenarios'][0]['name'])
		return data

	def get_highs_score(self):
		highs_score = urllib2.urlopen('https://ulimasoftware2.herokuapp.com/player_list/').read()
		data = {u'highs_score':json.loads(highs_score)}
		# print(data['scenarios'][0]['name'])
		return data


	def post_score(self, player):
		url = 'https://ulimasoftware2.herokuapp.com/player_list/'
		opener = urllib2.build_opener(urllib2.HTTPHandler(debuglevel=1))
		data = urllib.urlencode({'name' : player.name,
								'initial_year'  : player.entrant,
								'finish_year' : player.graduate,
								'score': player.score + player.lifes * 1000,
								'character': player.character})
		content = opener.open(url, data=data).read()
		urllib2.urlopen('http://localhost:8000/player_list/').read()
