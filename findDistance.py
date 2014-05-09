#Sean Teeling steeling@calpoly.edu

from bs4 import BeautifulSoup
import re

primary_words = ["Dorthey"]
secondary_words = ["1904"]
def parse_doc(doc):
	distances = []			#[(primary_word, secondary, distance), ]

	soup = BeautifulSoup(doc)
	
	for p_word in primary_words:								#grab each hotword
		for p_elem in soup(text=re.compile(p_word)): 			#grab each occurrence of the hot word
			p_tag = p_elem.parent.name
			min_distance = -1
			for s_word in secondary_words:						#compare to each secondary word
				for s_elem in soup(text=re.compile(s_word)):		#grab each occurrence of the secondary word
					distance = -1
					print "hello", s_elem, p_elem, s_elem.name, p_elem.name
					if s_elem == p_elem:
						distance = calc_same_tag_distance(p_elem,s_elem,p_word,s_word)
					elif (s_elem.parent.name.lower() == 'td' or s_elem.parent.name.lower() == 'th') and (p_elem.parent.name.lower() == 'td' or p_elem.parent.name.lower() == 'th') and s_elem.parent.parent == p_elem.parent.parent: 
						distance = 1
					print distance
					if distance == -1:
						continue
					#do some distance manipulation
					if distance < min_distance or min_distance == -1:
						print "in here"
						min_distance = distance
						min_s_word = s_word
						s_tag = s_elem.parent.name
			distances.append((p_word,min_s_word,min_distance,p_tag,s_tag))	
	return distances		

def calc_same_tag_distance(p_elem, s_elem, p_word, s_word):
	counter = 0
	p_found = False, s_found = False
	for word in p_elem:
		counter += 1
		if word == p_word and s_found == False:
			counter = 0
		if word == s_word:
			s_found = True
			if p_found == False: counter = 0
		if p_found and s_found:
			return counter
