#Sean Teeling steeling@calpoly.edu

from bs4 import BeautifulSoup
import re

primary_words = ["spouses", "parents" "Birth","Death", "married", "died", "born", "sibling", "Marriage", "Brother", "sister", "father", "mother", "niece", "nephew", "grandfather", "cousin", "grandmother", "aunt", "uncle"]
def parse_doc(doc):
	distances = []			#[(primary_word, secondary, distance), ]
	soup = BeautifulSoup(doc.lower())
	for p_word in primary_words:	
		p_word = p_word.lower()							#grab each hotword
		for p_elem in soup(text=re.compile(p_word)): 			#grab each occurrence of the hot word
			p_tag = p_elem.parent.name
			min_distance = -1
			#for s_word in secondary_words:						#compare to each secondary word
			for s_elem in soup(text=re.compile(r'\b((1[4-9]\d\d)|(20((1[0-4])|(0\d))))\b')):		#grab each occurrence of the secondary word
				distance = -1
				if s_elem == p_elem:
					distance = calc_same_tag_distance(p_elem,p_word)
				elif (p_elem.parent.name.lower() == 'th' and s_elem.parent.name.lower() == 'td' and p_elem.parent.parent.parent == s_elem.parent.parent.parent) or ((s_elem.parent.name.lower() == 'td' or s_elem.parent.name.lower() == 'th') and (p_elem.parent.name.lower() == 'td' or p_elem.parent.name.lower() == 'th') and s_elem.parent.parent == p_elem.parent.parent): 
					distance = 1
				if distance == -1:
					continue
				#do some distance manipulation
				if distance < min_distance or min_distance == -1:
					min_distance = distance
					min_s_word = s_elem
					s_tag = s_elem.parent.name
			if min_distance != -1:
				distances.append(float(min_distance))
	final_score = 0
	for x in distances:
		final_score += 1/x
	return 1 if x > 1 else x

def calc_same_tag_distance(p_elem, p_word):
	counter = 0
	p_elem = re.sub(r'[^\w]', ' ', p_elem)
	s_word = re.findall(r'\b((1[4-9]\d\d)|(20((1[0-4])|(0\d))))\b',p_elem)[0][0]
	p_found = False
 	s_found = False
	for word in p_elem.split(" "):
		counter += 1
		if word == p_word and s_found == False:
			p_found = True
			counter = 0
		if word == s_word:
			s_found = True
			if p_found == False: counter = 0
		if p_found and s_found:
			return counter
	return -1
