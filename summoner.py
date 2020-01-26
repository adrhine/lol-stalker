class Summoner:
	def __init__( self, id: str = None, account_id: str = None, puuid: str = None, name: str = None, summonerLevel: int = 0 ):
		if id is not None:
			self.id = id
		if account_id is not None:
			self.account_id = account_id
		if puuid is not None:
			self.puuid = puuid
		if name is not None:
			self.name = name
		if summonerLevel is not None:
			self.summonerLevel = summonerLevel
		# let's initiate champ_history
		self.champ_history = []
	def add_match( self, champions, match ):
		championId = match["champion"]
		# first check to see if we have already recorded matches with this champion
		for champion_id, champ_history in self.champ_history:
			if int(champion_id) == int(championId):
				champ_history.add_match(match)
				return
		# we must not have recorded a match with this champion yet, so look them up
		for champion_id, champion in champions:
			if int(champion_id) == int(championId):
				self.champ_history.append((champion.id, Champ_History(match, champion)))
				return

# holds information regarding matches played with a chmpion
class Champ_History:
	def __init__( self, match_data, champion ):
		self.champion = champion
		self.game_count = 1
		self.matches = [ match_data ]
	def add_match( self, match_data ):
		self.matches.append(match_data)
		self.game_count += 1
	def __repr__( self ):
		return "{game_count} games on {champion_name}".format(game_count = self.game_count, champion_name = self.champion.name)
