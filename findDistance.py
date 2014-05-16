#Sean Teeling steeling@calpoly.edu

from bs4 import BeautifulSoup
import re

def parse_doc(doc, primary_words):
	distances = []			#[(primary_word, secondary, distance), ]
	soup = BeautifulSoup(doc.lower())
	for e in soup.findAll('br'):
	    e.extract()
	counter = 0
	for p_word in primary_words:	
		p_word = p_word.lower()							#grab each hotword
		for p_elem in soup(text=re.compile(p_word)): 			#grab each occurrence of the hot word
			p_tag = p_elem.parent.name
			min_distance = -1
			#for s_word in secondary_words:						#compare to each secondary word
			for s_elem in soup(text=re.compile(r'\b((1[4-9]\d\d)|(20((1[0-4])|(0\d))))\b')):		#grab each occurrence of the secondary word
				distance = -1
				if s_elem == p_elem:
					print "same tag"
					distance = calc_same_tag_distance(p_elem,p_word)
				elif s_elem.parent == p_elem.parent:
					print "parent same"
					for temp_s in s_elem.parent:
						counter += 1
						if temp_s == p_elem:
							distance = counter
							break
					pass
					#distance = calc_same_tag_distance(p_elem.parent,p_word.parent) 				
				elif (p_elem.parent.name.lower() == 'th' and s_elem.parent.name.lower() == 'td' and p_elem.parent.parent.parent == s_elem.parent.parent.parent) or ((s_elem.parent.name.lower() == 'td' or s_elem.parent.name.lower() == 'th') and (p_elem.parent.name.lower() == 'td' or p_elem.parent.name.lower() == 'th') and s_elem.parent.parent == p_elem.parent.parent): 
					distance = 1
				print "distance: ",distance
				if distance == -1:
					continue
				#do some distance manipulation
				if distance < min_distance or min_distance == -1:
					min_distance = distance
					min_s_word = s_elem
					s_tag = s_elem.parent.name
			if min_distance != -1:
				print "appending"
				distances.append(float(min_distance))
	final_score = 0
	for x in distances:
		if x != 0:
			final_score += 1.0/(x/2)
	return 1 if final_score > 1 else final_score

def calc_same_tag_distance(p_elem, p_word):
	counter = 0
	p_elem = re.sub(r'[^\w]', ' ', p_elem)
	temp_s_words = re.findall(r'\b((1[4-9]\d\d)|(20((1[0-4])|(0\d))))\b',p_elem)
	s_words_list = []
	for tup in temp_s_words:
		s_words_list.append(tup[0])
	p_found = False
 	s_found = False
 	minCounter = -1
	for word in p_elem.split(" "):
		for s_word in s_words_list:
			counter += 1
			if word == p_word:
				p_found = True
				if s_found == False:
					counter = 1
			if word == s_word:
				s_found = True
				if p_found == False: 
					counter = 1
			if p_found and s_found:
				if minCounter == -1 or counter < minCounter:
					minCounter = counter
				break
	return minCounter




