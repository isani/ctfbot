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