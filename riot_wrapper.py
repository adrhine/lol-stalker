import os
import requests
import json
import util

from summoner import Summoner

class riot_fetcher:	
	def __init__( self, api_key ):
		self.api_key = api_key
	
	def get_summoner( self, summoner_name ):
		summoner_response = requests.get(self.summoner_url(summoner_name))

		if (summoner_response.ok):
			id = util.parse_summoner_response(summoner_response, "id")
			account_id = util.parse_summoner_response(summoner_response, "accountId")
			return Summoner(id = id, account_id = account_id)
		else:
			raise RuntimeError("Error retrieving Riot Data")

	# retrieve the champion mastery info for a summoner
	def get_mastery_response( self, summoner_name ):
		summoner_id = self.get_summoner(summoner_name).id

		mastery_response = requests.get(self.mastery_url(summoner_id))

		if (mastery_response.ok):
			return json.loads(mastery_response.content)
		else:
			raise RuntimeError("Error retrieving Riot Data")

	def get_match_history( self, summoner: Summoner ):
		account_id = summoner.account_id

		response = requests.get(self.matchlist_url(account_id))

		if (response.ok):
			return json.loads(response.content)["matches"]
		else:
			raise RuntimeError("Error retrieving Riot Data")

	# v4/summoner/by-name
	def summoner_url( self, summoner_name ):
		return "https://na1.api.riotgames.com/lol/summoner/v4/summoners/by-name/{summoner_name}?api_key={api_key}".format(summoner_name = summoner_name, api_key = self.api_key)
	# v4/champion-masteries/by-summoner
	def mastery_url( self, summoner_id ):
		return "https://na1.api.riotgames.com/lol/champion-mastery/v4/champion-masteries/by-summoner/{}?api_key={}".format(summoner_id, self.api_key)
	# v4/matchlists/by-account/{encryptedAccountId}
	def matchlist_url( self, encryptedAccountId ):
		return "https://na1.api.riotgames.com/lol/match/v4/matchlists/by-account/{}?api_key={}".format(encryptedAccountId, self.api_key)