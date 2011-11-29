from parser import *
from token  import *

p = Parser()
tokens = p.parse()
for token in tokens:
	print(token)