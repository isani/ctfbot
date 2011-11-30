from general import General
from parser import Parser
from token  import *

parser = Parser()
map = parser.parsemap()
general = General(map)

while (1):
	tokens = parser.parsesituation()
	general.commandtroops(tokens)