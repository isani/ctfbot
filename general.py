from token import *

class General:

	def __init__(self, map):
		self.map = map
	
	def commandtroops(self, tokens):
		for token in tokens:
			if type(token) == Soldier:
				print(token.name + " S")