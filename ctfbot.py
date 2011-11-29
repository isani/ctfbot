from sys import stdin

class Token(object):
	def __init__(self, x, y):
		self.x = x
		self.y = y

class Fighter(Token):
	def __init__(self, name, x, y, alive, flag):
		super(Fighter, self).__init__(x, y)
		self.name = name
		self.alive = alive
		self.flag = flag

class Soldier(Fighter):
	def __init__(self, name, x, y, cooldown, alive, flag):
		super(Soldier, self).__init__(name, x, y, alive, flag)
		self.cooldown = cooldown

class Enemy(Fighter):
	def __init__(self, name, x, y, alive, flag):
		super(Enemy, self).__init__(name, x, y, alive, flag)

class Flag(Token):
	def __init__(self, x, y):
		super(Flag, self).__init__(x, y)

class EnemyFlag(Token):
	def __init__(self, x, y):
		super(EnemyFlag, self).__init__(x, y)

class Grenade(Token):
	def __init__(self, x, y, countdown):
		super(Grenade, self).__init__(x, y)
		self.countdown = countdown
		
class Parser:
	
	def parse(self):
		line = stdin.readline() # Side
		line = stdin.readline() # First line of map
		while line != "\n":
			# Parse map here
			line = stdin.readline()
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

p = Parser()
tokens = p.parse()
for token in tokens:
	print(token)