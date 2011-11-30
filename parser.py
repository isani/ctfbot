from token import *
from sys import stdin

class Parser:
	
	def parsemap(self):
		line = stdin.readline() # Side
		line = stdin.readline() # First line of map
		while line != "\n":
			# Todo: Parse map here
			line = stdin.readline()
		return None
	
	def parsesituation(self):
		line = stdin.readline() # Score
		tokens = []
		line = stdin.readline() # First line of tokens
		while line != "\n":
			tokens.append(self.parsetoken(line))
			line = stdin.readline()
		return tokens

	def parsetoken(self, line):
		l = line.split()
		if l[0] == "Flag":
			return Flag(int(l[1]), int(l[2]))
		if l[0] == "Soldier":
			return Soldier(l[1], int(l[2]), int(l[3]), int(l[4]), l[5] == "True", l[6])
		if l[0] == "Grenade":
			return Grenade(int(l[1]), int(l[2]), int(l[3]))
		if l[0] == "EnemyFlag":
			return EnemyFlag(int(l[1]), int(l[2]))
		if l[0] == "Enemy":
			return Enemy(l[1], int(l[2]), int(l[3]), l[4] == "True", l[5])
