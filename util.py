import json
from champion import Champion

def parse_mastery_response(mastery_response, field_name):
	counter = 0
	for champion in mastery_response:
		counter += champion[field_name]

	return counter

def parse_summoner_response(summoner_response, field_name):
	return json.loads(summoner_response.content)[field_name]

def championBootstrap():
	champions = []
	#TODO: we should find a better way to include this resource
	with open('./resources/champion.json') as champion_file:
		body = json.load(champion_file)

	for champ_name, championData in body["data"].items():
		champion = Champion(championData)
		champions.append((champion.id, champion))

	# goofy check to make sure that we have a lot of champions loaded
	if (len(champions) > 100):
		print("Bootstrapped Champions Successfully")
	else:
		raise RuntimeError("Error bootstrapping champion data")
	
	return champions