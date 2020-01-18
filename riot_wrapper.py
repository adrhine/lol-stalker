import os
import requests
import json

class riot_fetcher:	
	def __init__(self, api_key):
		self.api_key = api_key
	# retrieve the uuid backing a summoner name
	def get_summoner_id( self, summoner_name ):
		summoner_response = requests.get(self.summoner_url(summoner_name))

		if (summoner_response.ok):
			return json.loads(summoner_response.content)["id"]

	# retrieve the champion mastery info for a summoner
	def get_mastery_response( self, summoner_name ):
		summoner_id = self.get_summoner_id(summoner_name)

		mastery_response = requests.get(self.mastery_url(summoner_id))

		if (mastery_response.ok):
			return json.loads(mastery_response.content)

	# v4/summoner/by-name
	def summoner_url( self, summoner_name ):
		return "https://na1.api.riotgames.com/lol/summoner/v4/summoners/by-name/{}?api_key={}".format(summoner_name, self.api_key)
	# v4/champion-masteries/by-summoner
	def mastery_url( self, summoner_id ):
		return "https://na1.api.riotgames.com/lol/champion-mastery/v4/champion-masteries/by-summoner/{}?api_key={}".format(summoner_id, self.api_key)