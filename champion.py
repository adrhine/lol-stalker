class Champion:
	# assumes champ is a json object, coming from ddragon dump
	def __init__( self, champ ):
		self.id = champ["key"]
		self.name = champ["name"]

	def __repr__(self):
		return self.name + self.id