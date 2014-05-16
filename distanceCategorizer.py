import findDistance
from findDistance import parse_doc

primary_words = ["spouses", "parents" "Birth","Death", "married", "died", "born", "sibling", "Marriage", "Brother", "sister", "father", "mother", "niece", "nephew", "grandfather", "cousin", "grandmother", "aunt", "uncle"]

#74f576572d25a17156a6f929dae2d008

def getScores(docs, a):  #a == number of "buckets" to categorize (higher the bucket, the higher the confidence)
	#pass it a bunch of docs, it will return list of scores, one for each doc
	threshold = []
	raw_scores = {}
	final_scores = {}

	for doc in docs:
		raw_scores[doc] = parse_doc(doc,primary_words)
	for i in xrange(0,a):
		threshold.append(raw_scores[len(raw_scores) * (i+1)/ a])

	for doc in docs:
		for i in xrange(0,len(threshold)):
			if raw_scores[doc] < threshold[i]
				final_scores[doc] = threshold[i]
	return final_scores