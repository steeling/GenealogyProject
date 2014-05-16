import os
# import findDistance, nltk
# from findDistance import parse_doc

# namesCorpus = nltk.corpus.names

# names = []
# names.extend(namesCorpus.words('male.txt'))
# names.extend(namesCorpus.words('female.txt'))

distances = []
num_pos = 0.0
num_neg = 0.0
num_neutral = 0.0
primary_words = ["spouses", "parents" "Birth","Death", "married", "died", "born", "sibling", "Marriage", "Brother", "sister", "father", "mother", "niece", "nephew", "grandfather", "cousin", "grandmother", "aunt", "uncle"]
total_score = 0.0
count = 0

for filename in os.listdir(os.getcwd()):
	f = open(filename, "r")
	text = f.read()
	count += 1
	print filename
	dist = parse_doc(text, primary_words)
	print count,        dist
	if dist < .1:
		num_neg += 1
	if dist > .1:
		num_pos += 1
	if dist == .1:
		num_neutral += 1
	total_score += dist

print num_neutral + num_pos + num_neg, num_pos, num_neg, num_neutral, total_score/count
