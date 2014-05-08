#!/usr/bin/python

import re

with open('test.html') as f:
	contents = f.read().replace('\n','')
	plain_text = []
	
	# Strip out all of the HTML tags
	start_pos = 0 # To just get us into the while loop
	while start_pos > -1:
		start_pos = contents.find('<')
		if start_pos > -1:
			end_pos = contents.find('>',start_pos)
			if end_pos > -1:
				# Get just the tag, and remove leading/trailing spaces
				tag = contents[start_pos+1:end_pos].strip()
				# Update contents to be without that tag
				contents = contents[:start_pos] + " " + contents[end_pos:]

				if tag[0] != '/': # Don't do ending tags
					if tag[-1] == '/': # Strip trailing slashes
						tag = tag[:-1] 
					parts = tag.split(' ')
					tag_type = parts[0]
					parts = parts[1:]
					print "TAG:" + tag_type
					if len(parts) > 0:
						print "   " + " ".join(parts)
			else:	
				# Well, *this* is awkward. The tag never got closed
				print "PROBLEM: Never found a closing bracket for a tag"					
				exit()

	# At this point, 'contents' should just contain the text of the document, without tags

	# Strip percent-escaped chars
	contents = re.sub('%[0-9]{2}','',contents)
	# Strip ampersand-escaped chars
	contents = re.sub('&[^;]+;','',contents)

	# strip punctuation
	contents = re.sub('[^ a-zA-Z0-9]','',contents).lower()
	words = re.split(' +',contents)
	for word in words:
		print "WORD:{0}".format(word)
	
