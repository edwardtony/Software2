import requests

class DataService():
	def __init__(self):
		pass
	
	def get_data(self):
		r = requests.get('http://localhost:8000/data/')
		print(r.json())