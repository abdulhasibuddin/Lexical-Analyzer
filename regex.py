import re

string = []
string = input()

for s in string:
	#print(s)
	if re.match(r'\d', s):
		#print("f2")
		print(s)
