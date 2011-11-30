from parser import *
from token  import *

parser = Parser()
map = parser.parsemap()
tokens = parser.parsesituation()
for token in tokens:
	print(token)