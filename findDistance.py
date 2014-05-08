#Sean Teeling steeling@calpoly.edu

primary_words = ["Dorthey"]
secondary_words = ["1904"]
def parse_doc(doc):
	distances = []			#[(primary_word, secondary, distance), ]

	soup = BeautifulSoup(doc)
	
	for p_word in primary_words:								#grab each hotword
		for p_elem in soup(text=re.compile(p_word)): 			#grab each occurrence of the hot word
			p_tag = p_elem.name
			min_distance = -1
			for s_word in secondary_words:						#compare to each secondary word
				for s_elem in soup(text=re.compile(s_word))		#grab each occurrence of the secondary word
					distance = calc_distance(p_elem,s_elem)
					if distance < min_distance or min_distance == -1:
						min_distance = distance
						min_s_word = s_word
						s_tag = s_elem.name
			distances.append((p_word,min_s_word,min_distance,p_tag,s_tag))			


def calc_distance(p_elem, s_elem, p_word, s_word):
	if p_elem.name.lower == 'p' or p_elem.name.lower == 'pre': #if it is in a paragraph
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
	#not else because words might have not been in same paragraph
	counter = 0
	

