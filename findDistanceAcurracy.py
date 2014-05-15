import os, findDistance

from findDistance import parse_doc
distances = []
num_pos = 0.0
num_neg = 0.0
num_neutral = 0.0
for filename in os.listdir(os.getcwd()):
	f = open(filename, "r")
	text = f.read()
	dist = parse_doc(text)
	if dist < .5:
		num_neg += 1
	if dist > .5:
		num_pos += 1
	if dist == .5:
		num_neutral += 1

print num_neutral + num_pos + num_neg, num_pos, num_neg, num_neutral 
